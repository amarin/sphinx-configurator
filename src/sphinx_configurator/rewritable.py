# -*- coding: utf-8 -*-
from os import path

from sphinx_configurator.constants import NOTSET

DEFAULT_PATH = path.join(path.dirname(__file__), 'defaults')


def rewritable_file_path(app, filename, default_path=NOTSET):
    """Get filepath in documentation src or default in sphinx_configurator"""
    src_dir = app.srcdir
    found_path = path.join(src_dir, filename)
    if path.exists(found_path):
        return found_path

    if default_path is NOTSET:
        default_path = path.dirname(__file__)
    return path.join(default_path, filename)


def rewritable_file_content(app, filename):
    """Get rewritable file content"""
    file_path = rewritable_file_path(app, filename, path.dirname(__file__))
    with open(file_path, 'rb') as content_fh:
        content = content_fh.read().decode()
        return content
