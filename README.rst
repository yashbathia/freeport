# Pharrell Notes

> Maybe use python3 to develop will have no pull request issues of travis-ci.

1. Create tar: ``python setup.py sdist``

2. Create your own wheel: ``python setup.py bdist_wheel --universal``

===============================
freeport
===============================

.. image:: https://img.shields.io/pypi/v/freeport.svg
        :target: https://pypi.python.org/pypi/freeport

.. image:: https://img.shields.io/travis/yashbathia/freeport.svg
        :target: https://travis-ci.org/yashbathia/freeport

.. image:: https://readthedocs.org/projects/freeport/badge/?version=latest
        :target: https://readthedocs.org/projects/freeport/?badge=latest
        :alt: Documentation Status


Description
===========
Simple Python library to free a port

Installation
============

To install freeport, simply:

.. code-block::

    $ pip install freeport

Usage
=====

.. code-block::

    $ freeport -h
       usage: freeport [-h] portnumber

       positional arguments:
         portnumber  The number of the port you want free (Eg. 8000)

       optional arguments:
         -h, --help  show this help message and exit 
    
    $ freeport 8000
      Port 8000 is free. Processs 16130 killed successfully

* Free software: ISC license
* Documentation: https://freeport.readthedocs.org.

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
