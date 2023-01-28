from recommonmark.parser import CommonMarkParser

project = "Research Computing\nUniversity of São Paulo"

master_doc = 'index'

source_parsers = {
    '.md': CommonMarkParser,
}

extensions = [
    'sphinx_markdown_tables',
]

source_suffix = ['.rst', '.md']
