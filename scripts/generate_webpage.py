from pathlib import Path
from string import Template
import markdown

md = markdown.Markdown(extensions=['toc'])

class CustomTemplate(Template):
    delimiter = '{{'
    pattern = r'''
    \{\{(?:
    (?P<escaped>\{\{)|
    (?P<named>[_a-z][_a-z0-9]*)\}\}|
    (?P<braced>[_a-z][_a-z0-9]*)\}\}|
    (?P<invalid>)
    )
    '''

template = CustomTemplate(
    Path("_template.html").read_text()
    )

posts = sorted(Path("posts").glob("*.md"))
content = "\n".join([md.convert(p.read_text()) for p in posts])

print(template.substitute(content = content), end = "")
