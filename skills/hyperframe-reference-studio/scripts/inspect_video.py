#!/usr/bin/env python3
"""Verify duration and extract MP4 evidence without modifying the input."""
import argparse
import hashlib
import json
import shutil
import subprocess
from decimal import Decimal, InvalidOperation
from pathlib import Path


def finite_decimal(value):
    try:
        result = Decimal(value)
        if not result.is_finite():
            raise InvalidOperation
        return result
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError("Expected a finite number of seconds") from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path)
    parser.add_argument("--out", type=Path, required=True, help="New directory; must not exist")
    parser.add_argument("--times", required=True, help="1–60 comma-separated seconds")
    parser.add_argument("--expected-duration", type=finite_decimal)
    args = parser.parse_args()
    if not args.video.is_file():
        parser.error("Input must be an existing regular video file")
    if args.out.exists() or args.out.is_symlink():
        parser.error("Output already exists; choose a new directory")
    ffmpeg, ffprobe = shutil.which("ffmpeg"), shutil.which("ffprobe")
    if not ffmpeg or not ffprobe:
        parser.error("ffmpeg and ffprobe must be on PATH")
    try:
        times = [finite_decimal(value.strip()) for value in args.times.split(",")]
    except argparse.ArgumentTypeError as exc:
        parser.error(str(exc))
    if args.expected_duration is not None and args.expected_duration <= 0:
        parser.error("Expected duration must be positive")
    try:
        raw = subprocess.check_output(
            [ffprobe, "-v", "error", "-show_format", "-show_streams", "-of", "json", str(args.video.resolve())],
            text=True,
        )
        metadata = json.loads(raw)
        duration = finite_decimal(metadata["format"]["duration"])
        if not any(stream.get("codec_type") == "video" for stream in metadata["streams"]):
            parser.error("Input has no video stream")
        if not times or len(times) > 60 or any(time < 0 or time >= duration for time in times):
            parser.error("Provide 1–60 timestamps from zero up to, but excluding, the duration")
        if args.expected_duration is not None and duration != args.expected_duration:
            parser.error(f"Duration mismatch: expected {args.expected_duration}, measured {duration}")
        args.out.mkdir(parents=True, exist_ok=False)
        # Reports omit the input's absolute local path. Media tags are retained.
        metadata["format"]["filename"] = args.video.name
        (args.out / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
        digest = hashlib.sha256()
        with args.video.open("rb") as source:
            for chunk in iter(lambda: source.read(1024 * 1024), b""):
                digest.update(chunk)
        frames = []
        for index, time in enumerate(times):
            name = f"frame-{index + 1:03d}.jpg"
            target = args.out / name
            subprocess.run(
                [ffmpeg, "-hide_banner", "-loglevel", "error", "-nostdin", "-ss", str(time),
                 "-i", str(args.video.resolve()), "-frames:v", "1", "-q:v", "2", str(target.resolve())], check=True,
            )
            if not target.is_file() or target.stat().st_size == 0:
                raise RuntimeError(f"No decoded frame at {time}")
            frames.append({"file": name, "requested_time_seconds": str(time)})
        columns = min(3, len(frames))
        rows = (len(frames) + columns - 1) // columns
        subprocess.run(
            [ffmpeg, "-hide_banner", "-loglevel", "error", "-nostdin", "-framerate", "1",
             "-i", str((args.out / "frame-%03d.jpg").resolve()), "-vf",
             f"scale=320:-1,tile={columns}x{rows}:padding=6:margin=6:color=0x202029",
             "-frames:v", "1", "-q:v", "2", str((args.out / "contact-sheet.jpg").resolve())], check=True,
        )
        manifest = {"source": args.video.name, "sha256": digest.hexdigest(), "duration_seconds": str(duration),
                    "frames": frames, "note": "Requested seek positions; visual inspection is still required."}
        (args.out / "frames.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"output": str(args.out), "duration": str(duration), "frames": len(frames)}, ensure_ascii=False))
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.CalledProcessError, argparse.ArgumentTypeError) as exc:
        parser.exit(1, f"Inspection failed: {exc}\n")


if __name__ == "__main__":
    main()
