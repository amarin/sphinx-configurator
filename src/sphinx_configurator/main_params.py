# -*- coding: utf-8 -*-
from sphinx.application import Sphinx

from sphinx_configurator import ConfigFile
from sphinx_configurator import init_confluence
from sphinx_configurator import init_latex
from sphinx_configurator.builders.htmldir import init_html
from sphinx_configurator.configurable import set_config_value
from sphinx_configurator.utils import get_main_sphinx_section_name

builders_order = {
    'confluence': init_confluence,
    'latex': init_latex,
    'html': init_html
}


def init_main_params(app, config):
    """Configure confluence builder options"""
    assert isinstance(app, Sphinx)
    assert isinstance(config, ConfigFile)

    sphinx_config = config.get_section(get_main_sphinx_section_name())
    builders = sphinx_config.builder

    for builder_name, builder_init in builders_order.items():
        if builder_name not in builders:
            continue
        builder_init(app, config)

    # Filenames extensions
    source_suffix = ['.rst']
    set_config_value(app, 'source_suffix', source_suffix)

    # Main document
    master_doc = 'index'
    set_config_value(app, 'master_doc', master_doc)

    # Main language
    language = 'ru'
    set_config_value(app, 'language', language)

    # Exclude some file and folder patterns
    exclude_patterns = []
    set_config_value(app, 'exclude_patterns', exclude_patterns)

    # Numerate figures
    numfig = True
    set_config_value(app, 'numfig', numfig)

    # Figure numbers follow section numbering upto 2 level depth
    numfig_secnum_depth = 2
    set_config_value(app, 'numfig_secnum_depth', numfig_secnum_depth)

    # Code highlight style
    pygments_style = 'friendly'
    set_config_value(app, 'pygments_style', pygments_style)

    # Format date
    today_fmt = '%x'
    set_config_value(app, 'today_fmt', today_fmt)

    templates_path = ['_templates']
    set_config_value(app, 'templates_path', templates_path)

    # Setup additional extensions
    app.setup_extension('sphinx_vcs_changelog')
