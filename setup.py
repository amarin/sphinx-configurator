#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup configuration"""
import os
from glob import glob
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

setup(
    name="sphinx_configurator",
    license="Media-Tel proprietary",
    author="Aleksey Marin",
    author_email="asmadews@gmail.com",
    include_package_data=True,
    platforms="POSIX",
    version="0.1.0",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[
        splitext(os.path.basename(path))[0] for path in glob('src/*.py')
    ],
    zip_safe=False,
    long_description="Sphinx Extension configurator",
    description="Sphinx Extension configurator",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Environment :: Sphinx',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'console_scripts': [
            'make_sphinx-docs = sphinx_configurator.sphinx_wrapper:main',
            'configure_docs = sphinx_configurator.cmdline.init:init_docs'
        ],
        'distutils.commands': [
            'make_sphinx_docs = sphinx_configurator.setup_command:Build',

        ],
    },
)
