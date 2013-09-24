Warehouse Tests
===============

Warehouse Tests is a collection of acceptance tests that can be ran against
a Python Package Repository to determine if it is a compliant repository.

Run the Tests
-------------

The tests must be run against a sandboxed instance of the implementation to be
tested. These tests will modify the instance and it is expected that after they
are done the instance will be thrown away.

.. code:: bash

    # Runs the tests against an index server available at http://example.com/
    $ py.test --base-url http://example.com/
