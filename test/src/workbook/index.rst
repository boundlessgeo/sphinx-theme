Workbook
********

.. slideconf::
   :theme: boundless_slides
   :autoslides: True

.. ifslides::
   
   Theme ``boundless_slides``

Sphinx Inline Directives
========================

.. ifslides::
   
   Directives with cut-and-paste examples.

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
   :linenos:
   
   Select the ``name`` column in the ``nyc_streets`` table.

Example:

Select the ``name`` column in the ``nyc_streets`` table.

Reference commands and applications
-----------------------------------

Reference commands (such as :command:`pgsql`) with the following syntax:

.. code-block:: rst
   :linenos:

   Use :command:`pgAdmin` to administration applications to connect
   to the PostgresSQL server running on localhost.

.. code-block:: rst
   :linenos:

   Alternatively use :command:`psql` interactive session:

   .. code-block:: bat

      > psql -U postgres nyc

Reference a label or button in a user interface
-----------------------------------------------

Use :command:`guilabel` to direct a user to click a link or look to a certain area of the GUI:

.. code-block:: rst
   :linenos:

   #. Click :guilabel:`View connection details` to open the :guilabel:`PostGIS connection` information.

.. ifnotslides::

   .. admonition:: Example use of ``guilabel``
      
      #. Click :guilabel:`View connection details` to open the :guilabel:`PostGIS connection` information.

Menu or user interface traversal
--------------------------------

Direct a user through a menubar with the following syntax:

.. code-block:: rst
   :linenos:

   Launch :menuselection:`Start Menu --> Programs --> GeoServer`

.. ifnotslides::

   .. admonition:: Example use of ``menuselection``

      Launch :menuselection:`Start Menu --> Programs --> GeoServer`.

.. nextslide::
   :increment:

Consistently refer to:

* *menubar* for the application or window menubar
* *toolbar* for the application or window toolbar

.. code-block:: rst
   :linenos:

   #. From the :guilabel:`DB Manager` menubar select :menuselection:`Table --> Import layer/file`.

.. ifnotslides::

   .. admonition:: Example menubar use
   
      #. From the :guilabel:`DB Manager` menubar select :menuselection:`Table --> Import layer/file`.

.. nextslide::
   :increment:

This approach also works for user interface traversal:

.. code-block:: rst
   :linenos:

   #. With :guilabel:`Databases` selected in the browser select
      :menuselection:`Object --> Create --> Database` to open
      the :guilabel:`Create Database` dialog.

.. ifnotslides::

   .. admonition:: Example user interface traversal

      #. With :guilabel:`Databases` selected in the browser select
         :menuselection:`Object --> Create --> Database` to open
         the :guilabel:`Create Database` dialog.

File Paths
----------

To refer to files or paths:

.. code-block:: rst
   :linenos:

   :file:`file.txt`
   :file:`/var/lib/opengeo/geoserver/`
   :file:`C:\\ProgramData\\Boundless\\Server\GeoServer\\data`

.. ifnotslides::

   .. admonition:: Example use of ``file``

      | :file:`file.txt`
      | :file:`/var/lib/opengeo/geoserver/`
      | :file:`C:\\ProgramData\\Boundless\\Server\GeoServer\\data`

.. nextslide::
   :increment:

Use the following syntax to reference files and paths:

.. code-block:: rst
   :linenos:

   Create :file:`myfile.txt`

.. ifnotslides::

   .. admonition:: Example file reference
   
      Create :file:`myfile.txt`.

.. nextslide::
   :increment:

You can reference paths in the same way:

.. code-block:: rst
   :linenos:

   Navigate to :file:`path/to/mydirectory`.

.. ifnotslides::

   .. admonition:: Example path reference
   
      Navigate to :file:`path/to/mydirectory`.

.. nextslide::
   :increment:

For Windows paths, use double backslashes:

.. code-block:: rst
   :linenos:

   Use :command:`Notepad` to open :file:`C:\\myfile.txt`.

.. ifnotslides::

   .. admonition:: Example windows path
      
      Use :command:`Notepad` to open :file:`C:\\myfile.txt`.

.. nextslide::
   :increment:

If you want to reference a non-specific path or file name:

.. code-block:: rst
   :linenos:

   Save changes to :file:`{your/own/path/to}/myfile.txt`

