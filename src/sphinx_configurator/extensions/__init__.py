# -*- coding: utf-8 -*-
import glob
import importlib
import types
from abc import abstractmethod
from os import path

from sphinx.application import Sphinx

from sphinx_configurator import ConfigFile
from sphinx_configurator.constants import OPTION_PLUGIN_DIR
from sphinx_configurator.constants import OPTION_PLUGIN_DIR_DEFAULT
from sphinx_configurator.constants import SECTION_PLUGINS_NAME


class Plugin(object):
    """Documentation builder plugin"""

    def __init__(self, app, config):
        assert isinstance(app, Sphinx)
        assert isinstance(config, ConfigFile)
        self.app = app
        self.config = config

    @abstractmethod
    def run(self):
        """Run plugin before builders"""
        pass

    @classmethod
    def get_plugins_dir(cls, app, config):
        """Get plugins dir"""
        assert isinstance(app, Sphinx)
        assert isinstance(config, ConfigFile)
        plugins_config = config.get_section(SECTION_PLUGINS_NAME)
        return plugins_config.get(OPTION_PLUGIN_DIR, OPTION_PLUGIN_DIR_DEFAULT)

    @classmethod
    def get_plugins(cls, app, config):
        plugins_dir = Plugin.get_plugins_dir(app, config)
        if not path.exists(plugins_dir):
            return
        plugins_pattern = path.join(plugins_dir, '*.py')

        def plugin_modules():
            """Generate plugin modules"""
            for module_path in glob.glob(plugins_pattern):
                m = importlib.import_module(module_path)
                assert isinstance(m, types.ModuleType)
                yield m

        def plugin_classes():
            """Generate plugin instances"""
            for m in plugin_modules():
                names = (x for x in m.__dict__)
                items = (m.__getattribute__(x) for x in names)
                classes = (x for x in items if type(x) == type)
                plugins = (x for x in classes if issubclass(x, Plugin))
                for plugin_class in plugins:
                    yield plugin_class

        # generate instances
        return (x(app, config) for x in plugin_classes())

    @classmethod
    def run_all_found(cls, app, config):
        """Run all found plugins"""
        for plugin in cls.get_plugins(app, config):
            plugin.run()
