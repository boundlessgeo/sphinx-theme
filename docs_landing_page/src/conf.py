import sys, os
import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

now = datetime.datetime.now()

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.todo', 'sphinx.ext.ifconfig', 'sphinx.ext.intersphinx', 'sphinx.ext.extlinks']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_template']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Boundless Documentation Index'
copyright = u'{} Boundless'.format(now.year)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = str(now.year)
# The full version, including alpha/beta/rc tags.
release = str(now.year)

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
today = ''

#External links
extlinks = {
    # boundless server
    'server': ('http://server.boundlessgeo.com/docs/latest/%s',''),
    'geoserver': ('http://server.boundlessgeo.com/docs/latest/geoserver/%s',''),
    'geos': ('https://osgeo-org.atlassian.net/browse/GEOS-%s','GEOS-'),
    'geot': ('https://osgeo-org.atlassian.net/browse/GEOT-%s','GEOT-'),
    'openlayers': ('https://openlayers.org/en/latest/%s',''),
    'postgresql': ('http://www.postgresql.org/docs/current/static/%s',''),
    'postgis': ('http://postgis.net/docs/manual-2.4/%s',''),

    # boundless desktop
    'desktop': ('https://connect.boundlessgeo.com/docs/desktop/latest/%s',''),
    'qgis': ('https://docs.qgis.org/2.18/en/docs/%s',''),
    'pgadmin': ('https://www.pgadmin.org/docs/pgadmin4/1.x/%s',''),
    'gdal': ('http://www.gdal.org/%s',''),
    'ogr': ('http://www.gdal.org/$s',''),

    # boundless customer
    'egnyte-files': ('https://boundlessgeo.egnyte.com/dl/%s',''),
    'training-files': ('http://training-files.boundlessgeo.com/%s',''),
    'connect': ('https://connect.boundlessgeo.com/%s',''),
    'leaning-center': ('https://learning-center.boundlessgeo.com/%s',''),

    # internal
    'sphinx': ('http://www.sphinx-doc.org/en/master/%s','')
}

# -- Options for HTML output ---------------------------------------------------


# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'boundless_standalone'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

# theme options for server_rtd_theme
html_theme_options = {
    'display_version': False, # No version number
    'prev_next_buttons_location': 'none', # use sidebar to navigate
    'display_connect': False
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['../..']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = 

html_short_title = "Boundless Documentation"

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False
html_copy_source = False


# Output file base name for HTML help builder.
htmlhelp_basename = "Boundless Documentation"


# Documents to append as an appendix to all manuals.

# along with |release| |version| and |today|
rst_epilog = """
.. |theme| replace:: {theme}
""".format(theme=html_theme)