.. ifnotslides::

   .. admonition:: Example file placeholder
      
      Save changes to :file:`{your/own/path/to}/myfile.txt`

URL Links
---------

URLs included in text are recognized and show up as links.

.. code-block:: rst
   :linenos:
   
   http://sphinx-doc.org/rest.html

.. ifnotslides::
   
   .. admonition:: Example URL reference
      
       http://sphinx-doc.org/rest.html
   
Adding a URL to text can be done as follows.

.. code-block:: rst
   :linenos:
   
   `reStructured Text Primer <http://sphinx-doc.org/rest.html>`__

.. ifnotslides::
   
   .. admonition:: Example text link
   
      `reStructured Text Primer <http://sphinx-doc.org/rest.html>`__
   
Note the use of `__` to create an anonymous reference, this avoids a duplicate URL error when a URL is used a second time on a different page.

.. nextslide::
   :increment:

Avoid separating out references (as shown below) as it is confusing:

.. code-block:: rst
   :linenos:
   
   `reStructured Text Primer`_

   .. _reStructured Text Primer: http://sphinx-doc.org/rest.html


File Downloads
--------------

Text snippets, large blocks of downloadable code, and even zip files or other binary sources can all be included as part of the documentation.  

.. ifnotslides:: To include files as part of the build process, use the following syntax:

.. nextslide:: Download

Use ``download`` directives to include configuration files and icons in the workbook.

.. code-block:: rst
   :linenos:
   
   #. First, download this airports style
      (:download:`airports.sld <files/airports.sld>`)
      to your host system.

      .. note:: You can right-click or Ctrl-click (OS X) the above file name to save it.

.. ifnotslides::
   
   .. admonition:: Example file download

      3. First, download this airports style
         (:download:`airports.sld <files/airports.sld>`)
         to your host system.

         .. note:: You can right-click or Ctrl-click (OS X) the above file name to save it.


External Links
--------------

We have enabled the external link extension in :file:`configy.py`.

For this workbook defined:

.. code-block:: python
   :lineno-start: 84
   
   extlinks = {
    'sphinx': ('http://www.sphinx-doc.org/en/master/%s',''),
     ...
   }

.. nextslide::

Allowing any sphinx documentation page to be referenced as an external link:

.. code-block:: rst
   :linenos:
   
   Reference:
   
   * :sphinx:`reStructured Text Primer <rest.html>`
   
.. ifnotslides::
   
   .. admonition:: Example external link
      
      Reference:
      
      * :sphinx:`reStructured Text Primer <rest.html>`
   
.. ifnotslides::

This approach is used for all documentation references.

.. nextslide:: Boundless Server External Links

* server - latest boundless server docs
  
  .. ifnotslides::
  
     .. code-block:: rst
        :linenos:
    
        Reference:
    
        * :server:`Boundless Server <index.html>`
        * :server:`Installing Boundless Server on Windows <install/windows/index.html>`

* geoserver - geoserver user manual, matching boundless server

  .. ifnotslides::
  
     .. code-block:: rst
        :linenos:

        Reference:
    
        * :geoserver:`GeoServer Users Manual <index.html>`
        * :geoserver:`GeoServer Styling Workshop <styling/workshop/index.html>` (GeoServer Users Manual)

* postgresql - latest postgresql manual

  .. ifnotslides::
  
     .. code-block:: rst
        :linenos:
     
        Reference:
     
        * :postgresql:`PostgerSQL Manual <index.html>`
        * :postgresql:`createdb <app-createdb.html>`
        * :postgresql:`CREATE EXTENSION <sql-createextension.html>` - add an extension to the current database
        * :postgresql:`CREATE INDEX <sql-createindex.html>`

* postgis - latest postgis manual

  .. ifnotslides::
 
     .. code-block:: rst
        :linenos:
    
        Reference:
    
        * :postgis:`PostGIS Manual <index.html>`
        * :postgis:`Creating a spatial database using EXTENSIONS <postgis_installation.html#create_new_db_extensions>`

.. nextslide:: Boundless Desktop External Links

* desktop - boundless desktop docs
* qgis
* pgadmin
* gdal - for gdal command references
* ogr - to link to ogr command references

.. nextslide:: Boundless Learning External Links

