"""Sphinx Unbloated Theme, an HTML theme for Sphinx."""

from pathlib import Path


__version__ = "0.1.dev0"
"""Current version of the Sphinx Unbloated Theme."""

THEME_PATH = Path(__file__).parent / "theme" / "sphinx_unbloated_theme"


def _build_subnav(app, pagename, docnames):
    """Build navigation links relative to the current page.

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application for the documentation build.
    pagename : str
        Document name of the current page.
    docnames : sequence of str
        Document names to include in the navigation.

    Returns
    -------
    list of tuple
        Links as ``(label, url, is_active)`` tuples. Documents without a
        title are skipped.
    """
    links = []
    for doc in docnames:
        title_node = app.env.titles.get(doc)
        if title_node is None:
            continue
        links.append((
            title_node.astext(),
            app.builder.get_relative_uri(pagename, doc),
            pagename == doc or pagename.startswith(doc + "/"),
        ))
    return links


def _add_nav_context(app, pagename, templatename, context, doctree):
    """Add navigation links to the page template context.

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application for the documentation build.
    pagename : str
        Document name of the current page.
    templatename : str
        Page template name. Unused, but required by the event signature.
    context : dict
        Template context to update with navigation links.
    doctree : docutils.nodes.document or None
        Page document tree. Unused, but required by the event signature.

    Notes
    -----
    ``nav_links`` contains Home and the top-level sections.
    ``breadcrumb_levels`` contains the top-level section's title, URL, and
    child links, rendered before the page body as ``{title, url, subnav}``.
    ``subnav_links`` contains the current page's children. JavaScript moves
    these links after the page's first ``<h1>``.
    """
    master = app.config.master_doc
    toctree_includes = getattr(app.env, "toctree_includes", {})
    top_level_docs = toctree_includes.get(master, [])
    page_section = pagename.split("/")[0]

    # Keep the same navigation links on every page.
    nav_links = [("Home", app.builder.get_relative_uri(pagename, master), pagename == master)]
    for doc in top_level_docs:
        title_node = app.env.titles.get(doc)
        if title_node is None:
            continue
        is_active = (doc.split("/")[0] == page_section) and (pagename != master)
        nav_links.append((
            title_node.astext(),
            app.builder.get_relative_uri(pagename, doc),
            is_active,
        ))
    context["nav_links"] = nav_links

    breadcrumb_levels = []   # Rendered before the page body.
    subnav_links = []        # Moved after the first h1 by JavaScript.

    if pagename == master:
        context["breadcrumb_levels"] = breadcrumb_levels
        context["subnav_links"] = subnav_links
        return

    # Match the page's first path segment to a top-level section.
    section_doc = next(
        (doc for doc in top_level_docs if doc.split("/")[0] == page_section),
        None,
    )
    if section_doc is None:
        context["breadcrumb_levels"] = breadcrumb_levels
        context["subnav_links"] = subnav_links
        return

    section_children = toctree_includes.get(section_doc, [])

    if pagename == section_doc:
        # On a section page, show its children after the title.
        subnav_links = _build_subnav(app, pagename, section_children)
    else:
        # On a descendant page, show the section and its children above the body.
        section_title_node = app.env.titles.get(section_doc)
        breadcrumb_levels.append({
            "title": section_title_node.astext() if section_title_node else section_doc,
            "url": app.builder.get_relative_uri(pagename, section_doc),
            "subnav": _build_subnav(app, pagename, section_children),
        })

        # Show the current page's children after its title, if any.
        current_children = toctree_includes.get(pagename, [])
        subnav_links = _build_subnav(app, pagename, current_children)

    context["breadcrumb_levels"] = breadcrumb_levels
    context["subnav_links"] = subnav_links


def setup(app):
    """Register the theme and navigation hook with Sphinx.

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application for the documentation build.

    Returns
    -------
    dict
        Extension metadata with the version and parallel build safety flags.
    """
    app.add_html_theme("sphinx_unbloated_theme", THEME_PATH)
    app.connect("html-page-context", _add_nav_context)
    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def add_two_numbers(a: int, b: int) -> int:
    """Add two numbers.

    Parameters
    ----------
    a : int
        First number.
    b : int
        Second number.

    Returns
    -------
    int
        Sum of the two numbers.
    """
    return a + b
