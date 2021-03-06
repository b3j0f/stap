#!/usr/bin/env python
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2014 Jonathan Labéjof <jonathan.labejof@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# --------------------------------------------------------------------

"""b3j0f project building script."""

from setuptools import setup, find_packages

from os.path import abspath, dirname, join

from re import compile as re_compile, S as re_S

NAME = 'b3j0f.stap'  # project name

_namepath = NAME.replace('.', '/')

_base_path = dirname(abspath(__file__))

# get long description from setup directory abspath
with open(join(_base_path, 'README.rst')) as f:
    DESC = f.read()

# Get the version - do not use normal import because it does break coverage
# thanks to the python jira project
# (https://github.com/pycontribs/jira/blob/master/setup.py)
with open(join(_base_path, _namepath, 'version.py')) as f:
    stream = f.read()
    regex = r'.*__version__ = \'(.*?)\''
    VERSION = re_compile(regex, re_S).match(stream).group(1)

KEYWORDS = ['save time after party', 'tools']

DEPENDENCIES = []

DESCRIPTION = 'Set of tools and utilities useful in python projects'

URL = 'https://github.com/{0}'.format(_namepath)

setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(exclude=['test.*', '*.test.*']),
    author='b3j0f',
    author_email='jlabejof@yahoo.fr',
    install_requires=DEPENDENCIES,
    description=DESCRIPTION,
    long_description=DESC,
    include_package_data=True,
    url=URL,
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: French',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
    test_suite='b3j0f',
    scripts=['scripts/mdateorganize'],
    keywords=KEYWORDS
)
