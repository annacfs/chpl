# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

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

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
#html_theme = "sphinx_rtd_theme"
html_static_path = ["_static", f"{docset}/_static"]
html_css_files = ["css/custom.css", "css/sphinx_prompt_css.css"]
html_js_files = ["js/expand_tabs.js"]
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_logo = "docs/img/logo.svg"
html_theme_options = {
    "logo_only": True,
    "display_version": False,
}
# -- Options for EPUB output
epub_show_urls = 'footnote'