* training-files - used to reference downloads associated with training materials

  .. ifnotslides::
  
     .. code-block:: rst
        :linenos:
     
        Download from the following link: :training-files:`data bundle <postgis/postgis-workshop.zip>`

* connect
* learning-center - LMS location

.. nextslide:: Issue Trackers

Less commonly used:

* geos - geoserver bug ticket

  .. ifnotslides::
  
     .. code-block:: rst
        :linenos:
     
        For more information, please see the JIRA issue :geos:`GEOS-7917 <GEOS-7917>`.

* geot - geotools bug ticket

.. nextslide:: Custom External Links

We pull these out as external links because the location of the latest docs changes over time:

* It also gives us the option of generating out the docs with references to docs on localhost for off-line use.

* These may be configured to use docs.boundlessgeo.com (rather than community website).

.. nextslide::

Although we have pulled the above definitions out into a shared :file:`conf.py` file, you can add to the list using:

.. code-block:: python
  :lineno-start: 47
     
   # External links
   extlinks = global_conf.extlinks
   extlinks.update({
       'sphinx': ('http://www.sphinx-doc.org/en/master/%s',''),
   })

Sphinx Block Directives
========================

.. ifslides::
   
   Blocks used to organize content.

.. ifnotslides::
   
   Second section on writing block directives, used to orgnaize blocks of content.

   Reference:

   * :sphinx:`Sphinx documentation contents <contents.html>`

Block Directives
----------------

Block directives are more commonly used to organize blocks of content:

* Use spaces, not tabs for indenting
* Align text with start of the directive

.. code-block:: rst
   :linenos:
     
   .. pull-quote::

      OGC(R) standards are technical documents that detail interfaces or encodings.

      -- Open Geospatial Consortium

.. ifnotslides::
   
   .. admonition:: Example pull-quote 
      
      .. pull-quote::
         
         OGC(R) standards are technical documents that detail interfaces or encodings.
         
         -- Open Geospatial Consortium

Comments
--------

.. code-block:: rst
   :linenos:
   
   .. this is a comment that does not appear in the generated workbook

.. code-block:: rst
   :linenos:
   
   ..
      multi line comments
      are supported

.. nextslide:: Comments - Hot Tip!

Directives always end with ``::``, you can quickly "comment out" a working directive:

.. code-block:: rst
   :linenos:
    
   .. code-block:: shell

      $ tail -f *

By chaning to a single ``:``, turning this code example in a hidden comment:

.. code-block:: rst
   :linenos:
   :emphasize-lines: 1

   .. code-block: shell

      $ tail -f *

Lists
-----

There are two types of lists, bulleted lists and numbered lists.  A **bulleted list** is accomplished using:

.. code-block:: rst
   :linenos:
   
   * An item
   * Another item
   * Yet another item

.. ifnotslides::
   
   .. admonition:: Example bulleted list 

      * An item
      * Another item
      * Yet another item

.. nextslide:: Number List

A **numbered list**:

.. code-block:: rst
   :linenos:
   
   #. First item
   #. Second item
   #. Third item

.. ifnotslides::
   
   .. admonition:: Example numbered-list 

      #. First item
      #. Second item
      #. Third item

.. nextslide::

Numbers are automatically generated, making it easy to add/remove items.


.. warning:: Double check the generated numbering, occasionally if you get the indenting wrong the list will restart at one throwing your instructions off.

List tables
-----------

Bulleted lists can sometimes be cumbersome and hard to follow.  When dealing with a long list of items, use list-tables.  For example, to talk about a list of options, create a table that looks like this:

.. code-block:: rst
   :linenos:
   
   .. list-table::
      :widths: 20 80
      :header-rows: 1

      * - Shapes
        - Description
      * - Square
        - Four sides of equal length, 90 degree angles
      * - Rectangle
        - Four sides, 90 degree angles

.. ifnotslides::
   
   .. admonition:: Example list table

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
   :linenos:
   
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

Simple Table (Not Recommended)
------------------------------

Simple tables are not recommended, as they are hard to maintain (consider adding :kbd:`Equilateral Triangle` to the table below).

.. code-block:: rst
   :linenos:

   ========= ============================================
   Shapes    Description
   ========= ============================================
   Square    Four sides of equal length, 90 degree angles
   Rectangle Four sides, 90 degree angles
   ========= ============================================

