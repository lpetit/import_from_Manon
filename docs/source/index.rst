Welcome to the High-frequency MRI database documentation
=========================================================

TractoFlow pipeline is developed by the Sherbrooke Connectivity Imaging Lab (`SCIL`_)
in order to process diffusion MRI dataset from the raw data to the tractography.
The pipeline is based on Nextflow and Singularity. The goal with this pipeline
is to be fast and reproducible.

.. _SCIL: http://scil.usherbrooke.ca/en/

Our work is published in ***** (need to adapt):

   Edde M., Theaud G., Dumont M., Théberge A., Valcourt-Caron A., Gilbert G.,
   Houde J.C., Maltais L., Rheault F.,Spagnolo F., Barakovic M., Magon S. and Descoteaux M.
   High frequency advanced longitudinal white matter MRI database: Bundles-profiling stability and more,
   in review in Sciences Data

.. toctree::
   :maxdepth: 1
   :caption: Data

   data/overview
   data/data_description

.. toctree::
   :maxdepth: 1
   :caption: Pipeline

   pipeline/mri_processing
   pipeline/common_space
   pipeline/bundles
   pipeline/consistency_analysis

.. toctree::
   :maxdepth: 1
   :caption: Results

   results/average_maps
   results/correlation
   results/measure
   results/consistency
   results/fiber_population

   
   
