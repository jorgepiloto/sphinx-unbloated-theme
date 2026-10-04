"""Sphinx documentation configuration file."""

from datetime import datetime
from pathlib import Path
import logging
import os
import pathlib
import shutil
import subprocess
import sys

# Make the package importable for autodoc without a prior install step
import sphinx
import sphinx.application
from sphinx.util.display import status_iterator

sys.path.insert(0, str(Path(__file__).parents[2] / "src"))

from sphinx_unbloated_theme import __version__

# Project information
project = "Sphinx Unbloated Theme"
copyright = f"{datetime.now().year}, Jorge Martinez"
author = "Jorge Martinez"
release = version = __version__
cname = os.getenv("DOCUMENTATION_CNAME", "localhost")

# Sphinx extensions
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "nbsphinx",
    "myst_parser",
]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

# autodoc settings
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
}

# HTML configuration
html_theme = "sphinx_unbloated_theme"
html_title = "Sphinx Unbloated Theme"
html_short_title = "Sphinx Unbloated Theme"
html_baseurl = "https://jorgemartinez.space/projects/sphinx-unbloated-theme/version/stable/"

html_theme_options = {
    "site_description": "A minimal, clean Sphinx theme with a monospace aesthetic.",
    "footer_text": f"&copy; {datetime.now().year} Jorge Martinez. Built with the Sphinx Unbloated Theme.",
    "github_url": "https://github.com/jorgemartinez",
    "versions_url": f"https://{cname}/versions.json",
}

# Source settings
master_doc = "index"
exclude_patterns = ["_build", "conf.py"]

# Generate a 404 page from the theme template
html_additional_pages = {"404": "404.html"}

# Examples to exclude from the gallery
exclude_examples = []

# The suffix(es) of source filenames
source_suffix = {
    ".rst": "restructuredtext",
    ".mystnb": "jupyter_notebook",
    ".md": "markdown",
    ".py": "jupyter_notebook",
}

# Configure examples
nbsphinx_execute = "always"
nbsphinx_custom_formats = {
    ".mystnb": ["jupytext.reads", {"fmt": "mystnb"}],
    ".py": ["jupytext.reads", {"fmt": ""}],
}
nbsphinx_prompt_width = ""

# Download buttons shown at the top of every notebook example page
_cname = os.environ.get("CNAME", "localhost")
_cname_pref = f"https://{_cname}/version/{version}"

nbsphinx_prolog = """
.. raw:: html

   <div class="download-buttons" id="download-buttons">
     <a href="{cname_pref}/{{{{ env.docname }}}}.py">
       <button><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M439.8 200.5c-7.7-30.9-22.3-54.2-53.4-54.2h-40.1v47.4c0 36.8-31.2 67.8-66.8 67.8H172.7c-29.2 0-53.4 25-53.4 54.3v101.8c0 29 25.2 46 53.4 54.3 33.8 9.9 66.3 11.7 106.8 0 26.9-7.8 53.4-23.5 53.4-54.3v-40.7H226.2v-13.6h160.2c31.1 0 42.6-21.7 53.4-54.2 11.2-33.5 10.7-65.7 0-108.6zM286.2 404c11.1 0 20.1 9.1 20.1 20.3 0 11.3-9 20.4-20.1 20.4-11 0-20.1-9.2-20.1-20.4.1-11.3 9.1-20.3 20.1-20.3zM167.8 248.1h106.8c29.7 0 53.4-24.5 53.4-54.3V91.9c0-29-24.4-50.7-53.4-55.6-35.8-5.9-74.7-5.6-106.8.1-45.2 8-53.4 24.7-53.4 55.6v40.7h106.9v13.6h-147c-31.1 0-58.3 18.7-66.8 54.2-9.8 40.7-10.2 66.1 0 108.6 7.6 31.6 25.7 54.2 56.8 54.2H101v-48.8c0-35.3 30.5-66.4 66.8-66.4zm-6.7-142.6c-11.1 0-20.1-9.1-20.1-20.3.1-11.3 9-20.4 20.1-20.4 11 0 20.1 9.2 20.1 20.4s-9 20.3-20.1 20.3z"/></svg> Download as Python script</button>
     </a>
     <a href="{cname_pref}/{{{{ env.docname }}}}.ipynb">
       <button><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M96 0C43 0 0 43 0 96V416c0 53 43 96 96 96H384h32c17.7 0 32-14.3 32-32s-14.3-32-32-32V384c17.7 0 32-14.3 32-32V32c0-17.7-14.3-32-32-32H384 96zm0 384H352v64H96c-17.7 0-32-14.3-32-32s14.3-32 32-32zm32-240c0-8.8 7.2-16 16-16H336c8.8 0 16 7.2 16 16s-7.2 16-16 16H144c-8.8 0-16-7.2-16-16zm16 48H336c8.8 0 16 7.2 16 16s-7.2 16-16 16H144c-8.8 0-16-7.2-16-16s7.2-16 16-16z"/></svg> Download as Jupyter notebook</button>
     </a>
     <a href="{cname_pref}/{{{{ env.docname }}}}.pdf">
       <button><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M0 64C0 28.7 28.7 0 64 0H224V128c0 17.7 14.3 32 32 32H384V304H176c-35.3 0-64 28.7-64 64V512H64c-35.3 0-64-28.7-64-64V64zm384 64H256V0L384 128zM176 352h32c30.9 0 56 25.1 56 56s-25.1 56-56 56H192v32c0 8.8-7.2 16-16 16s-16-7.2-16-16V368c0-8.8 7.2-16 16-16zm32 80c13.3 0 24-10.7 24-24s-10.7-24-24-24H192v48h16zm96-80h32c26.5 0 48 21.5 48 48v64c0 26.5-21.5 48-48 48H304c-8.8 0-16-7.2-16-16V368c0-8.8 7.2-16 16-16zm32 128c8.8 0 16-7.2 16-16V400c0-8.8-7.2-16-16-16H320v96h16zm80-112c0-8.8 7.2-16 16-16h48c8.8 0 16 7.2 16 16s-7.2 16-16 16H448v32h32c8.8 0 16 7.2 16 16s-7.2 16-16 16H448v48c0 8.8-7.2 16-16 16s-16-7.2-16-16V368z"/></svg> Download as PDF document</button>
     </a>
   </div>
   <script>
     document.addEventListener('DOMContentLoaded', function () {{
       var buttons = document.getElementById('download-buttons');
       var h1 = document.querySelector('main h1');
       if (h1 && buttons) h1.insertAdjacentElement('afterend', buttons);
     }});
   </script>

""".format(cname_pref=_cname_pref)


