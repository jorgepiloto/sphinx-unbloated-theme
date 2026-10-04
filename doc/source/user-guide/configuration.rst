.. _configuration:

Configuration
#############

Set the theme options in ``html_theme_options`` in your ``conf.py``.

Available options
-----------------

``site_description``
    A short description displayed below the project title in the site header.
    Defaults to an empty string (no description shown).

    .. code-block:: python

       html_theme_options = {
           "site_description": "Comprehensive documentation for MyProject.",
       }

``footer_text``
    Custom HTML string rendered inside the ``<footer>`` element.
    Defaults to the Sphinx copyright string plus a "Built with Sphinx" notice.

    .. code-block:: python

       html_theme_options = {
           "footer_text": "&copy; 2026 My Name.",
       }

``github_url``
    URL of the project's GitHub repository. When set, a GitHub icon link is
    shown in the header next to the other social icons.
    Defaults to an empty string (icon not shown).

    .. code-block:: python

       html_theme_options = {
           "github_url": "https://github.com/my-org/my-project",
       }

``linkedin_url``
    URL of a LinkedIn profile or company page. When set, a LinkedIn icon link
    is shown in the header.
    Defaults to an empty string (icon not shown).

    .. code-block:: python

       html_theme_options = {
           "linkedin_url": "https://www.linkedin.com/in/my-profile/",
       }

``youtube_url``
    URL of a YouTube channel or playlist. When set, a YouTube icon link is
    shown in the header.
    Defaults to an empty string (icon not shown).

    .. code-block:: python

       html_theme_options = {
           "youtube_url": "https://www.youtube.com/@my-channel",
       }

``rss_url``
    URL of an RSS feed. When set, an RSS icon link is shown in the header.
    Defaults to an empty string (icon not shown).

    .. code-block:: python

       html_theme_options = {
           "rss_url": "https://my-site.com/feed.xml",
       }

``sponsor_url``
    URL of a sponsorship page (e.g. GitHub Sponsors, Open Collective).
    When set, a heart-shield icon link is shown in the header.
    Defaults to an empty string (icon not shown).

    .. code-block:: python

       html_theme_options = {
           "sponsor_url": "https://github.com/sponsors/my-org",
       }

``versions_url``
    URL of a JSON file that lists the available documentation versions.
    When set, a version-switcher drop-down is rendered in the header.
    The JSON must be an array of objects with ``name`` and ``url`` keys.
    Defaults to an empty string (drop-down not shown).

    .. code-block:: python

       html_theme_options = {
           "versions_url": "https://my-site.com/versions.json",
       }

    Expected JSON format:

    .. code-block:: json

       [
         {"name": "v2.0 (stable)", "url": "https://my-site.com/version/stable/"},
         {"name": "v1.0",          "url": "https://my-site.com/version/v1.0/"}
       ]

Full example
------------

.. code-block:: python

   html_theme = "sphinx_unbloated_theme"

   html_theme_options = {
       "site_description": "My project documentation.",
       "footer_text": "&copy; 2026 My Name. Built with the Sphinx Unbloated Theme.",
       "github_url": "https://github.com/my-org/my-project",
       "linkedin_url": "https://www.linkedin.com/in/my-profile/",
       "youtube_url": "https://www.youtube.com/@my-channel",
       "rss_url": "https://my-site.com/feed.xml",
       "sponsor_url": "https://github.com/sponsors/my-org",
       "versions_url": "https://my-site.com/versions.json",
   }

AutoAPI Templates
-----------------

The theme includes templates for `Sphinx AutoAPI
<https://sphinx-autoapi.readthedocs.io/en/latest/>`_. They group API summaries
into tabs and include descriptions and member details. Class summaries group
methods, properties, and attributes and include an import example.

Install ``sphinx-autoapi`` and ``numpydoc``, then select the templates in
``conf.py``:

.. code-block:: python

   from sphinx_unbloated_theme import get_autoapi_templates_dir

   extensions = ["autoapi.extension", "numpydoc"]
   html_theme = "sphinx_unbloated_theme"
   autoapi_dirs = ["../../src/my_project"]
   autoapi_template_dir = get_autoapi_templates_dir()
   numpydoc_show_class_members = False

Set ``autoapi_dirs`` to your package directory, relative to the documentation
source directory. To give each class its own page, set
``autoapi_own_page_level = "class"``.

Use the arrow keys, Home, and End to switch summary tabs. All summary groups
remain visible when JavaScript is disabled.

To use your own templates, set ``autoapi_template_dir`` to your template
directory instead.
