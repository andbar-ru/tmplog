tmplog
=================

Utilities which I use for debugging purposes in python projects.

Usage
-----

.. code::

   from tmplog import tmplog

   # General usage
   tmplog(a, b)
   tmplog(a=a, b=b)
   tmplog(a, b, c=c, d=d)

   # Customized usage
   tmplog(file='/path/to/file', context='nl', format_value=False, a=a, b=b)
