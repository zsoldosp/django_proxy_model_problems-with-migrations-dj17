#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

setup(
    name='django-proxy-model-problems',
    version='0.0.1',
    description="""Proxy model strangeness repro""",
    author='Peter Zsoldos',
    author_email='hello@zsoldosp.eu',
    packages=[
        'django_proxy_model_problems',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
)
