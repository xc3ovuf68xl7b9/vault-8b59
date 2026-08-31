from __future__ import annotations

import json
from pathlib import Path


def load_items(path: Path) -> list[dict]:
    raw = path.read_text(encoding="utf-8")
    data = json.loads(raw) if raw.strip().startswith(("[", "{")) else [
        {"line": line} for line in raw.splitlines() if line.strip()
    ]
    if not isinstance(data, list):
        raise ValueError("expected a JSON list or a text file")
    return data


def watch(items: list[dict], key: str = "id") -> list[dict]:
    seen: set[str] = set()
    out: list[dict] = []
    for item in items:
        token = str(item.get(key, item))
        if token in seen:
            continue
        seen.add(token)
        out.append(item)
    return out