.. ifnotslides::
   
   .. admonition:: Example simple table

      ========= ============================================
      Shapes    Description
      ========= ============================================
      Square    Four sides of equal length, 90 degree angles
      Rectangle Four sides, 90 degree angles
      ========= ============================================

Grid tables (Not Recommended)
-----------------------------

Grid-tables are not recommended, even harder harder to maintain.

.. code-block:: rst
   :linenos:

   +-----------+----------------------------------------------+
   | Shapes    | Description                                  |
   +===========+==============================================+
   | Square    | Four sides of equal length, 90 degree angles |
   +-----------+----------------------------------------------+
   | Rectangle | Four sides, 90 degree angles                 |
   +-----------+----------------------------------------------+

.. ifnotslides::
   
   .. admonition:: Example grid table

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
   :linenos:

   .. note:: You might want to temporarily set some layer transparency to make adding the ring easier.

.. ifnotslides::
   
   .. admonition:: Example  note

      .. note:: You might want to temporarily set some layer transparency to make adding the ring easier.

When generating slides any ``note`` directives are available as from the presenters console.

.. nextslide:: Warning

The use of ``warning`` should be reserved for really common mistakes that have a history of class disruption.

.. code-block:: rst
   :linenos:
   
   .. warning:: Please be sure to use :command:`Firefox` as we are making use of its ability to display JSON and XML output in a readable fashion.

.. ifnotslides::
   
   .. admonition:: Example warning

      .. warning:: Please be sure to use :command:`Firefox` as we are making use of its ability to display JSON and XML output in a readable fashion.

.. nextslide:: Admonition

Special Effects
===============

.. notslides:: We use a number of directives together to follow our writing guidelines. This section provides cut and paste examples for use when writing workbooks.

   Reference:

   * :sphinx:`Directives <usage/restructuredtext/basics.html#rst-directives>`
   
Exercises
---------

We use the generic ``admonition`` directive to isolate our exercise into boxes visually.

.. code-block:: rst
   :linenos:
   
   .. rst-class:: break

   .. nextslide:: Comparing WMS Versions
   
   .. admonition:: Explore difference between CRS:84 and EPSG:4326

      What is the difference between the ``CRS:84`` and ``EPSG:4326``
      spatial reference systems?
      
      .. ifnotslides::
      
         .. include:: explore_crs84.txt
   
   .. admonition:: Challenge WMS GetMap use
      
      Do you expect ``CRS:84`` to work with a WMS 1.0.0 GetMap Request?
      
      .. ifnotslides::
         
         * For background compare OGC WMS specification with the results produced by :command:`GeoServer`.

.. rst-class:: break

.. nextslide:: Comparing WMS Versions

.. ifslides::

   .. admonition:: Explore difference between CRS:84 and EPSG:4326

      What is the difference between the ``CRS:84`` and ``EPSG:4326``
      spatial reference systems?
  
   .. admonition:: Challenge WMS GetMap use
  
      Do you expect ``CRS:84`` to work with a WMS 1.0.0 GetMap Request?

.. ifnotslides::

   .. admonition:: Example use of admonition for exercises

      .. admonition:: Explore difference between CRS:84 and EPSG:4326

         What is the difference between the ``CRS:84`` and ``EPSG:4326``
         spatial reference systems?
      
         #. Review carefully the WMS 1.3.0 GetCapabiities document which lists both spatial reference systems.
         #. Download the WMS 1.3.0 specification from the OGC website for the definition of ``CRS:84``
         #. You may wish to compare the generated layer bounds for both ``CRS:84`` and ``EPSG:4326``.
      
      .. admonition:: Challenge WMS GetMap use
      
         Do you expect ``CRS:84`` to work with a WMS 1.0.0 GetMap Request?
         
         * For background compare OGC WMS specification with the results produced by :command:`GeoServer`.

Instructor notes
----------------

We use the ``only`` directive, combined with our ant :file:`build.xml` script, to provide an instructor specific build of the workbooks.

To provide notes that only an instructor will see (such as an answer to an Explore section):

.. code-block:: rst
   :linenos:
   
   .. admonition:: Explore

      What is the difference between the ``CRS:84`` and ``EPSG:4326``?

      .. only:: instructor

         .. admonition:: Instructor Notes

            The difference is the strict definition of axis order.

