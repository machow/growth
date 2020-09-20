from pathlib import Path
from string import Template

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

content = "\n".join([p.read_text() for p in Path("posts").glob("*.md")])

print(template.format(content = content), end = "")
