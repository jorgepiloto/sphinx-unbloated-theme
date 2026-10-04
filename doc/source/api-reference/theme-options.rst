.. _api-theme-options:

Theme options
#############

The following options can be passed via ``html_theme_options`` in ``conf.py``.
They are declared in
``src/sphinx_unbloated_theme/theme/sphinx_unbloated_theme/theme.toml``.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Option
     - Default
     - Description
   * - ``site_description``
     - ``""``
     - Short description shown beneath the project title in the page header.
   * - ``footer_text``
     - ``""``
     - HTML string rendered inside ``<footer>``. When empty the theme falls
       back to the Sphinx copyright notice.
