import markdown
from flask import Markup


def md_to_html(filename):
    exts = ["markdown.extensions.extra", "markdown.extensions.codehilite", "markdown.extensions.tables",
            "markdown.extensions.toc"]

    with open(filename, 'r', encoding="utf-8") as f:
        md_content = f.read()

    content = markdown.markdown(md_content, extensions=exts)
    html = Markup(content)
    return html
