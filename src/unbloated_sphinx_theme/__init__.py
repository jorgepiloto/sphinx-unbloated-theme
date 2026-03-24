"""Unbloated Sphinx Theme — a minimal, clean Sphinx theme."""

from pathlib import Path


__version__ = "0.1.dev0"
"""Current version of the Unbloated Sphinx Theme."""

THEME_PATH = Path(__file__).parent / "theme" / "unbloated_sphinx_theme"


def _build_subnav(app, pagename, docnames):
    """Return a list of (label, url, is_active) for *docnames* relative to *pagename*."""
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
    """Inject navigation context into every page's template.

    ``nav_links``         — top-level section buttons (always present).
    ``breadcrumb_levels`` — list of ancestor levels rendered *before* the page
                            body, each as ``{title, url, subnav}``.
    ``subnav_links``      — children of the current page; JS moves them
                            immediately after the page <h1>.
    """
    master = app.config.master_doc
    toctree_includes = getattr(app.env, "toctree_includes", {})
    top_level_docs = toctree_includes.get(master, [])
    page_section = pagename.split("/")[0]

    # ── Main nav (always the same) ────────────────────────────────────────────
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

    # ── Breadcrumb chain + current-page subnav ───────────────────────────────
    breadcrumb_levels = []   # ancestor levels rendered before the body
    subnav_links = []        # current page's own children (JS-placed after h1)

    if pagename == master:
        context["breadcrumb_levels"] = breadcrumb_levels
        context["subnav_links"] = subnav_links
        return

    # Find the top-level section that owns this page
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
        # We ARE the section page — its children become the JS-placed subnav.
        subnav_links = _build_subnav(app, pagename, section_children)
    else:
        # We are a descendant — build the breadcrumb chain upward.
        # Level 1: top-level section → its children (with current branch active)
        section_title_node = app.env.titles.get(section_doc)
        breadcrumb_levels.append({
            "title": section_title_node.astext() if section_title_node else section_doc,
            "url": app.builder.get_relative_uri(pagename, section_doc),
            "subnav": _build_subnav(app, pagename, section_children),
        })

        # Level 2+: walk deeper if the current page itself has children
        # (supports arbitrary depth for future use)
        current_children = toctree_includes.get(pagename, [])
        subnav_links = _build_subnav(app, pagename, current_children)

    context["breadcrumb_levels"] = breadcrumb_levels
    context["subnav_links"] = subnav_links


def setup(app):
    """Register the theme with Sphinx."""
    app.add_html_theme("unbloated_sphinx_theme", THEME_PATH)
    app.connect("html-page-context", _add_nav_context)
    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
