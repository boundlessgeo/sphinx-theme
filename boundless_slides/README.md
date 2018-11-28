# Boundless Slides Theme

Slide theme extending basic for corporate look and feel.

Theme options are based on {slides} theme:

* custom_css
* custom_js
* logo: choose between boundless_learning, boundless_server, boundless_desktop

## Use

To add a section break using autoslides:

```
Section Title
-------------

Section subtitle
```

To add a section using slide directive:

```
.. slide:: Section Title
   :class: section
   :level: 2
   
   Section subtitle 
```

## Design

* fonts:
  
  * headings: Proxa Nova is bundled with theme, with Lato as fallback
  * text: 'Lato', sans-serif
  * code: "Source Code Pro", Droid, monospace
  
* sections:
  
  * H1: Title relies on cover.jpg background, with white text
  * H2: Section break (heading 2) relies on solid color background, with white text
  * H3: Content
  * H4: Content

* footers:
  
  * footer: company logo right aligned, may be replaced with product logo as required?
  * numbering: right aligned
  
* figure:
  
  Figure captions are right aligned under diagram.

* image:
  
  Images are included, adjust scale for images that may be larger then slide.

## Implementation Notes

theme:

* theme.conf: extends ``slides`` theme
* layout.html: inherited from slides
* slide.html: inherited from slides
* console.html: inherited from slides
* static/boundless_slide.css
* static/cover.jpg

css:

* boundless_slide.css: imports ``slides.css`` from ``basic``.

## slide.html

slide.html variable reference:

* id
* title
* level
* content
* content_classes
* slide_classes
* classes
* slide_number
* config
* config.master_doc
* config.html_short_title

slide css styling guide:

* slides contained in article element
* each slide has an ``id`` matching the permalink ID
* heading level is added as a class: ``level-2``
* slides may be styled using a theme, or custom CSS
* enable slide numbers or slide footer with configuration setting

notes on use of classes:

* Could not get slide class ``title-image`` to work as documented
* Add ``.. rst-class:: custom`` to provide a ``rst-custom`` class for use by CSS

Example:

```
<h{{ level }}>{{ title }}</h{{ level }}>
```

## layout.html

layout.html variable reference:

* pagename
* master_doc

Example:

```
<a href="{{ pathto('index') }}#2">{{ title|e }}</a>
```

## Reference

* [Hieroglyph Creating Themes](http://docs.hieroglyph.io/en/latest/theme-creation.html) [source](https://github.com/nyergler/hieroglyph/blob/master/docs/theme-creation.rst)
* [Hieroglyph Styling](http://docs.hieroglyph.io/en/latest/styling.html) [source](https://github.com/nyergler/hieroglyph/blob/master/docs/styling.rst)
* [Sphinx Templating](https://www.sphinx-doc.org/en/master/templating.html)
