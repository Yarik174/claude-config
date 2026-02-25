#!/usr/bin/env python3
"""
Создать папку сессии продуктового интервью и скопировать шаблоны.

Пример:
  python3 scripts/init_session.py --topic "Новый продукт для бухгалтеров"
  python3 scripts/init_session.py --topic "CRM виджет" --base-dir .workflow/.product-interview
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
from pathlib import Path


def slugify(text: str, max_len: int = 40) -> str:
    s = (text or "").strip().lower()
    s = s.replace("ё", "е")
    s = re.sub(r"[^a-z0-9а-я]+", "-", s, flags=re.IGNORECASE)
    s = s.strip("-")
    s = re.sub(r"-{2,}", "-", s)
    if not s:
        return "session"
    return s[:max_len].strip("-") or "session"


def main() -> int:
    parser = argparse.ArgumentParser(description="Init product interview session folder")
    parser.add_argument("--topic", required=True, help="Тема/название продукта (для slug)")
    parser.add_argument(
        "--base-dir",
        default=".workflow/.product-interview",
        help="Базовая директория для сессий",
    )
    parser.add_argument(
        "--date",
        default=None,
        help="Дата YYYY-MM-DD (по умолчанию сегодня)",
    )
    args = parser.parse_args()

    skill_dir = Path(__file__).resolve().parents[1]
    templates_dir = skill_dir / "assets" / "templates"
    if not templates_dir.exists():
        raise SystemExit(f"Templates dir not found: {templates_dir}")

    date = dt.date.today() if not args.date else dt.date.fromisoformat(args.date)
    session_id = f"PI-{slugify(args.topic)}-{date.isoformat()}"

    base_dir = Path(args.base_dir).resolve()
    out_dir = base_dir / session_id
    out_dir.mkdir(parents=True, exist_ok=False)

    for template in ("interview-notes.md", "prd-seed.md", "open-questions.md"):
        src = templates_dir / template
        dst = out_dir / template
        shutil.copy2(src, dst)

    (out_dir / "session.txt").write_text(
        "\n".join(
            [
                f"session_id: {session_id}",
                f"topic: {args.topic}",
                f"date: {date.isoformat()}",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

