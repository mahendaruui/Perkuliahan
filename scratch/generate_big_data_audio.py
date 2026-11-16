#!/usr/bin/env python3
"""Generate Indonesian narration MP3s for the Big Data decks using macOS say + ffmpeg."""
from __future__ import annotations

import json
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "scratch" / "big_data_audio_manifest.json"
OUT = ROOT / "docs" / "public" / "audio" / "big-data"
TMP = Path("/private/var/folders/l2/q_h8fjrs0tx7mbqh6yq_7rp00000gn/T/opencode/bigdata-audio")
VOICE = "Damayanti"
RATE = "165"


def synth(module: str, index: int, text: str) -> str:
    dest_dir = OUT / module
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"slide-{index:02d}.mp3"
    if dest.exists() and dest.stat().st_size > 1000:
        return f"skip {dest.relative_to(ROOT)}"
    aiff = TMP / f"{module}-{index:02d}.aiff"
    aiff.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["say", "-v", VOICE, "-r", RATE, "-o", str(aiff), text],
        check=True,
    )
    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error",
            "-i", str(aiff),
            "-codec:a", "libmp3lame", "-qscale:a", "4", "-ac", "1",
            str(dest),
        ],
        check=True,
    )
    aiff.unlink(missing_ok=True)
    return f"ok   {dest.relative_to(ROOT)}"


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    jobs = []
    for module, texts in manifest.items():
        for index, text in enumerate(texts, 1):
            jobs.append((module, index, text))

    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(synth, *job) for job in jobs]
        for future in as_completed(futures):
            print(future.result(), flush=True)
    print(f"Selesai: {len(jobs)} narasi.")


if __name__ == "__main__":
    main()
