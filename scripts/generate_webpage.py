from pathlib import Path

template = Path("_template.html").read_text()

content = "\n".join([p.read_text() for p in Path("posts").glob("*.md")])

print(template.format(content = content), end = "")
