# -*- coding: utf-8 -*-
from os import path
from setuptools import setup, find_packages
from tdsc import __version__
from io import open

here = path.abspath(path.dirname(__file__))

packages = ['tdsc']

package_data = {'': ['*']}

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    install_requires = f.read().split('\n')

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup_kwargs = {
    'name': 'tdsc',
    'version': __version__,
    'description': 'Tiny, simple desired state configuration',
    'long_description': long_description,
    'author': 'Liam Dawson',
    'author_email': 'liam@ldaws.com',
    'url': 'https://github.com/liamdawson/tdsc/',
    'packages': find_packages(),
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7,!3.0,!3.1,!3.2,!3.3,<4.0',
    'classifiers': [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    'include_package_data': True,
}


setup(**setup_kwargs)
