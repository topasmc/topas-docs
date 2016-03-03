# topas-docs

The documentation is written in reStructuredText format (reST). It is hosted by [ReadTheDocs](https://docs.readthedocs.org). A good resource on reST is the [Sphinx documentation](http://www.sphinx-doc.org), but please note that not all features described there are supported by ReadTheDocs. It also describes some Python-only features, since that is its domain.

To build and view the docs locally (recommended for substantial editing), you will need to

    pip install sphinx sphinx-autobuild sphinx_rtd_theme

then, after your edits

    make clean
    make html
    open .build/html/index.html
