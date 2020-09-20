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

content = "\n".join([md.convert(p.read_text()) for p in Path("posts").glob("*.md")])

print(template.substitute(content = content), end = "")
