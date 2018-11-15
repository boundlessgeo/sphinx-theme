Workbook
********

.. slideconf::
   :theme: slides
   :autoslides: True

Use of ``slides`` theme.

.. ifnotslides::
   
   For the following section break to work ``rst-class:: section`` is used to mark the heading
   appropriately.

.. rst-class:: section

Style Guidelines
================

.. ifnotslides::

   This section concerns the tone to use when writing text for pages.

   These writing guidelines are compatible with the writing style of Boundless Server, which are extension of the GeoServer `Documentation Guide <http://docs.geoserver.org/latest/en/docguide/style.html>`__ instructions.

   This section concerns the tone to use when writing text for pages.

.. ifnotslides::

   Reference:

   * :server:`Boundless Server User Manual <>`
   * `Style Guidelines <http://docs.geoserver.org/latest/en/docguide/style.html>`__ (GeoServer Documentation Guide)

Be concise
----------

Style guide: *Documentation should be concise and not just a brain dump. Reference material should contain short pages and be easy to refer to without having to scroll through a large volume of text.  Tutorials can be longer, depending on scope.  If the point of the document is to share your thoughts and insights, it belongs in a blog post.  This documentation is a manual, not a wiki.*

.. nextslide::
   :increment:

For training materials we fall under "tutorials". Concise writing, with the understanding that understand that repetition, and taking multiple perspectives on the same subject matter, is required to communicate key ideas.

* For key ideas we often looking to communicate through a) text b) diagram c) hands-on step-by-step instructions.

* Consider to how to communicate the idea using both GIS professional terms, and IT professional terms.

Avoid marketing
---------------

Style guide: *If the point of the document is to showcase a new feature it does not belong in the documentation. Write an article or a blog post about it. If it is necessary to point out a technical benefit of a feature then do so from a technical standpoint.*

Bad
   Super-overlays are a great way to publish super cool datasets awesomely in Google Earth!
Good
   Super-overlays allow you to efficiently publish data via Google Earth.

.. nextslide::
   :increment:

Training is in-between marketing and documentation and marketing.

Many attending our instruction are being introduced to the product for the first time and we have a goal to entertain and get attendees excited about the technology and how it can be applied in their organization.

Guidance: Please leave feature-promotion to the description of the technology, and instructor notes. Needless verbiage, however enthusiastic, should not distrupt from step by step instructions.

Be professional
---------------

Style Guide: *Avoid the use of slang or other "colorful" language. The point of a technical document is to be informative, not to keep the reader amused.  Avoiding slang helps keep the document accessible to as large an audience as possible.*

Bad
   Next, fire up whatever tool you use to browse the web and point it in the direction of ...
Good
   Next, start your web browser and navigate to ...

.. nextslide::
   :increment:

Guidance: This is a difficult a difficult balance for training material, when teaching internationally simple consistent professional langague works best. If you have a some a colorful story, or description, please add as an instructor notes.

Use direct commands
-------------------

Style Guide: *When providing step-by-step instructions, use direct commands or requests. Avoid the use of "we" and "let's".*

Bad
   Now let's add a shapefile by ...
Good
   Add a shapefile by ...

Naming conventions
------------------

Reference:

* `Wikipedia naming conventions <http://en.wikipedia.org/wiki/Wikipedia:Naming_conventions>`_.

.. nextslide:: Naming: Capitalization of page names

Capitalization of page names: Each word in the page name should be capitalized except for articles (such as "the", "a", "an") and conjunctions (such as "and", "but", "or"). A page name should never start with an article.

Bad
   Adding a shapefile or postgis table
Good
   Adding a Shapefile or PostGIS Table

Bad
   The Shapefile Tutorial
Good
   Shapefile Tutorial

.. nextslide:: Naming: Capitalization of section names

Capitalization of section names: Do not capitalize second and subsequent words unless the title is almost always capitalized in English (like proper names). Thus, capitalize John Wayne and Art Nouveau, but not Video Games.

Bad
   Creating a New Datastore
