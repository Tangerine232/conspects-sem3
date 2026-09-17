from __future__ import annotations

from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "index.html"
README_PATH = ROOT / "README.md"

SUBJECTS = [
    (
        "Теоретическая механика",
        "Ирина Юрьевна Потоцкая",
        ROOT / "subjects/01-theoretical-mechanics/theormech.tex",
        "subjects/01-theoretical-mechanics/theormech.pdf",
    ),
    (
        "Математический анализ",
        "Мария Александровна Скопина",
        ROOT / "subjects/02-mathematical-analysis/matan.tex",
        "subjects/02-mathematical-analysis/matan.pdf",
    ),
    (
        "Теория функций комплексной переменной",
        "Александр Дмитриевич Овсянников",
        ROOT / "subjects/03-complex-analysis/tfcv.tex",
        "subjects/03-complex-analysis/tfcv.pdf",
    ),
    (
        "Теория групп и теория чисел",
        "Александр Владимирович Кривошеин",
        ROOT / "subjects/04-group-theory-number-theory/gtnt.tex",
        "subjects/04-group-theory-number-theory/gtnt.pdf",
    ),
    (
        "Дифференциальные уравнения",
        "Алексей Петрович Жабко",
        ROOT / "subjects/05-differential-equations/di_furry.tex",
        "subjects/05-differential-equations/di_furry.pdf",
    ),
    (
        "Численные методы",
        "Сергей Иванович Перегудин",
        ROOT / "subjects/06-numerical-methods/chislaki.tex",
        "subjects/06-numerical-methods/chislaki.pdf",
    ),
    (
        "Базы данных и сетевые технологии",
        "Мария Анатольевна Малинина",
        ROOT / "subjects/07-databases-network-technologies/bdst.tex",
        "subjects/07-databases-network-technologies/bdst.pdf",
    ),
]

HTML_START_MARKER = "<!-- PROGRESS_TABLE_START -->"
HTML_END_MARKER = "<!-- PROGRESS_TABLE_END -->"
README_START_MARKER = "<!-- README_PROGRESS_START -->"
README_END_MARKER = "<!-- README_PROGRESS_END -->"
NEWLECTION_RE = re.compile(r"\\newlection\s*\{([^{}]+)\}")


def strip_comments(text: str) -> str:
    cleaned_lines = []
    for line in text.splitlines():
        match = re.search(r"(?<!\\)%", line)
        if match:
            line = line[: match.start()]
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


def latest_lection(tex_path: Path) -> str | None:
    if not tex_path.exists():
        return None

    text = tex_path.read_text(encoding="utf-8")
    matches = NEWLECTION_RE.findall(strip_comments(text))
    return matches[-1].strip() if matches else None


def build_html_table() -> str:
    rows = []

    for subject_name, lecturer, tex_path, pdf_href in SUBJECTS:
        latest = latest_lection(tex_path)
        if latest:
            progress = f'<span class="lecture-progress">Лекция от {escape(latest)}</span>'
        else:
            progress = '<span class="not-started">—</span>'

        rows.append(
            "      <tr>\n"
            "        <td>\n"
            f'          <a href="{escape(pdf_href, quote=True)}">{escape(subject_name)}</a><br>\n'
            f'          <span class="lecturer">{escape(lecturer)}</span>\n'
            "        </td>\n"
            f"        <td>{progress}</td>\n"
            "      </tr>"
        )

    return (
        f"{HTML_START_MARKER}\n"
        '<table class="progress-table">\n'
        "  <thead>\n"
        "    <tr>\n"
        "      <th>Предмет</th>\n"
        "      <th>Последняя написанная лекция</th>\n"
        "    </tr>\n"
        "  </thead>\n"
        "  <tbody>\n"
        + "\n".join(rows)
        + "\n  </tbody>\n"
        "</table>\n"
        f"{HTML_END_MARKER}"
    )


def build_readme_table() -> str:
    rows = [
        "| Предмет | Последняя написанная лекция |",
        "|---|---|",
    ]

    for subject_name, lecturer, tex_path, pdf_href in SUBJECTS:
        latest = latest_lection(tex_path)
        progress = f"Лекция от {latest}" if latest else "—"
        rows.append(
            f"| {lecturer}, [{subject_name}]({pdf_href}) | {progress} |"
        )

    return (
        f"{README_START_MARKER}\n"
        + "\n".join(rows)
        + f"\n{README_END_MARKER}"
    )


def replace_marked_block(text: str, start_marker: str, end_marker: str, replacement: str) -> str:
    if start_marker not in text or end_marker not in text:
        raise RuntimeError(
            f"Markers were not found: {start_marker!r} / {end_marker!r}"
        )

    before, rest = text.split(start_marker, 1)
    _, after = rest.split(end_marker, 1)
    return before + replacement + after


def main() -> None:
    html = INDEX_PATH.read_text(encoding="utf-8")
    html = replace_marked_block(
        html,
        HTML_START_MARKER,
        HTML_END_MARKER,
        build_html_table(),
    )
    INDEX_PATH.write_text(html, encoding="utf-8")

    readme = README_PATH.read_text(encoding="utf-8")
    readme = replace_marked_block(
        readme,
        README_START_MARKER,
        README_END_MARKER,
        build_readme_table(),
    )
    README_PATH.write_text(readme, encoding="utf-8")

    for subject_name, _, tex_path, _ in SUBJECTS:
        latest = latest_lection(tex_path)
        print(f"{subject_name}: {latest or '—'}")


if __name__ == "__main__":
    main()
