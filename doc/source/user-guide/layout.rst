.. _layout:

Layout
######

The theme renders every page with four structural HTML elements that mirror
the layout used on `jorgemartinez.space <https://jorgemartinez.space>`_:

``<header>``
    Black background, white text. Displays the project name (``project`` from
    ``conf.py``) and, optionally, the ``site_description`` theme option.

``<nav>``
    A row of monospace buttons linking to the parent pages and the previous /
    next document. Buttons invert to white-on-black on hover or when active.

``<main>``
    The full-width content area. No sidebar is rendered; the document takes all
    available horizontal space (up to 800 px).

``<footer>``
    Black background, white text. Renders the value of the ``footer_text``
    theme option, or a default copyright + Sphinx notice.

No sidebar
----------

The ``basic`` theme's sidebar is suppressed entirely. If you need a table of
contents you can add it inline in your ``.rst`` files using the ``.. contents::``
directive:

.. code-block:: rst

   .. contents:: On this page
      :local:
      :depth: 2
