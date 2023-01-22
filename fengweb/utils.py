try:
    from urlparse import urlparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin

import markdown
from flask import Markup, request, redirect, url_for


def md_to_html(filename):
    exts = ["markdown.extensions.extra", "markdown.extensions.codehilite", "markdown.extensions.tables",
            "markdown.extensions.toc"]

    with open(filename, 'r', encoding="utf-8") as f:
        md_content = f.read()

    content = markdown.markdown(md_content, extensions=exts)
    html = Markup(content)
    return html


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def redirect_back(default='blog.index', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))