Good
   Creating a new datastore

.. nextslide:: Naming: Verb usage

Verb usage: It is recommended that the gerund (the -ing form in English) be used unless there is a more common noun form. For example, an article on swimming is better than one on swim.

Bad
   Create a new datastore
Good
   Creating a new datastore

.. nextslide:: Naming: Avoid plurals

Avoid plurals: Create page titles that are in the singular.  Exceptions to this are nouns that are always plural (scissors, trousers), a small class that requires a plural (polar coordinates, Bantu languages, The Beatles).

Bad
   Templates tutorial
Good
   Template tutorial

Formatting
----------

Any code or command line snippets should be formatted as code::

   This is a code block.

When considering PDF output we have some hard limitations on lines are longer than 77 characters. Please use multiple lines in a format appropriate for the language in use.

If possible, snippets should be functional when pasted directly into the appropriate target.

.. nextslide::
   :increment:

For example, Java and XML make no distinction between a single space and multiple spaces, so the following snippets are fine::

   org.geoserver.package.Object someVeryLongIdentifier =
      org.geoserver.package.Object.factoryMethod();

::

   <namespace:tagname attributename="attributevalue"
      attribute2="attributevalue" nextattribute="this is on another line"/>

.. nextslide::
   :increment:

For shell scripts, new lines can be escaped with a backslash character :kbd:`\\`. It is also recommended to use a simple ``$`` prompt to save space. For example::

   $ /org/jdk1.5.0*/bin/java \
      -cp /home/user/.m2/repository/org/geoserver/*/*.jar \
      org.geoserver.GeoServer \
      -DGEOSERVER_DATA_DIR=/var/lib/geoserver_data/release

For windows commands, characters can be escaped with a :kbd:`^` character, but it is so unusual that it is not recommended.

.. rst-class:: section

Sphinx Inline Directives
========================

.. ifnotslides::
   
   First section on writing incline directives using rich-structured-text, with examples for workbook consistency.

   Reference:

   * :sphinx:`Sphinx documentation contents <contents.html>`

Basic markup
------------

A reStructuredText document is written in plain text.  Without the need for complex formatting, one can be composed simply, just like one would any plain text document.  For basic formatting, see this table:

.. list-table::
   :widths: 30 40 30

   * - **Format**
     - **Syntax**
     - **Output**
   * - Emphasis, single asterisk
     - :kbd:`*italics*`
     - *italics*
   * - Strong Emphasis, double asterisk
     - :kbd:`**bold**`
     - **bold**
   * - Inline literal, double back quote
     - :kbd:`\`\`monspace\`\``
     - ``monspace``
     
.. nextslide:: Use of directives

Common Inline Directives
-------------------------

We tending to avoid the use of Basic markup, preferring inline directives, which document function rather than appearance.

.. list-table::
   :widths: 30 40 30

   * - **Format**
     - **Syntax**
     - **Output**

   * - Keyboard input, :command:`kbd` directive
     - :kbd:`:kbd:\`control-a\``
     - :kbd:`control-a`
   * - File reference, :command:`file` directive
     - :kbd:`:file:\`setup.txt\``
     - :file:`setup.txt`
   * - Button or label, :command:`guilabel` directive
     - :kbd:`:guilabel:\`OK\``
     - :guilabel:`OK`
   * - Application or command, :command:`command` directive
     - :kbd:`:command:\`gdalinfo\``
     - :guilabel:`gdalinfo`

This approach is used to allow styling to change the appearance of user interface buttons, keyboard input, command line tools.

Inline literal
--------------

Use inline literals to name layers, tables, and columns. This is do to avoid possibility of error when copying these texts into queries, configurations or requests.

.. code-block:: rst
   
   Select the ``name`` column in the ``nyc_streets`` table.

Example:

Select the ``name`` column in the ``nyc_streets`` table.

Reference commands and applications
-----------------------------------

Reference commands (such as :command:`pgsql`) with the following syntax:

.. code-block:: rst

   Use :command:`pgAdmin` to administration applications to connect
   to the PostgresSQL server running on localhost.

.. code-block:: rst

   Alternatively use :command:`psql` interactive session:

   .. code-block:: bat

      psql -U postgres nyc

Reference an label or button in a user interface
------------------------------------------------

Use :command:`guilabel` to direct a user to click a link or look to a certain area of the GUI:

.. code-block:: rst

   #. Click :guilabel:`View connection details` to open the :guilabel:`PostGIS connection` information.

Menu or user interface traversal
--------------------------------

Direct a user through a menubar with the following syntax:

.. code-block:: rst

   :menuselection:`Start Menu --> Programs --> GeoServer`

This will output :menuselection:`Start Menu --> Programs --> GeoServer`.

.. nextslide::
   :increment:

Consistently refer to:

* :guilabel:`menubar` for the application or window menubar
* :guilabel:`toolbar` for the application or window toolbar

.. code-block:: rst

   #. From the :guilabel:`DB Manager` menubar select :menuselection:`Table --> Import layer/file`.

.. nextslide::
   :increment:

This approach also works for user interface traversal:

.. code-block:: rst

   #. With :guilabel:`Databases` selected in the browser select
      :menuselection:`Object --> Create --> Database` to open
      the :guilabel:`Create Database` dialog.

File Paths
----------

To refer to files or paths:

.. code-block:: rst

   :file:`file.txt`
   :file:`/var/lib/opengeo/geoserver/`
   :file:`C:\\ProgramData\\Boundless\\Server\GeoServer\\data`

Example:

| :file:`file.txt`
| :file:`/var/lib/opengeo/geoserver/`
| :file:`C:\\ProgramData\\Boundless\\Server\GeoServer\\data`

.. nextslide::
   :increment:

Use the following syntax to reference files and paths::

   :file:`myfile.txt`

This will output: :file:`myfile.txt`.

.. nextslide::
   :increment:

You can reference paths in the same way:

.. code-block:: rst

   :file:`path/to/myfile.txt`

This will output: :file:`path/to/myfile.txt`.

.. nextslide::
   :increment:

For Windows paths, use double backslashes:

.. code-block:: rst

   :file:`C:\\myfile.txt`

This will output: :file:`C:\\myfile.txt`.

.. nextslide::
   :increment:

If you want to reference a non-specific path or file name:

.. code-block:: rst

   :file:`{your/own/path/to}/myfile.txt`

This will output: :file:`{your/own/path/to}/myfile.txt`


URL Links
---------

URLs included in text are recognized and show up as links.

.. code-block:: rst

   http://sphinx-doc.org/rest.html

Adding a URL to text can be done as follows.

.. code-block:: rst

   `reStructured Text Primer <http://sphinx-doc.org/rest.html>`_

To avoid a duplicate URL error when a URL is used a second time on a different page:

.. code-block:: rst

   `reStructured Text Primer <http://sphinx-doc.org/rest.html>`__

.. nextslide::
   :increment:

Avoid separating out references (as shown below) as it is confusing:

.. code-block:: rst

   `reStructured Text Primer`_

   .. _reStructured Text Primer: http://sphinx-doc.org/rest.html


File Downloads
--------------

Text snippets, large blocks of downloadable code, and even zip files or other binary sources can all be included as part of the documentation.  To include files as part of the build process, use the following syntax:

.. nextslide:: Download

Use ``download`` directives to include configuration files and icons in the workbook.

.. code-block:: rst

   #. First, download this airports style
      (:download:`airports.sld <files/airports.sld>`)
      to your host system.

      .. note:: You can right-click or Ctrl-click (OS X) the above file name to save it.

Example:

3. First, download this airports style
   (:download:`airports.sld <files/airports.sld>`)
   to your host system.

   .. note:: You can right-click or Ctrl-click (OS X) the above file name to save it.


External Links
-----------------------------

We have enabled the external link extension in :file:`configy.py`.

For this workbook we defined:

.. code-block:: python

   extlinks = {
    'sphinx': ('http://www.sphinx-doc.org/en/master/%s',''),
     ...
   }

Allowing any sphinx documentation page to be referenced as an external link:

.. code-block:: rst

   :sphinx:`reStructured Text Primer <rest.html>`

.. nextslide::
   :increment:

This approach is used for all documentation references:

* server - latest boundless server docs

  .. code-block:: rst

     * :server:`Boundless Server <index.html>`
     * :server:`Installing Boundless Server on Windows <install/windows/index.html>`

* geoserver - geoserver user manual, matching boundless server

  .. code-block:: rst

     * :geoserver:`GeoServer Users Manual <index.html>`
     * :geoserver:`GeoServer Styling Workshop <styling/workshop/index.html>` (GeoServer Users Manual)

* postgresql - latest postgresql manual

  .. code-block:: rst

     * :postgresql:`PostgerSQL Manual <index.html>`
     * :postgresql:`createdb <app-createdb.html>`
     * :postgresql:`CREATE EXTENSION <sql-createextension.html>` - add an extension to the current database
     * :postgresql:`CREATE INDEX <sql-createindex.html>`

* postgis - latest postgis manual

  .. code-block:: rst

     * :postgis:`PostGIS Manual <index.html>`
     * :postgis:`Creating a spatial database using EXTENSIONS <postgis_installation.html#create_new_db_extensions>`

* desktop - boundless desktop docs
* qgis
* pgadmin
* gdal - for gdal command references
* ogr - to link to ogr command references
* training-files - used to reference downloads associated with training materials

  .. code-block:: rst

     Download from the following link: :training-files:`data bundle <postgis/postgis-workshop.zip>`

* connect
* learning-center - LMS location

Less commonly used:

* geos - geoserver bug ticket

  .. code-block:: rst

     For more information, please see the JIRA issue :geos:`GEOS-7917 <GEOS-7917>`.

* geot - geotools bug ticket

We pull these out as external links because the location of the latest docs changes over time.

* It also gives us the option of generating out the docs with references to docs on localhost for off-line use.

* These may be configured to use docs.boundlessgeo.com (rather than community website).

Although we have pulled the above definitions out into a shared :file:`conf.py` file, you can add to the list using:

.. code-block:: python

   # External links
   extlinks = global_conf.extlinks
   extlinks.update({
       'sphinx': ('http://www.sphinx-doc.org/en/master/%s',''),
   })

Sphinx Block Directives
========================

.. ifnotslides::
   
   Second section on writing block directives, commonly used to orgnaize blocks of content.

   Reference:

   * :sphinx:`Sphinx documentation contents <contents.html>`

Block Directives
----------------

Block directives are more commonly used to organize blocks of content:

.. code-block:: rst

   .. pull-quote::

      OGC(R) standards are technical documents that detail interfaces or encodings.

      -- Open Geospatial Consortium

* Use spaces, not tabs for indenting
* Align text with start of the directive

Comments
--------

.. code-block:: rst

   .. this is a comment that does not appear in the generated workbook

.. code-block:: rst

   ..
      multi line comments
      are supported

.. nextslide::

directives always end with ``::``, you can quickly "comment out" a working directive:

.. code-block:: rst

   .. code-block:: shell

      $ tail -f *

By chaning to a single ``:``, turning this code example in a hidden comment:

.. code-block:: rst
   :emphasize-lines: 1

   .. code-block: shell

      $ tail -f *

Lists
-----

There are two types of lists, bulleted lists and numbered lists.  A **bulleted list** is accomplished using:

.. code-block:: rst

   * An item
   * Another item
   * Yet another item

Bulleted list example:

* An item
* Another item
* Yet another item

.. nextslide:: Number List

A **numbered list**:

.. code-block:: rst

   #. First item
   #. Second item
   #. Third item

Numbered-list example:

#. First item
#. Second item
#. Third item

.. nextslide::

Numbers are automatically generated, making it easy to add/remove items.

Double check the generated numbering, occasionally if you get the indenting wrong the list will restart at one throwing your instructions off.

List tables
-----------

Bulleted lists can sometimes be cumbersome and hard to follow.  When dealing with a long list of items, use list-tables.  For example, to talk about a list of options, create a table that looks like this:

.. code-block:: rst

   .. list-table::
      :widths: 20 80
      :header-rows: 1

      * - Shapes
        - Description
      * - Square
        - Four sides of equal length, 90 degree angles
      * - Rectangle
        - Four sides, 90 degree angles

.. nextslide:: List Table

List table example

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Shapes
     - Description
   * - Square
     - Four sides of equal length, 90 degree angles
   * - Rectangle
     - Four sides, 90 degree angles

.. nextslide:: List Table Dialog Input Example

A common example documenting dialog input for an exercise step:

.. code-block:: rst

   #. On the :guilabel:`General` supply the database name and owner.

      .. list-table::
         :widths: 30 70
         :stub-columns: 1

         * - Database
           - :kbd:`training`
         * - Owner
           - :kbd:`postgres`

      .. figure:: img/create_database.png

         Create database

.. nextslide:: Simple Table

Simple tables are not recommended, as they are hard to maintain (consider adding :kbd:`Equilateral Triangle` to the table below).

.. code-block:: rst

   ========= ============================================
   Shapes    Description
   ========= ============================================
   Square    Four sides of equal length, 90 degree angles
   Rectangle Four sides, 90 degree angles
   ========= ============================================

Simple table example:

========= ============================================
Shapes    Description
========= ============================================
Square    Four sides of equal length, 90 degree angles
Rectangle Four sides, 90 degree angles
========= ============================================

.. nextslide:: Grid tables

Grid-tables are not recommended, even harder harder to maintain.

.. code-block:: rst

   +-----------+----------------------------------------------+
   | Shapes    | Description                                  |
   +===========+==============================================+
   | Square    | Four sides of equal length, 90 degree angles |
   +-----------+----------------------------------------------+
   | Rectangle | Four sides, 90 degree angles                 |
   +-----------+----------------------------------------------+

Grid table example

+-----------+----------------------------------------------+
| Shapes    | Description                                  |
+===========+==============================================+
| Square    | Four sides of equal length, 90 degree angles |
+-----------+----------------------------------------------+
| Rectangle | Four sides, 90 degree angles                 |
+-----------+----------------------------------------------+

Admonitions: Notes and Warnings
-------------------------------

When it is beneficial to have a section of text stand out from the main text, Sphinx has two such boxes, the note and the warning.  They function identically, and only differ in their coloring.  You should use notes and warnings sparingly, however, as adding emphasis to everything makes the emphasis less effective.

.. nextslide:: note

We make limited use of ``note`` and ``warning`` when writing, as they distract

.. code-block:: rst

   .. note:: You might want to temporarily set some layer transparency to make adding the ring easier.

Example:

.. note:: You might want to temporarily set some layer transparency to make adding the ring easier.

When generating slides any ``note`` directives are available as from the presenters console.

.. nextslide:: Warning

The use of ``warning`` should be reserved for really common mistakes that have a history of class disruption.

.. code-block:: rst

   .. warning:: Please be sure to use :command:`Firefox` as we are making use of its ability to display JSON and XML output in a readable fashion.

Example:

.. warning:: Please be sure to use :command:`Firefox` as we are making use of its ability to display JSON and XML output in a readable fashion.

.. nextslide:: Admonition

We also use the generic ``admonition`` directive to isolate our exercise into boxes visually.

.. code-block:: rst

   .. admonition:: Explore

      What is the difference between the ``CRS:84`` and ``EPSG:4326``
      spatial reference systems?

.. admonition:: Explore

   What is the difference between the ``CRS:84`` and ``EPSG:4326``
   spatial reference systems?

.. ifnotslides::

   Reference:

   * :sphinx:`Directives <usage/restructuredtext/basics.html#rst-directives>`

Instructor notes
----------------

We use the ``only`` directive, combined with our ant :file:`build.xml` script, to provide an instructor specific build of the workbooks.

To provide notes that only an instructor will see (such as an answer to an Explore section):

.. code-block:: rst

   .. admonition:: Explore

      What is the difference between the ``CRS:84`` and ``EPSG:4326``?

      .. only:: instructor

         .. admonition:: Instructor Notes

            The difference is the strict definition of axis order.

.. nextslide:: Workbook

Build with ``ant workbook`` example output:

.. admonition:: Explore

   What is the difference between the ``CRS:84`` and ``EPSG:4326``?

.. nextslide:: Instructor

Build with ``ant instructor`` example output:

.. admonition:: Explore

   What is the difference between the ``CRS:84`` and ``EPSG:4326``?

   .. admonition:: Instructor Notes

      The difference is the strict definition of axis order.

Images
------

Add images to your documentation when possible.  Images, such as screenshots, are a very helpful way of making documentation understandable.  When making screenshots, try to crop out unnecessary content (browser window, desktop, etc).  Avoid scaling the images, as the Sphinx theme automatically resizes large images.  It is also helpful to include a caption underneath the image.

.. nextslide::
   :increment:

For images, use the ``figure`` directive and add a caption. Place the image files in an ``img`` directory:

.. code-block:: rst

   .. figure: img/welcome.png

      Welcome page for the installer

When given the option 8-bit PNG are preferred (text remains readable and file size is smaller). There are some tools (https://pngquant.org)

.. nextslide::
   :increment:

Directory structure::

  src/section/index.rst - section being written
  src/section/img       - images and screen shots used in section/index.rst above
  src/index.rst         - start of module
  src/config.py

Screenshots
-----------

* Change Windows 10 Background to *sold color* with *white* for easier screen capture

  .. figure:: img/screensnap-background.png
     :width: 50%

     Settings Personalization Background

.. nextslide::
   :increment:

* Change Windows 10 Colors to *transparency effects* off, automatically pick accent color from background, don't show accent colors on taskbar or title bars

  .. figure:: img/screensnap-color.png
     :width: 50%

     Settings Personalization Color

.. nextslide::
   :increment:

* Stick to clipping out screen and dialog content (so the result is more cross platform)
* Remove obvious version numbers (so we do not have to update constantly)

.. nextslide::
   :increment:

* This course is written and tested with Firefox, so use Firefox for screen snaps
* When making screen snaps of GeoServer or any web app determine the minimum width before horizontal scroll bars appear.
* Take a crop of the page, rather than include the browser window.
* Crop to the full width of the form ignoring navigation menu (rather than have the size change from step to step).
* Use width percentage as required for consistent look for navigation menu.

.. nextslide::
   :increment:

.. tip:: On MacOS use :command:`System Preferences` navigate to :menuselection:`Keyboard --> Shortcuts` and ensure :guilabel:`Copy a picture of section area to the clipboard` is mapped to :kbd:`shift-command-4`. You can then paste the clipboard into the :command:`Preview` application and save ther result as png.

.. tip:: On Windows you can use the :command:`Snip` tool to capture cropped images, or use :kbd:`Alt-Shift-F12` to copy the current window to the clipboard.

There are several tools, example https://pngquant.org, for bulk converting images to :file:`PNG`.

Icons
-----

It is technically possible to show icons such as toolbar buttons inline, using  substitutions.

.. code-block:: rst

   #. From the :menuselection:`toolbar` select :guilabel:`Save` ( |save| ) to make the change and remain in edit mode.

   .. |save| image:: img/save.png
             :class: inline

Example:

#. From the :menuselection:`toolbar` select :guilabel:`Save` ( |save| ) to make the change and remain in edit mode.

.. |save| image:: img/save.png
          :class: inline

We prefer to reference toolbar buttons by name:

.. code-block:: rst

   #. From the :menuselection:`toolbar` select :guilabel:`Save` to make the change and remain in edit mode.

Figures
-------

For figures, or diagrams we need to draw by hand, use the ``figure`` directive and add a caption. Place the image files in the top-level ``/figure`` directory:

.. code-block:: rst

   .. figure:: /figure/component_diagram.*

      Boundless Server component architecture

Please save both a :file:`svg` and :file:`png` image. The above snippet will use the SVG image for builders such as html, while use PDF image for PDF generation.

.. nextslide::
   :increment:

Please save the original file (adobe illustrator, sketch, inkscape) in addition to the generated SVG and PNG, although it is not used in workbook generation we would like a copy on hand in order to update the diagrams.

Directory structure::

  src/section/index.rst - section being written
  src/figure/           - illustrations including generated svg and png files
  src/index.rst         - start of module
  src/config.py

Graphic Design
--------------

Component diagrams take the time to include component logos and product groupings.

.. figure:: /figure/component_diagram.*

   Boundless Server component architecture

.. nextslide::
   :increment:

Component interaction is often illustrated with block diagrams, showing the internal components involved.

.. figure:: /figure/config_admin.*

   Interaction diagrams

.. nextslide::
   :increment:

When illustrating configuration make sure diagram exactly matches the exercise.

.. figure:: /figure/config_data.*

   Configuration Illustration

.. nextslide::
   :increment:

Follow boundless branding for icons such as GeoServer and QGIS when available.

.. figure:: /figure/components.*

   Boundless Style Guide: Components

Use of opensource logos are fine when they do not conflict with company branding (such as pgAdmin or SQL Shell above).

.. nextslide::
   :increment:

Follow boundless styleguide for use of fonts.

.. figure:: /figure/fonts.*

   Boundless Style Guide: Fonts

We may need to update our sphinx theme over time.

.. nextslide::
   :increment:

Boundless provides a range of colors for use:

.. figure:: /figure/swatch.*

   Boundless Style Guide: Color

Our illustrations use a slightly muted version of the company color palette.

Code Examples
-------------

Use ``code-block``, specifying language for syntax highlighting:

.. code-block:: rst

   .. code-block:: yaml

        - point:
            symbols:
            - mark:
                shape: star

Example:

.. code-block:: yaml

     - point:
         symbols:
         - mark:
             shape: star

.. nextslide::
   :increment:

When adding or editing emphasis the changed lines:

.. code-block:: rst

   .. code-block:: yaml
      :emphasize-lines: 4

        - point:
            symbols:
            - mark:
                shape: triangle

Example

.. code-block:: yaml
   :emphasize-lines: 4

     - point:
         symbols:
         - mark:
             shape: triangle

Literal Includes
----------------

Use ``literalinclude`` and ``download`` directives, to avoid possibility of error with config, style and data files!

.. code-block:: rst

   #. Contents of :download:`geoserver.xml <files/geoserver.xml>`:

      .. literalinclude:: files/geoserver.xml
         :language: xml

Example:

4. Contents of :download:`geoserver.xml <files/geoserver.xml>`:

   .. literalinclude:: files/geoserver.xml
      :language: xml

.. nextslide::
   :increment:

Combined with line highlighting to help direct exercises where configuration files are changed.

.. code-block:: rst

   7. Change to :file:`svg` icon as show below:

   .. literalinclude:: files/airports.ysld
      :language: yaml
      :emphasize-lines: 5-6

Example:

7. Change to :file:`svg` icon as show below:

   .. literalinclude:: files/airports.ysld
      :language: yaml
      :emphasize-lines: 4-5

.. nextslide::
   :increment:

If you want to include only part of the file use ``start-after`` and ``end-before`` (rather than line numbers). Your can also use ``prepend`` and ``append`` to keep structured text like xml or json valid.

.. code-block:: rst

   .. literalinclude:: files/airports1.sld
      :language: xml
      :start-after: <PointSymbolizer>
      :end-before: <Mark>

Example:

.. literalinclude:: files/airports1.sld
   :language: xml
   :start-after: <PointSymbolizer>
   :end-before: <Mark>

Reference:

* :sphinx:`Includes <markup/code.html#includes>`
