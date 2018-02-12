tmplog
=================

Utilities which I use for debugging purposes in python projects.

Usage
-----

.. code::

   from tmplog import tmplog

   # General usage
   tmplog(a=a, b=b)

   # Customized usage
   tmplog(file='/path/to/file', context='nl', format_value=False, a=a, b=b)
