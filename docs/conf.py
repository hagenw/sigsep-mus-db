# -*- coding: utf-8 -*-

import os

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = 'default'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'numpydoc'
]

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'dsdtools'
copyright = u'2016, Fabian-Robert Stöter'
author = u'Fabian-Robert Stöter'

version = u'0.1.1'
release = u'0.1.1'

language = None

exclude_patterns = ['_build']

pygments_style = 'sphinx'

todo_include_todos = False

html_static_path = ['_static']

htmlhelp_basename = 'dsdtoolsdoc'

latex_elements = {
}

latex_documents = [
  (master_doc, 'dsdtools.tex', u'dsdtools Documentation',
   u'Fabian-Robert Stöter', 'manual'),
]

man_pages = [
    (master_doc, 'dsdtools', u'dsdtools Documentation',
     [author], 1)
]

texinfo_documents = [
  (master_doc, 'dsdtools', u'dsdtools Documentation',
   author, 'dsdtools', 'One line description of project.',
   'Miscellaneous'),
]

# Fake imports to avoid actually loading NumPy and libsndfile
import fake_numpy
sys.modules['numpy'] = sys.modules['fake_numpy']
import fake_cffi
sys.modules['cffi'] = sys.modules['fake_cffi']
