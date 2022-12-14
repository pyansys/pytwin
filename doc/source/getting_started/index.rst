.. _getting_started:

===============
Getting started
===============
PyTwin provides Pythonic access to Ansys Digital Twins Runtimes.
These Runtimes are generated using `Ansys Twin Builder and Twin Deployer <https://www.ansys.com/products/digital-twin/ansys-twin-builder>`_.

To run PyTwin, you must have a license of Ansys Twin Deployer
installed locally. PyTwin supports Runtimes generated using 2023 R1 and later.

Define the Ansys License Server
-------------------------------
Your Ansys License Manager must have a license file with the *twin_builder_deployer* feature available. Define the
following environment variable that specifies the location of your Ansys License Manager:

.. code::

   ANSYSLMD_LICENSE_FILE={PORT_NUMBER}@{SERVER_NAME}

Twin Runtimes dependencies
--------------------------
The ``pytwin`` package allows users to easily execute deployment workflows based on ``.twin`` files generated by `Ansys Twin Builder <https://www.ansys.com/products/digital-twin/ansys-twin-builder>`_, which are generally made up of several types of models (system level models, ROMs, 3rd party FMUs,...). Each of these models may have specific runtime dependencies (e.g. Modelica models cross-compiled with Ansys Twin Deployer on Ubuntu 20.04 have a dependency on libgfortran5). When executing the Twin Runtimes through ``pytwin`` on a specific environment, it is therefore important that all the dependencies of the Twin Runtimes, including the ones of their constitutive models, are properly installed and made available in that environment.

Install the package
-------------------
The ``pytwin`` package supports Python 3.8 through
Python 3.10 on Windows and Linux.

Install the latest release from `PyPi
<https://pypi.org/project/pytwin/>`_ with:

.. code::

   pip install pytwin

If you plan on doing local *development* of PyTwin with Git, install
the latest release with:

.. code::

   git clone https://github.com/pyansys/pytwin.git
   cd pytwin
   pip install pip -U
   pip install -e .


Any changes that you make locally are reflected in your setup after you restart
the Python kernel.

Additional PyAnsys libraries
-----------------------------
You can also install and use these additional PyAnsys libraries:

- `PyAEDT <https://aedt.docs.pyansys.com//>`_, which provides
  access to Ansys Twin Builder for models creation and Digital Twins Runtimes generation.

