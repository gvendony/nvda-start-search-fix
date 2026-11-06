"""Builds the .nvda-addon package into dist/. Docs are generated from the READMEs."""

import html
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent
ADDON = ROOT / "addon"
DIST = ROOT / "dist"
DOCS = {"en": "README.md", "hu": "README.hu.md"}


def inline(text: str) -> str:
	text = html.escape(text, quote=False)
	text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
	return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)


def to_html(markdown: str, lang: str) -> str:
	body = []
	open_list = None
	for line in markdown.splitlines():
		match = re.match(r"(#+) (.*)", line)
		item = re.match(r"(-|\d+\.) (.*)", line)
		tag = ("ol" if item.group(1)[0].isdigit() else "ul") if item else None
		if open_list and tag != open_list:
			body.append(f"</{open_list}>")
			open_list = None
		if match:
			level = len(match.group(1))
			body.append(f"<h{level}>{inline(match.group(2))}</h{level}>")
		elif item:
			if not open_list:
				body.append(f"<{tag}>")
				open_list = tag
			body.append(f"<li>{inline(item.group(2))}</li>")
		elif line.strip():
			body.append(f"<p>{inline(line)}</p>")
	if open_list:
		body.append(f"</{open_list}>")
	title = re.search(r"<h1>(.*?)</h1>", "".join(body)).group(1)
	content = "\n".join(body)
	return (
		f'<!DOCTYPE html>\n<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n'
		f"<title>{title}</title>\n</head>\n<body>\n{content}\n</body>\n</html>\n"
	)


def main() -> None:
	manifest = (ADDON / "manifest.ini").read_text(encoding="utf-8")
	name = re.search(r"^name = (.+)$", manifest, re.M).group(1).strip()
	version = re.search(r"^version = (.+)$", manifest, re.M).group(1).strip()
	DIST.mkdir(exist_ok=True)
	target = DIST / f"{name}-{version}.nvda-addon"
	with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
		for path in sorted(ADDON.rglob("*")):
			if path.is_file() and "__pycache__" not in path.parts:
				archive.write(path, path.relative_to(ADDON).as_posix())
		archive.write(ROOT / "LICENSE", "LICENSE")
		for lang, source in DOCS.items():
			text = (ROOT / source).read_text(encoding="utf-8")
			text = re.sub(r"^\[[^\]]*\]\(README[^)]*\)\n\n", "", text, flags=re.M)
			archive.writestr(f"doc/{lang}/readme.html", to_html(text, lang))
	print(target)


if __name__ == "__main__":
	main()
