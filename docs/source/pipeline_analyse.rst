Analysis pipeline
=================

Processing
---------------
For MRI images processing all processing tools were availables on SCIL git page.
https://github.com/scilus


** DWI and T1 processing :
    Tractoflow      https://github.com/scilus/tractoflow version
    NODDI flow      https://github.com/scilus/noddi_flow
** MTI processing : scilus
** Segmentation of bundles :
    RecobundlesX      https://github.com/scilus/rbx_flow version
** Profiling bundles :
    Tractometry flow  https://github.com/scilus/tractometry_flow version


Quality Control
---------------

After running the analysis, check your Quality Control (QC) report by
opening the file ``~/spineGeneric_results/qc/index.html``. Use the "Search"
feature of the QC report to quickly jump to segmentations or labeling
results.


Generate common space from b0 images
------------------------------------

Common space is generated from b0 images resulting from Tractoflow using ANTs.

.. code-block:: bash

  buildparalleltemplate.sh -d 3 ...


To generate mean image for each measure, run:

.. code-block:: python

  # Mean images (example for FA map)
  scil_image_math.py mean *fa*.nii.gz mean_fa_healthy_control.nii.gz
  # Standard deviation images
  scil_image_math.py sd *fa*.nii.gz sd_fa_healthy_control.nii.gz



Consistency analysis
-------
