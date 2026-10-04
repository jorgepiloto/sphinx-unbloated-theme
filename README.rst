|python| |pypi| |GH-CI| |MIT|

.. |python| image:: https://img.shields.io/pypi/pyversions/sphinx-unbloated-theme?logo=python&logoColor=white&label=Python
   :target: https://pypi.org/project/sphinx-unbloated-theme/
   :alt: Python

.. |pypi| image:: https://img.shields.io/pypi/v/sphinx-unbloated-theme.svg?logo=pypi&logoColor=white&label=PyPI
   :target: https://pypi.org/project/sphinx-unbloated-theme/
   :alt: PyPI

.. |GH-CI| image:: https://github.com/jorgemartinez/sphinx-unbloated-theme/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/jorgemartinez/sphinx-unbloated-theme/actions/workflows/ci.yml
   :alt: GH-CI

.. |MIT| image:: https://img.shields.io/badge/License-MIT-white.svg?labelColor=black
   :target: https://opensource.org/licenses/MIT
   :alt: MIT

About
=====

The Sphinx Unbloated Theme is a minimal, clean HTML theme for
`Sphinx <https://www.sphinx-doc.org/>`_. It is built on Sphinx's ``basic``
theme — the only dependency — and uses vanilla CSS with no third-party
frameworks or bundlers.

The theme is intentionally small: a single well-organised CSS file, a Jinja2
layout template, and a handful of configuration options. It is designed to be
easy to read, easy to override, and fast to load.

Installation
============

Ensure your environment meets the `prerequisites`_. Then follow the
`installation guidelines`_ for step-by-step instructions.

Quick install with pip:

.. code-block:: bash

   pip install sphinx-unbloated-theme

Then set the theme in your ``conf.py``:

.. code-block:: python

   html_theme = "sphinx_unbloated_theme"

Documentation
=============

The `official documentation`_ contains the following sections:

- `Getting started`_. A brief overview of the theme, prerequisites, and
  installation instructions to get your documentation site up and running
  in minutes.

- `User guide`_. Detailed documentation of all configuration options,
  layout conventions, and CSS customisation hooks. This is the right place
  to learn how to tailor the theme to your project.

- `API reference`_. Auto-generated reference for the public Python API
  exposed by the theme package (Sphinx extension hooks, version helpers,
  etc.).

- `Examples`_. A gallery of self-contained scientific Python notebooks that
  demonstrate the theme rendering prose, code blocks, maths, figures, and
  interactive output.

- `Changelog`_. A version-by-version summary of notable changes, bug fixes,
  and new features.

Troubleshooting
===============

For troubleshooting or reporting issues, please open an issue in the project
repository:

- Go to the `project repository`_.
- Click the **Issues** tab.
- Click **New Issue**.
- Provide a clear description of the problem, including any error messages,
  code snippets, or screenshots that help reproduce it.

License
=======

This project is distributed under the MIT licence. See the `LICENSE`_ file
for the full licence text.

Changelog
=========

The changelog tracks notable changes for each release of the Sphinx Unbloated
Theme. To view the full history, see the `changelog file`_ in the repository.


.. _prerequisites: https://jorgemartinez.space/projects/sphinx-unbloated-theme/version/stable/getting-started/prerequisites.html
.. _installation guidelines: https://jorgemartinez.space/projects/sphinx-unbloated-theme/version/stable/getting-started/installation.html

.. _official documentation: https://jorgemartinez.space/projects/sphinx-unbloated-theme/version/stable/
.. _getting started: https://jorgemartinez.space/projects/sphinx-unbloated-theme/version/stable/getting-started.html
.. _user guide: https://jorgemartinez.space/projects/sphinx-unbloated-theme/version/stable/user-guide.html
.. _api reference: https://jorgemartinez.space/projects/sphinx-unbloated-theme/version/stable/api-reference.html
.. _examples: https://jorgemartinez.space/projects/sphinx-unbloated-theme/version/stable/examples.html
.. _changelog: https://jorgemartinez.space/projects/sphinx-unbloated-theme/version/stable/changelog.html

.. _project repository: https://github.com/jorgemartinez/sphinx-unbloated-theme
.. _LICENSE: https://github.com/jorgemartinez/sphinx-unbloated-theme/blob/main/LICENSE
.. _changelog-file: https://github.com/jorgemartinez/sphinx-unbloated-theme/blob/main/CHANGELOG.md
