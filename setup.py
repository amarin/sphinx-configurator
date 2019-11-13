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
    license="MIT",
    author="Aleksey Marin",
    author_email="asmadews@gmail.com",
    platforms="POSIX",
    version="0.3.1",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[
        splitext(os.path.basename(path))[0] for path in glob('src/*.py')
    ],
    zip_safe=False,
    package_data={'sphinx_configurator': ['locale/*/LC_MESSAGES/*.mo']},
    include_package_data=True,
    long_description="Sphinx Extension configurator",
    description="Sphinx Extension configurator",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Plugins',
        'Framework :: Sphinx :: Extension',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation'
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
    setup_requires=[
        "Jinja2"
    ]

)
