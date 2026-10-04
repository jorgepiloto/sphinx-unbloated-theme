.. _kitchen-sink:

Kitchen sink
############

This page exercises every reStructuredText element supported by the theme so
you can verify at a glance that typography, spacing, and colours look correct.

Typography
----------

Normal paragraph text set in the theme's monospace typeface. **Bold text**,
*italic text*, ``inline code``, and `hyperlinks <https://www.sphinx-doc.org/>`_
all appear here.

Headings
--------

Heading level 2 (h2)
~~~~~~~~~~~~~~~~~~~~~

Heading level 3 (h3)
^^^^^^^^^^^^^^^^^^^^^

Heading level 4 (h4)
"""""""""""""""""""""

Lists
-----

Unordered
~~~~~~~~~

- First item in an unordered list.
- Second item, with a bit more text to check line wrapping at narrower
  viewport widths.
- Third item.

Ordered
~~~~~~~

1. First step.
2. Second step.
3. Third step.

Definition list
~~~~~~~~~~~~~~~

term
    Definition of the term.

another term
    Definition of another term, possibly spanning multiple lines to verify
    that continuation indentation is rendered correctly.

Code
----

Inline code: ``print("Hello, world!")``.

Code block:

.. code-block:: python

   def greet(name: str) -> str:
       """Return a friendly greeting."""
       return f"Hello, {name}!"

   print(greet("world"))

Admonitions
-----------

.. note::

   This is a **note** admonition. Use it for supplementary information that
   the reader should be aware of.

.. warning::

   This is a **warning** admonition. Use it to flag potentially dangerous or
   irreversible actions.

.. tip::

   This is a **tip** admonition. Use it to share best-practice advice.

Tables
------

.. list-table:: Sample data table
   :header-rows: 1
   :widths: 20 40 40

   * - Column A
     - Column B
     - Column C
   * - Row 1
     - Some value
     - Another value
   * - Row 2
     - Some value
     - Another value

Blockquote
----------

   A blockquote is an indented block of text used to highlight a passage or
   cited material. It should stand out visually from surrounding paragraphs.

Mathematics
-----------

Inline math: the area of a circle is :math:`A = \pi r^2`.

Display math — the quadratic formula:

.. math::

   x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}

A multi-line equation — Euler's identity and the Gaussian integral:

.. math::

   e^{i\pi} + 1 &= 0 \\
   \int_{-\infty}^{\infty} e^{-x^2}\, dx &= \sqrt{\pi}

Images
------

.. figure:: /_static/logo.png
   :align: center
   :alt: Sphinx Unbloated Theme logo

   A figure caption appears below the image in italics.
