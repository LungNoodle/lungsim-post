=======
Modules
=======

Modules should be collections of functions that are linked to one another in a logical way
make sure that before you add some code to a module, it actually fits in that module.

Its pretty simple to make a new module, just make a file in the `src/lungsimpost` directory called
`module_name.py`, add a corresponding `test_module_name.py` to the `tests` directory, and then add some
documentation (list on this page, and create a `.rst` file to the `docs/Modules` directory that auto-creates
documentation from doc strings in the module itself. The final step is to expose the module to the library in the `src/lungsimpost__init__.py` file.

List of modules
---------------

#.. toctree::
#   :maxdepth: 1