#!/usr/bin/env python3
"""Copy the bundled, portable demo to a NEW project directory."""
import argparse
import shutil
from pathlib import Path


def create_project(destination: Path) -> Path:
    skill = Path(__file__).resolve().parents[1]
    source = skill / "assets" / "studio-demo"
    files = ["index.html", "index.motion.json", "package.json", "package-lock.json"]
    trees = ["assets/fonts", "scripts"]
    for item in files + trees:
        if not (source / item).exists():
            raise FileNotFoundError(f"Installed template is incomplete: {item}")
    for item in ["LICENSE", "NOTICE", "THIRD_PARTY_NOTICES.md"]:
        if not (skill / item).is_file():
            raise FileNotFoundError(f"Installed skill is incomplete: {item}")
    # exist_ok=False also refuses symlinks and prevents overwriting user work.
    destination.mkdir(parents=True, exist_ok=False)
    for item in files:
        shutil.copy2(source / item, destination / item)
    for item in trees:
        shutil.copytree(source / item, destination / item)
    for item in ["LICENSE", "NOTICE", "THIRD_PARTY_NOTICES.md"]:
        shutil.copy2(skill / item, destination / item)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    try:
        create_project(args.destination)
    except (OSError, shutil.Error) as exc:
        parser.exit(1, f"Cannot create project: {exc}\n")
    print(f"Created: {args.destination}\nNext: npm ci, npm run setup, npm run lint, npm run render")


if __name__ == "__main__":
    main()
