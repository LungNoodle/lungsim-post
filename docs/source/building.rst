========================
How to install and build
========================

Requirements
==============

To use these libraries you need:

- A python interpreter

The requirements for building and use of this library is given in the requirements.txt file provided (available at `our github repository <https://github.com/LungNoodle/lungsim-post/blob/develop/requirements.txt>`_). A simple way to install these requirements is to do a batch install:

.. code-block:: console

    pip install -r requirements.txt

Install and run (not a developer)
=================================

Use pip to install the libraries

.. code-block:: console

    pip install git+https://github.com/LungNoodle/lungsim-post.git


Once installed the libraries can called from python

.. code-block:: python

    import lungsimpost

Install and run (for developing, quickstart)
============================================
You can find these libraries on github `here <https://github.com/LungNoodle/lungsim-post>`_.

To use and improve on these code we would like you to be familiar with github and python. If you aren't then we suggest that you look into an online course - there are plenty available via `Software Carpentry <https://software-carpentry.org/>`_ (for example).

Simply fork `this repository <https://github.com/LungNoodle/lungsim-post>`_ to your github account, and you are ready to clone onto your computer and start working! Once you have done this, you can set up branches to work through your edits to the code, and install locally using pip:

.. code-block:: console

    pip install -e /path/to/lungsim-post

Once installed the libraries can called from python:

.. code-block:: python

    import lungsimpost

To build the documentation locally on your machine, you will need sphinx:

.. code-block:: console

    pip install sphinx

Then, just navigate to the docs directory and use the make command (below shows for html docs, but you can make other formats that are provided with sphinx.

.. code-block:: console

    cd /path/to/lungsim-post/docs
    make html

Make sure you update any documentation alongside changes to the code!