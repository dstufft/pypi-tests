PyPI Tests
==========

PyPI Tests is a collection of acceptance tests that can be ran against
a Python Package Repository to determine if it is a compliant repository.


Running the Tests
-----------------

Setup
~~~~~

* There must be a package named ``pypi.testpkg`` on the index server with the
versions ``1.0``, ``1.5``, and ``2.0`` uploaded as sdist's (tar.gz).


Execution
~~~~~~~~~

.. code:: bash

    # Runs the tests against an index server available at http://example.com/
    $ py.test --simple-url http://example.com/simple/
