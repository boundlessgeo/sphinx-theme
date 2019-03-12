Sphinx themes for Boundless documentation
========================================

This repository contains reusable themes for documentation at Boundless. To use these themes, pull this repository in as a submodule to your desired Sphinx project, and build with a custom theme parameter.

Sphinx Themes
-------------

First generation themes fork and customize built-in sphinx themes:

* **boundless_learning** - theme is shared by tutorials and workshops maintained by Boundless Learning

* **boundless_product** - This theme is to be used by Boundless products, namely Suite, Desktop, and Exchange. There is a variable ("product") in the code to toggle between the three options.

* **boundless_doc** - This theme is shared and used by all qgis plugins documentation through the [qgis-plugins-documentation repository](https://github.com/boundlessgeo/qgis-plugins-documentation).

Second generation themes extend built-in sphinx themes:

* ***boundless_rtd*** - extends *sphinx_rtd_theme* with boundless branding
* ***boundless_standalone*** extends *boundless_rtd* removing the sidebar and navigation, for standalone boundless-branded pages, such as the docs.boundlessgeo.com landing page.
* ***boundless_slides*** - extends *slides* theme with boundless branding
* ***boundless_single*** - extends *single-level* with boundless branding

The built-in themes are supplied by (we include a local copy for reference):

```
pip3 install sphinx
pip3 install hieroglyph
pip3 install sphinx_rtd_theme
```

Test Project
------------

This project includes a test project as a reference for theme development:

* test - offers a stress test of sphinx theming based on our writing guidelines

Landing Page
------------

This project provides a landing page for docs.boundlessgeo.com, which links to downstream documentation.
