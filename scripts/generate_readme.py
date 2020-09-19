from pathlib import Path
import re


def a(link, title):
    return f'<a href="{link}">{title}</a>'

def li(el):
    return f"<li>{el}</li>"

def ul(*args):
    return "<ul>\n" + "\n".join(args) + "\n</ul>"

def replace_toc(original, text):
    return re.sub(
            r"(<!-- TOC -->)(.*)(<!-- ENDTOC -->)",
            r"\1\n%s\n\3"%text,
            original,
            flags = re.MULTILINE | re.DOTALL
            )


p = Path("posts")
readme = Path("README.md")

entries = []
for post in p.glob("*.md"):
    m = re.match("# (.*)", post.read_text())
    if m is None:
        raise ValueError("Cannot match title for post: %s" %post)

    entries.append((str(post), m.group(1)))

html = ul(*[li(a(*entry)) for entry in entries])

print("README", readme.read_text())
print(replace_toc(readme.read_text(), html))
