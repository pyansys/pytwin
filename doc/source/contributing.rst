.. _ref_contributing:

============
Contributing
============
Overall guidance on contributing to a PyAnsys library appears in the
`Contributing <https://dev.docs.pyansys.com/how-to/contributing.html>`_ topic
in the *PyAnsys Developer's Guide*. Ensure that you are thoroughly familiar with
this guide, paying particular attention to the `Coding Style
<https://dev.docs.pyansys.com/coding-style/index.html#coding-style>`_ topic, before
attempting to contribute to PyTwin.
 
The following contribution information is specific to PyTwin.

Post issues
-----------
Use the `PyTwin Issues <https://github.com/pyansys/pytwin/issues>`_ page to
submit questions, report bugs, and request new features.

Clone the repository
--------------------
To clone and install the latest PyTwin release in development
mode, run:

.. code::

    git clone https://github.com/pyansys/pytwin.git
    cd pytwin
    pip install pip -U
    pip install -e .

Build documentation
-------------------
To build the PyTwin documentation locally, in the root directory of the
repository, run:

.. code:: 

    pip install -r requirements/requirements_doc.txt
    cd doc
    make html

After the build completes, the HTML documentation is located in the
``_builds/html`` directory. You can load the ``index.html`` file in
this directory into a web browser.

You can clear all HTML files from the ``_builds/html`` directory with:

.. code::

    make clean

Run unitary tests
-----------------
To launch ``pytwin`` unitary tests automatically and verify that code modifications do not break existing logic,
install `pytest <https://pypi.org/project/pytest/>`_ package into your Python environment and from the root
directory, run :

.. code::

    pytest --cov=pytwin --cov-report=term --cov-report=xml:.cov/coverage.xml --cov-report=html:.cov/html tests -vv

Adhere to code style
--------------------
PyTwin is compliant with the `PyAnsys code style
<https://dev.docs.pyansys.com/coding_style/index.html>`_. It uses the tool
`pre-commit <https://pre-commit.com/>`_ to check the code style. You can
install and activate this tool with:

.. code:: bash

   python -m pip install pre-commit
   pre-commit install


Or, you can directly execute `pre-commit <https://pre-commit.com/>`_ with:

.. code:: bash

    pre-commit run --all-files --show-diff-on-failure
