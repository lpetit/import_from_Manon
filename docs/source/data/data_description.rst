Data collection
===============

Imaging Protocol
-----------------
Twenty healthy adults (mean age 36 years, age range 29-46 y.o.(SD = 4.7),
3 men and 17 women) were scan at the Centre Hospitalier Universitaire
of Sherbrooke (CHUS) using a clinical 3T MRI scanner (Ingenia, Philips
Healthcare, Best, Netherlands) with a 32-channel head coil.

Study design - 20 healthy subjects

.. image:: acquisition_design.png
   :align: center
   :width: 700
   
Each MRI session include : 

* Anatomical 3D T1-weighted (3DT1)

* Multi-shell diffusion-weighted images (DWI)

* Reverse phase encoding B0 (revb0)

* inhomogeneous magnetization transfer (ihMT) 


Data conversion: DICOM to BIDS
------------------------------

To convert data we use `BIDS standard <http://bids.neuroimaging.io/>`__.
An example of the data structure for one subject is shown below:

::

    data-subject
    ├── dataset_description.json
    ├── participants.json
    ├── participants.tsv
    ├── sub-001_ses-01
    ├── sub-001_ses-02
    ├── sub-001_ses-03
    ├── sub-001_ses-04
    ├── sub-001_ses-04
    ├── sub-002_ses-01
    ├── ...
    ├── sub-003_ses-01
        │
        ├── anat
        │   ├── sub-003-01_T1w.json
        │   ├── sub-003-01_T1w.nii.gz
        │   ├── sub-003-01_acq-pos_ihmt.json
        │   ├── sub-003-01_acq-pos_ihmt.nii.gz
        │   ├── sub-003-01_acq-neg_ihmt.json
        │   ├── sub-003-01_acq-neg_ihmt.nii.gz
        │   ├── sub-003-01_acq-altnp_ihmt.json
        │   ├── sub-003-01_acq-altnp_ihmt.nii.gz
        │   ├── sub-003-01_acq-altpn_ihmt.json
        │   ├── sub-003-01_acq-altpn_ihmt.nii.gz
        │   ├── sub-003-01_acq-T1w_ihmt.json
        │   └── sub-003-01_acq-T1w_ihmt.nii.gz
        │
        └── dwi
            ├── sub-003-01_dwi.bval
            ├── sub-003-01_dwi.bvec
            ├── sub-003-01_dwi.json
            ├── sub-003-01_dwi.nii.gz
            ├── sub-003-01_b0.json
            ├── sub-003-01_b0.nii.gz
            ├── sub-003-01_rev-b0.json
            └── sub-003-01_rev-b0.nii.gz



To convert our DICOM data folder to the compatible BIDS structure, we used
`dcm2bids <https://github.com/cbedetti/Dcm2Bids#install>`__.

.. code-block:: bash

  dcm2bids -d DICOM_folder -p id_subject -c config.txt -o sub-id


Quality Control raw data
------------------------

Quality control of raw data was performed using DMRIQC flow `DMRIQC flow <https://github.com/scilus/dmriqc_flow>`__.


Example of datasets for one subject
-----------------------------------

** Anatonimal image **

+---------------------------------+
|              3D-T1w             | 
+=================================+
| .. image:: 3DT1.gif             |
|    :width: 200                  |
+---------------------------------+

** Diffusion images **

+----------------------------+----------------------------+----------------------------+----------------------------+----------------------------+
|        DWI - b0            |    DWI - b value = 300     |    DWI - b value = 1000    |    DWI - b value = 2000    |      DWI - Reverse B0      |
+============================+============================+============================+============================+============================+
| .. image:: b0.gif          |  .. image:: b300.gif       | .. image:: b1000.gif       | .. image:: b2000.gif       | .. image:: epi.gif         |
|    :width: 200             |    :width: 200             |    :width: 200             |    :width: 200             |    :width: 200             |
+----------------------------+----------------------------+----------------------------+----------------------------+----------------------------+

** ihMT images **

+--------------------------+-----------------------+-----------------------+-----------------------+-----------------------+----------------------+
|          MT-Off          |     Positive (pos)    |    Negative (neg)     |  Alternative pos-neg  | Alternative neg-pos   |      T1w ihMT        |
+==========================+=======================+=======================+=======================+=======================+======================+
| .. image:: mtoff.gif     | .. image:: pos.gif    |  .. image:: neg.gif   | .. image:: altpn.gif  | .. image:: altnp.gif  | .. image:: T1w.gif   |
|    :width: 200           |    :width: 200        |    :width: 200        |    :width: 200        |    :width: 200        |    :width: 200       |
+--------------------------+-----------------------+-----------------------+-----------------------+-----------------------+----------------------+

