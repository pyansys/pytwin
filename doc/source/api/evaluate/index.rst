.. _ref_index_api_evaluate:

Evaluate
========

Evaluate module is an example of higher level abstraction implementation
to facilitate the manipulation and execution of Twin Runtimes through TwinModel.

.. currentmodule:: pytwin

.. autosummary::
   :toctree: _autosummary

   TwinModel

Workflow Example
----------------

.. code-block:: pycon

   >>> from pytwin import TwinModel
   >>> from pytwin import examples

   # downloading the input files
   >>> twin_file = examples.download_file("CoupledClutches_23R1_other.twin", "twin_files")
   >>> csv_input = examples.download_file("CoupledClutches_input.csv", "twin_input_files")
   >>> twin_config = examples.download_file("CoupledClutches_config.json", "twin_input_files")

   # loading the CSV file containing the Twin input data over time
   >>> twin_model_input_df = examples.load_data(csv_input)
   # Loading and instantiating the TwinModel
   >>> twin_model = TwinModel(twin_file)

   >>> inputs = dict()
   >>> for column in twin_model_input_df.columns[1::]:
   ...     inputs[column] = twin_model_input_df[column][0]
   ...

   # Initializing the TwinModel given initial inputs values as well as a configuration file for parameters values
   >>> twin_model.initialize_evaluation(inputs=inputs, json_config_filepath=twin_config)

   # Evaluating the TwinModel in batch mode and printing the computed outputs values
   >>> results_batch_pd = twin_model.evaluate_batch(twin_model_input_df)
   >>> print(results_batch_pd)
          Time  Clutch1_torque  Clutch2_torque  Clutch3_torque
   0     0.000      -10.000000             0.0             0.0
   1     0.001       -9.999997             0.0             0.0
   2     0.002       -9.999999             0.0             0.0
   3     0.003       -9.999985             0.0             0.0
   4     0.004       -9.999956             0.0             0.0
   ...     ...             ...             ...             ...
   1496  1.496        0.000000             0.0             0.0
   1497  1.497        0.000000             0.0             0.0
   1498  1.498        0.000000             0.0             0.0
   1499  1.499        0.000000             0.0             0.0
   1500  1.500        0.000000             0.0             0.0

   [1501 rows x 4 columns]
