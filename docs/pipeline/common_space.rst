Common Space
============

Build common space
------------------
To evaluate the consistency of each measure at the voxel level across the
bundles in the whole brain, we build a common space based on our population.
Common space is generated from b0 images resulting from Tractoflow using
ANTs as follow:

.. code-block:: bash

  buildtemplateparallel.sh -d 3 -o b0_template -g 0.2 -c 2 -j 4 -s CC -r 1 -k 1 -m 100x70x50 -t GR b0*nii.gz

.. note::

   As we used the b0 output from tractoflow, b0 images are already
   pre-processing (including skull stripping, resampling, distorsion correction...),
   see Tractoflow description here https://tractoflow-documentation.readthedocs.io.


Average metrics maps
--------------------

To generate mean image for each measure, we run scilpy python script:

.. code-block:: python

  # Mean images (example for FA map)
  scil_image_math.py mean *fa*.nii.gz mean_fa_healthy_control.nii.gz

  # Standard deviation images
  scil_image_math.py sd *fa*.nii.gz sd_fa_healthy_control.nii.gz