.. ifnotslides::

   Build with ``ant workbook`` example output:

   .. admonition:: Example workbook build
   
      .. admonition:: Explore

         What is the difference between the ``CRS:84`` and ``EPSG:4326``?

   Build with ``ant instructor`` example output:

   .. admonition:: Example instructor build including instructor note
   
      .. admonition:: Explore

         What is the difference between the ``CRS:84`` and ``EPSG:4326``?

         .. only:: instructor

            .. admonition:: Instructor Notes

               The difference is the strict definition of axis order.

Break slides
------------

The `rst-class` directive assigns a class to the next html element generated.

.. nextslide::

We use the `rst-class` to mark some slides a `break` where instructor lets the class work:

.. code-block:: rst
   :linenos:
   
   .. rst-class:: break

   .. nextslide:: Comparing WMS Versions
   
   .. admonition:: Exercise WMS GetMap

      Use WMS `GetMap` parameters to control styling:
      
      .. ifnotslides::
      
         .. include:: wms_getmap_exercise.txt

.. nextslide::

This is also used to apply `break` class to headings:

.. code-block:: rst
   :linenos:
   
   .. rst-class:: break
   
   Tomcat Performance Discussion
   -----------------------------
   
   Discuss performance expectations:
   
   * Startup time
   * Response 
   * Thoughput

Keeping slides simple
---------------------

Our workbooks use `hieroglyph` for slide generation.

We use the `ifnotslides` directive to hide large blocks and reference links from the generated slides.

.. code-block:: rst
   :linenos:
   
   .. notslides:: 

      Reference:

      * :sphinx:`Directives <usage/restructuredtext/basics.html#rst-directives>`

.. ifnotslides::

   .. admonition:: Example ifnotslides directive
   
      Reference:

      * :sphinx:`Directives <usage/restructuredtext/basics.html#rst-directives>`   
   
.. ifnotslides::

   Reference:

   * `hieroglyph <http://docs.hieroglyph.io/>`__


Include download.txt (recommended)
----------------------------------

The `include` directive can be used to inline a file, or a few lines of a file.

We use this capability to make download links easier to manage in workbooks and setup instructions (in cases where the version number changes frequently).

.. code-block:: rst
   :linenos:
   
   #. Download the virtual machine:

     .. include:: download.txt
        :start-line: 2
        :end-line: 3

.. ifnotslides::

   .. admonition:: Example include download.txt
   
      #. Download the virtual machine:
  
        .. include:: files/download.txt
           :start-line: 2
           :end-line: 3

.. nextslide:: 

Directory structure:

.. list-table::
   :widths: 30 70

   * - :file:`vm/download.txt`
     - Download links isolated as separate file
   * - :file:`vm/index.rst`
     - 
   
Images and Graphics
===================

.. ifnotslides::
   
   Add images to your documentation when possible.  Images, such as screenshots, are a very helpful way of making documentation understandable and provide an entry point for visual instruction.

   When making screenshots, try to crop out unnecessary content (browser window, desktop, etc).  Avoid scaling the images, as the sphinx theme automatically resizes large images.

Images
------

For images, use the ``figure`` directive and add a caption. Place the image files in an :file:`img` directory:

.. code-block:: rst
   :linenos:
   
   .. figure: img/boundless_desktop_install.png

      Boundless Desktop Setup installing

.. ifnotslides::

   .. admonition:: Example image
   
      .. figure:: img/boundless_desktop_install.png

         Boundless Desktop Setup installing

