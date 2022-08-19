# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'The high-frequency MRI database'
copyright = '2022, Edde'
author = 'Edde'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    "rightsidebar": "False",
    "relbarbgcolor": "black"
}

html_css_files = [
    'custom.css'
]

# -- Options for EPUB output
epub_show_urls = 'footnote'
