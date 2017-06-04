#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# hubble2 documentation build configuration file

import alabaster

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'alabaster'
]

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# general project information
project = 'hubble2'
copyright = '2017, Zack Buhman'
#version = hubble2.__version__
#release = hubble2.__version__

# styles
pygments_style = 'sphinx'
highlight_language = 'python3'

# The theme to use for HTML and HTML Help pages.
html_theme = 'alabaster'
html_theme_path = [alabaster.get_path()]

html_theme_options = {
    'description': 'General-purpose environment manager',
    'github_user': 'buhman',
    'github_repo': 'hubble2',
    'github_button': True,
    'github_type': 'star',
    'github_banner': True,
    'shield_list': [
        {
            'image': 'https://img.shields.io/circleci/project/github/buhman/hubble2.svg',
            'target': 'https://circleci.com/gh/buhman/hubble2'
        },
        {
            'image': 'https://img.shields.io/codecov/c/github/buhman/hubble2.svg',
            'target': 'https://codecov.io/gh/buhman/hubble2'
        },
        {
            'image': 'https://img.shields.io/pypi/v/hubble2.svg',
            'target': 'https://pypi.org/project/hubble2/'
        }
    ]
}

html_sidebars = {
    '**': [
        'about.html', 'navigation.html', 'searchbox.html',
    ]
}