def copy_examples_to_output_dir(app: sphinx.application.Sphinx, exception: Exception):
    """
    Copy the examples directory to the output directory of the documentation.

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application instance containing the all the doc build configuration.
    exception : Exception
        Exception encountered during the building of the documentation.

    """
    OUTPUT_EXAMPLES = pathlib.Path(app.outdir) / "examples"
    OUTPUT_EXAMPLES.mkdir(parents=True, exist_ok=True)

    EXAMPLES_DIRECTORY = pathlib.Path(app.srcdir).parent.parent / "examples"

    all_examples = list(EXAMPLES_DIRECTORY.glob("*.py"))
    examples = [file for file in all_examples if file.name not in exclude_examples]
    for file in status_iterator(
        examples,
        "Copying example to doc/_build/examples/",
        "green",
        len(examples),
        verbosity=1,
        stringify_func=(lambda x: x.name),
    ):
        destination_file = OUTPUT_EXAMPLES / file.name
        destination_file.write_text(file.read_text(encoding="utf-8"), encoding="utf-8")


def copy_examples_files_to_source_dir(app: sphinx.application.Sphinx, config):
    """
    Copy the examples directory to the source directory of the documentation.

    This hook is connected to the ``config-inited`` event so that the files
    are present before Sphinx enumerates source files (``find_files`` is
    called in ``_post_init_env``, which runs after ``config-inited`` but
    before ``builder-inited``).

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application instance containing the all the doc build configuration.
    config : sphinx.config.Config
        Sphinx configuration object (unused, required by the event signature).

    """
    SOURCE_EXAMPLES = pathlib.Path(app.srcdir) / "examples"
    SOURCE_EXAMPLES.mkdir(parents=True, exist_ok=True)

    EXAMPLES_DIRECTORY = pathlib.Path(app.srcdir).parent.parent / "examples"

    all_examples = list(EXAMPLES_DIRECTORY.glob("*.py"))
    examples = [file for file in all_examples if file.name not in exclude_examples]
    for file in examples:
        destination_file = SOURCE_EXAMPLES / file.name
        destination_file.write_text(file.read_text(encoding="utf-8"), encoding="utf-8")


def remove_examples_from_source_dir(app: sphinx.application.Sphinx, exception: Exception):
    """
    Remove the example files from the documentation source directory.

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application instance containing the all the doc build configuration.
    exception : Exception
        Exception encountered during the building of the documentation.

    """
    EXAMPLES_DIRECTORY = pathlib.Path(app.srcdir) / "examples"
    logger = logging.getLogger(__name__)
    logger.info(f"\nRemoving {EXAMPLES_DIRECTORY} directory...")
    shutil.rmtree(EXAMPLES_DIRECTORY)


def render_examples_as_pdf(app: sphinx.application.Sphinx, exception: Exception):
    """
    Render notebook examples as PDF files using Quarto.

    Quarto needs to be installed in the system to render the PDF files. See
    https://quarto.org/docs/get-started/.

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application instance containing the all the doc build configuration.
    exception : Exception
        Exception encountered during the building of the documentation.

    """
    try:
        RENDERED_EXAMPLES_DIRECTORY = pathlib.Path(app.outdir) / "examples"
        notebooks = list(RENDERED_EXAMPLES_DIRECTORY.glob("*.ipynb"))

        for notebook in status_iterator(
            notebooks,
            "Rendering notebook as PDF",
            "green",
            len(notebooks),
            verbosity=1,
            stringify_func=(lambda x: x.name),
        ):
            subprocess.run(
                [
                    "quarto",
                    "render",
                    str(notebook),
                    "--to",
                    "pdf",
                    "-M",
                    f"author:{author}",
                    "-M",
                    "highlight-style:pygments",
                ],
                check=True,
            )
    except FileNotFoundError:
        logger = logging.getLogger(__name__)
        logger.warning(
            "Quarto is not installed in the system. PDF files will not be rendered. "
            "See https://quarto.org/docs/get-started/"
        )


def setup(app: sphinx.application.Sphinx):
    """
    Run different hook functions during the documentation build.

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application instance containing the all the doc build configuration.

    """
    # Examples are kept in the repo root ``examples/`` directory. They are copied
    # into ``doc/source/examples/`` before Sphinx reads them (it requires all
    # source files to live under the source directory), and removed again once the
    # build finishes so they are not permanently duplicated.
    app.connect("config-inited", copy_examples_files_to_source_dir)
    app.connect("build-finished", remove_examples_from_source_dir)
    app.connect("build-finished", copy_examples_to_output_dir)
    app.connect("build-finished", render_examples_as_pdf)
