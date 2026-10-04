.. _layout:

Layout
######

The theme renders every page with four structural HTML elements that mirror
the layout used on `jorgemartinez.space <https://jorgemartinez.space>`_:

``<header>``
    Black background, white text. Displays the project name (``project`` from
    ``conf.py``) and, optionally, the ``site_description`` theme option.

``<nav>``
    Monospace buttons link to the top-level sections and the current section's
    child pages. They show white text on black when hovered or active.

``<main>``
    The full-width content area. No sidebar is rendered; the document takes all
    available horizontal space (up to 800 px).

``<footer>``
    Black background, white text. Renders the value of the ``footer_text``
    theme option, or a default copyright + Sphinx notice.

Page Navigation
---------------

A back button below the content links to the parent page. Top-level pages link
back to Home. The button has a left arrow, a black border, and a gray shadow.
Hovering or focusing it with the keyboard switches to white text on black.
On short pages, the content area expands to keep the button just above the
footer.

No Sidebar
----------

The ``basic`` theme's sidebar is suppressed entirely. If you need a table of
contents you can add it inline in your ``.rst`` files using the ``.. contents::``
directive:

.. code-block:: rst

   .. contents:: On this page
      :local:
      :depth: 2