When given the option 8-bit PNG are preferred (text remains readable and file size is smaller). There are some tools (https://pngquant.org)

.. nextslide::
   :increment:

Directory structure:

.. list-table::
   :widths: 30 70

   * - :file:`src/section/index.rst`
     - section being written
   * - :file:`src/section/img/`
     - images and screen shots used in section/index.rst above
   * - :file:`src/index.rst`
     - start of module
   * - :file:`src/config.py`
     - 

Icons
-----

It is technically possible to show icons such as toolbar buttons inline, using  substitutions.

.. code-block:: rst
   :linenos:

   #. From the :menuselection:`toolbar` select :guilabel:`Save` ( |save| ) to make the change and remain in edit mode.

   .. |save| image:: img/save.png
             :class: inline

.. ifnotslides::

   .. admonition:: Example icon

      4. From the :menuselection:`toolbar` select :guilabel:`Save` ( |save| ) to make the change and remain in edit mode.

      .. |save| image:: img/save.png
                :class: inline

.. nextslide:: Icon Tooltip

You may prefer to reference toolbar buttons by name (as provided by Icon tooltip):

.. code-block:: rst
   :linenos:

   #. From the :menuselection:`toolbar` select :guilabel:`Save` to make the change and remain in edit mode.

.. ifnotslides::

   .. admonition:: Example
      
      4. From the :menuselection:`toolbar` select :guilabel:`Save` to make the change and remain in edit mode.

Screenshots
-----------

Screenshots are essential to the success of step by step exercises, a consistent visual appearance is important to their success.

.. warning::
   
   Do you run linux? If so fire up a virtual machine to take screen snaps. No excuses.

.. warning::
   
   Do you run macOS? If so fire up a virtual machine to take screen snaps. No excuses.

.. nextslide::
   :increment:
   
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
* Use width percentage as required for consistent look for navigation menu.

  .. code-block:: rst
     :linenos:
  
     .. figure: img/start-tomcat.png
        :width: 30%
        
        Launch Tomcat from the Start Menu

.. nextslide:: Browser Screen Snaps
   :increment:

* This course is written and tested with :command:`Firefox`, so use :command:Firefox for screen snaps
* When making screen snaps of :command:`GeoServer` or any web app determine the minimum width before horizontal scroll bars appear.
* Take a crop of the page, rather than include the entire browser window.
* Crop to the full width of the form ignoring navigation menu (rather than have the size change from step to step).

.. nextslide::
   :increment: 

.. tip:: On MacOS use :command:`System Preferences` navigate to :menuselection:`Keyboard --> Shortcuts` and ensure :guilabel:`Copy a picture of section area to the clipboard` is mapped to :kbd:`shift-command-4`. You can then paste the clipboard into the :command:`Preview` application and save ther result as png.

.. tip:: On Windows you can use the :command:`Snip` tool to capture cropped images, or use :kbd:`Alt-Shift-F12` to copy the current window to the clipboard.

There are several tools, example https://pngquant.org, for bulk converting images to :file:`PNG`.

Figures
-------

For figures, or diagrams we need to draw by hand, use the ``figure`` directive and add a caption. Place the image files in the top-level ``/figure`` directory:

.. code-block:: rst
   :linenos:

   .. figure:: /figure/component_diagram.*

      Boundless Server component architecture

.. ifnotslides::

   .. admonition:: Example figure
   
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

.. nextslide:: Interaction illustrations
   :increment:

Component interaction is often illustrated with block diagrams, showing the internal components involved.

.. figure:: /figure/config_admin.*

   Interaction diagrams

.. nextslide:: Exercise illustrations 

When illustrating configuration make sure diagram exactly matches the exercise.

.. figure:: /figure/config_data.*

   Configuration Illustration

.. nextslide:: Boundless Branding Icons

Follow boundless branding for icons such as GeoServer and QGIS when available.

.. figure:: /figure/components.*

   Boundless Style Guide: Components

Use of opensource logos are fine when they do not conflict with company branding (such as pgAdmin or SQL Shell above).

.. nextslide:: Boundless Branding Fonts

Follow boundless styleguide for use of fonts.

.. figure:: /figure/fonts.*

   Boundless Style Guide: Fonts

We may need to update our sphinx theme over time.

.. nextslide:: Boundless Style Guide Colors

Boundless provides a range of colors for use:

.. figure:: /figure/swatch.*

   Boundless Style Guide: Color

Our illustrations use a slightly muted version of the company color palette.

Code Examples
=============

.. ifslides::
   
   Reduce frustration with line numbers and directly including live code examples.

.. ifnotslides:: 
   
   Describing edits to configuration files and code examples represent the largest and most frustrating opportunity for error. We have standardized on using line numbers for all code examples, and using using ``literal-include`` to directly include live code examples whenever possible.

Code Block
----------

Use ``code-block``, specifying language for syntax highlighting, and turning on ``linenos`` :

.. code-block:: rst
   :linenos:
   
   #. Define the initial point style:

      .. code-block:: yaml
         :linenos:
            
           - point:
               symbols:
               - mark:
                   shape: star

.. ifnotslides::

   .. admonition:: Example code-block

      4. Define the initial point style:
 
         .. code-block:: yaml
            :linenos:
            
              - point:
                  symbols:
                  - mark:
                      shape: star

.. nextslide::
   :increment:

When adding or editing use emphasis to indicate changed lines:

.. code-block:: rst
   :linenos:
   
   #. Change the ``shape`` to :kbd:`triangle`:

      .. code-block:: yaml
         :linenos:
         :emphasize-lines: 4

           - point:
               symbols:
               - mark:
                   shape: triangle

.. ifnotslides::

   .. admonition:: Example code-block with emphasis

      5. Change the ``shape`` to :kbd:`triangle`:

         .. code-block:: yaml
            :linenos:
            :emphasize-lines: 4

              - point:
                  symbols:
                  - mark:
                      shape: triangle

.. nextslide::

Command line exampels should be formatted appropriate (`bat` or `bash`) and do not require line numbers:

.. code-block:: rst
   :linenos:
   
   #. Check the contents of the directory:
   
      .. code-block:: bash
         
         $ ls -la
      
      ::
      
        total 2800
        -rw-r--r--   1 boundless  staff      429 14 Nov 16:14 README.md

.. ifnotslides::

   .. admonition:: Example bash output

      #. Check the contents of the directory:
   
         .. code-block:: bash
         
            $ ls -la
      
         ::
      
           total 2800
           -rw-r--r--   1 boundless  staff      429 14 Nov 16:14 README.md


   
Literal Includes
----------------

Use ``literalinclude`` and ``download`` directives, to avoid possibility of error with config, style and data files!

.. code-block:: rst
   :linenos:

   #. Contents of :download:`geoserver.xml <files/geoserver.xml>`:

      .. literalinclude:: files/geoserver.xml
         :language: xml
         :linenos:

.. ifnotslides::

   .. admonition:: Example literal include

      2. Contents of :download:`geoserver.xml <files/geoserver.xml>`:

         .. literalinclude:: files/geoserver.xml
            :language: xml
            :linenos:

.. nextslide::
   :increment:

Combined with line highlighting to help direct exercises where configuration files are changed.

.. code-block:: rst
   :linenos:

   7. Change to :file:`svg` icon as show below:

      .. literalinclude:: files/airports.ysld
         :language: yaml
         :linenos:
         :emphasize-lines: 4-5

.. ifnotslides::

   .. admonition:: Example literal include with emphasis

      7. Change to :file:`svg` icon as show below:

         .. literalinclude:: files/airports.ysld
            :language: yaml
            :linenos:
            :emphasize-lines: 4-5

.. nextslide::
   :increment:

If you want to include only part of the file use ``start-after`` and ``end-before`` (rather than line numbers). Your can also use ``prepend`` and ``append`` to keep structured text like xml or json valid. Note the use of ``lineno-start`` to keep line numbering consistent.

.. code-block:: rst
   :linenos:
   
   #. SLD lists symbology graphics in order of preference, first ``image/svg`` then ``mage/png``:

      .. literalinclude:: files/airports1.sld
         :language: xml
         :lineno-start: 33
         :start-after: <PointSymbolizer>
         :end-before: <Mark>

.. ifnotslides::
   
   .. admonition:: Example literal include of snippet

      8. SLD lists symbology graphics in order of preference, first ``image/svg`` then ``mage/png``:
      
         .. literalinclude:: files/airports1.sld
            :language: xml
            :lineno-start: 16
            :start-after: <PointSymbolizer>
            :end-before: <Mark>

.. nextslide::
   :increment:
   
It is good practice to provide the final document as a download and reference:

.. code-block:: rst
   :linenos:
   
   #. The completed :download:`airports.sld <files/airports1.sld>`:

      .. literalinclude:: files/airports1.sld
         :language: xml

.. ifnotslides::
   
   .. admonition:: Example literal include of snippet

      9. The completed :download:`airports.sld <files/airports1.sld>`:

         .. literalinclude:: files/airports1.sld
            :language: xml

.. ifnotslides::

   Reference:

   * :sphinx:`Includes <markup/code.html#includes>`
