"""Test distribution boundaries and failure cases, not just rendered appearances."""
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "hyperframe-reference-studio"


def run_helper(name, *args):
    return subprocess.run([sys.executable, str(SKILL / "scripts" / name), *map(str, args)], capture_output=True, text=True)


class ProjectCopyTests(unittest.TestCase):
    def test_portable_copy_contains_required_assets_and_licenses(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "project"
            result = run_helper("new_project.py", output)
            self.assertEqual(result.returncode, 0, result.stderr)
            for file in ["index.html", "index.motion.json", "package-lock.json", "LICENSE", "NOTICE",
                         "THIRD_PARTY_NOTICES.md", "assets/fonts/OFL.txt", "assets/fonts/NotoSansKR.woff2",
                         "scripts/setup-assets.mjs"]:
                self.assertTrue((output / file).is_file(), file)
            for forbidden in ["node_modules", "assets/vendor", "out.mp4", "review", ".hyperframes"]:
                self.assertFalse((output / forbidden).exists(), forbidden)
            original = SKILL / "assets/studio-demo/assets/fonts/NotoSansKR.woff2"
            self.assertEqual(hashlib.sha256(original.read_bytes()).digest(),
                             hashlib.sha256((output / "assets/fonts/NotoSansKR.woff2").read_bytes()).digest())

    def test_existing_directory_is_preserved(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            sentinel = output / "index.html"
            sentinel.write_text("user-owned work", encoding="utf-8")
            result = run_helper("new_project.py", output)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(sentinel.read_text(), "user-owned work")
            self.assertEqual(list(output.iterdir()), [sentinel])

    def test_symlink_destination_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            existing = base / "existing"
            existing.mkdir()
            link = base / "link"
            link.symlink_to(existing, target_is_directory=True)
            result = run_helper("new_project.py", link)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(list(existing.iterdir()), [])


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "FFmpeg/ffprobe required")
class VideoEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.base = Path(self.temporary.name)
        self.video = self.base / "input.mp4"
        self.output = self.base / "review"
        subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i", "color=c=blue:s=64x96:r=30",
                        "-t", "0.2", "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", str(self.video)], check=True)
        self.digest = hashlib.sha256(self.video.read_bytes()).digest()

    def tearDown(self):
        self.assertEqual(self.digest, hashlib.sha256(self.video.read_bytes()).digest())
        self.temporary.cleanup()

    def inspect(self, *args):
        return run_helper("inspect_video.py", self.video, "--out", self.output, *args)

    def test_duration_mismatch_leaves_no_false_evidence(self):
        result = self.inspect("--times", "0", "--expected-duration", "0.3")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Duration mismatch", result.stderr)
        self.assertFalse(self.output.exists())

    def test_invalid_timestamps_are_rejected_before_writing(self):
        for invalid in ["NaN", "Infinity", "hello", "-0.1", "0.2", "0,"]:
            with self.subTest(value=invalid):
                result = self.inspect("--times", invalid)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(self.output.exists())

    def test_decode_manifest_and_no_overwrite(self):
        result = self.inspect("--times", "0,0.1", "--expected-duration", "0.200000")
        self.assertEqual(result.returncode, 0, result.stderr)
        manifest = json.loads((self.output / "frames.json").read_text())
        self.assertEqual(manifest["duration_seconds"], "0.200000")
        self.assertEqual(manifest["source"], "input.mp4")
        self.assertEqual(manifest["sha256"], self.digest.hex())
        for item in manifest["frames"]:
            self.assertGreater((self.output / item["file"]).stat().st_size, 0)
        self.assertTrue((self.output / "contact-sheet.jpg").is_file())
        before = (self.output / "frames.json").read_bytes()
        second = self.inspect("--times", "0", "--expected-duration", "0.2")
        self.assertNotEqual(second.returncode, 0)
        self.assertEqual(before, (self.output / "frames.json").read_bytes())


if __name__ == "__main__":
    unittest.main()
