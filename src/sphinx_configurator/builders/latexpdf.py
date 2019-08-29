# -*- coding: utf-8 -*-
from os import path

from sphinx.application import Sphinx

from sphinx_configurator.configurable import ConfigFile
from sphinx_configurator.configurable import set_config_value
from sphinx_configurator.constants import NOTSET


def load_preamble(file_path=NOTSET):
    """Load preamble from predefined or user-specified path"""
    if file_path == NOTSET:
        file_path = path.join(path.dirname(__file__), 'latexpdf_preamble.tex')
    with open(file_path, 'rb') as preamble_fh:
        preamble = preamble_fh.read().decode()
        return preamble


def init_latex(app, config):
    """Configure confluence builder options"""
    assert isinstance(app, Sphinx)
    assert isinstance(config, ConfigFile)
    config.assert_has_section('metadata')

    # Use xalatex
    set_config_value(app, 'latex_engine', 'xelatex')

    # Paper spec
    set_config_value(app, 'latex_paper_size', 'a4')

    # Show urls in footnotes
    set_config_value(app, 'latex_show_urls', 'footnotes')

    # Use international build
    set_config_value(app, 'latex_use_xindy', True)

    # Add specific indicies
    set_config_value(app, 'latex_domain_indices', True)

    latex_preamble = load_preamble()

    set_config_value(app, 'latex_elements', {
        'preamble': latex_preamble,
        'pointsize': '10pt',
        'fncychap': '',
        'extraclassoptions': 'openany,oneside',
        'sphinxsetup': 'hmargin={1in,1in}, vmargin={1in,1in}, marginpar=0.1in',
    })

    latex_document = (
        app.config['master_doc'],  # source start file
        app.config['package'] + '.tex',  # result file name
        app.config['project'],  # title
        app.config['author'],  # author
        'manual',  # documentclass [howto/manual]
        False
    )

    set_config_value(
        app,
        'latex_documents',
        [latex_document]
    )
