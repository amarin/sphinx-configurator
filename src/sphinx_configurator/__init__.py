# -*- coding: utf-8 -*-

__version__ = '0.3.1'

from datetime import datetime

from sphinx_configurator.builders.confluence import init_confluence
from sphinx_configurator.builders.latexpdf import init_latex
from sphinx_configurator.configurable import ConfigFile
from sphinx_configurator.constants import CONFIGURATION_SECTION_MAIN
from sphinx_configurator.constants import CONFIGURATION_SECTION_METADATA
from sphinx_configurator.extensions import Plugin
from sphinx_configurator.main_params import init_main_params


def setup(app):
    """Populate Sphinx configuration based on ini file"""
    config_file = ConfigFile(app, 'setup.cfg')

    metadata = config_file.get_section(CONFIGURATION_SECTION_METADATA)
    metadata.configure('project', 'Default project')
    metadata.configure('package', 'default')
    metadata.configure('author', 'Unknown author')
    metadata.configure('copyright', "{year}, {author}".format(
        year=datetime.now().year,
        author=metadata.author
    ))

    init_main_params(app, config_file)

