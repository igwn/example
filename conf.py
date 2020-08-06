# Configuration file for the Sphinx documentation builder.

# Inherit IGWN defaults.
from sphinx_igwn.conf import *


# -- Project information -----------------------------------------------------

project = 'Sphinx IGWN Example'
# author = 'LIGO Scientific Collaboration, Virgo Collaboration, KAGRA Collaboration'
# copyright = '2020, LIGO Scientific Collaboration, Virgo Collaboration, KAGRA Collaboration'


# -- Options for LaTeX output ------------------------------------------------

latex_documents = [
    (master_doc, 'SphinxIGWNExample.tex', project,
     author , 'manual'),
]


# -- Extension configuration -------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions += [
    # 'matplotlib.sphinxext.plot_directive',
]


# -- Options for intersphinx extension ---------------------------------------

# Add intersphinx mappings here to cross-reference other documentation sets.
intersphinx_mapping.update({
    # 'astropy': ('https://docs.astropy.org/en/stable/', None),
})
