# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys, os

sys.path.append(os.path.abspath('exts'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CanMV'
copyright = '2022 Canaan Inc'
author = 'Canaan'
# release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton',
    'myst_parser',
    'sphinx_multiversion',
    'sphinxcontrib.mermaid'
]

html_js_files = [
    'https://cdnjs.cloudflare.com/ajax/libs/mermaid/8.13.8/mermaid.min.js',
    'init_mermaid.js',
]

html_static_path = ['_static']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

myst_heading_anchors = 4
suppress_warnings = ["myst.header"]

html_copy_source = False
html_show_sourcelink = False

html_favicon = 'favicon.ico'

# html_show_sphinx = False

# html_theme = 'alabaster'
html_theme = "sphinx_book_theme"
html_static_path = ['_static']
html_copy_source = True
html_show_sourcelink = False

# if want to add top nav for canann, enable this.
# html_css_files = ['topbar.css']
html_css_files = ['topbar.css', 'custom-theme.css']

html_theme_options = {
    "repository_url": "https://github.com/kendryte/canmv_docs",
    'collapse_navigation': True,
    'navigation_depth': 7,
    "use_edit_page_button": True,
    "use_edit_page_button": True,
    "show_navbar_depth": 2,
    "primary_sidebar_end": ["versionsFlex.html"],
}
