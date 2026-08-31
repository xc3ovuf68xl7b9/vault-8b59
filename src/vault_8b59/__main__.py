from __future__ import annotations

import argparse
import json
from pathlib import Path

from .core import load_items, watch


def main() -> int:
    parser = argparse.ArgumentParser(description="vault-8b59 — small watch utility")
    parser.add_argument("path", type=Path)
    parser.add_argument("--key", default="id")
    args = parser.parse_args()
    items = watch(load_items(args.path), key=args.key)
    print(json.dumps(items, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
