#!/usr/bin/env python3
"""Generate small gallery thumbnails from the numbered original artwork."""
from pathlib import Path
from PIL import Image, ImageOps, UnidentifiedImageError

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
PREVIEWS = ASSETS / "previews"
KINDS = ("backgrounds", "borders", "stickers")
EXTS = {".png", ".jpg", ".jpeg", ".webp"}
SIZE = (150, 150)

for kind in KINDS:
    source_dir = ASSETS / kind
    dest_dir = PREVIEWS / kind
    dest_dir.mkdir(parents=True, exist_ok=True)
    if not source_dir.exists():
        print(f"Skipping missing {source_dir}")
        continue
    generated = set()
    for source in sorted(source_dir.iterdir()):
        if not source.is_file() or source.suffix.lower() not in EXTS or not source.stem.isdigit():
            continue
        target = dest_dir / f"{int(source.stem)}.webp"
        if target.name in generated:
            raise RuntimeError(f"Multiple originals for {kind}/{source.stem} with different extensions")
        generated.add(target.name)
        # Regenerate on every run: correctly handles edits to existing images.
        try:
            with Image.open(source) as original:
                img = ImageOps.exif_transpose(original)
                has_alpha = img.mode in ("RGBA", "LA") or "transparency" in img.info
                img = img.convert("RGBA" if has_alpha else "RGB")
                img.thumbnail(SIZE, Image.Resampling.LANCZOS)
                img.save(target, "WEBP", quality=76, method=6)
                print(f"Created {target.relative_to(ROOT)} ({target.stat().st_size:,} bytes)")
        except (UnidentifiedImageError, OSError) as exc:
            raise RuntimeError(f"Could not process {source}: {exc}") from exc
    # Remove stale previews when numbered artwork is removed.
    for old in dest_dir.glob("*.webp"):
        if old.name not in generated:
            old.unlink()
            print(f"Removed stale {old.relative_to(ROOT)}")
