Data collection
===============

Imaging Protocol
-----------------
Twenty healthy adults (mean age 36 years, age range 29-46 y.o.(SD = 4.7),
3 men and 17 women) were scan at the Centre Hospitalier Universitaire
of Sherbrooke (CHUS) using a clinical 3T MRI scanner (Ingenia, Philips
Healthcare, Best, Netherlands) with a 32-channel head coil.

.. image:: acquisition_description.png
   :scale: 30 %
   :align: center

Data conversion: DICOM to BIDS
------------------------------

To convert data we use `BIDS standard <http://bids.neuroimaging.io/>`__.
An example of the data structure for one subject is shown below:

::

    data-multi-subject
    ├── dataset_description.json
    ├── participants.json
    ├── participants.tsv
    ├── sub-003_ses-01
        │
        ├── anat
        │   ├── sub-003-01_T1w.json
        │   ├── sub-003-01_T1w.nii.gz
        │   ├── sub-003-01_FLAIR.json
        │   ├── sub-003-01_FLAIR.nii.gz
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



To convert your DICOM data folder to the compatible BIDS structure, you need to install
`dcm2bids <https://github.com/cbedetti/Dcm2Bids#install>`__.

.. code-block:: bash

  dcm2bids -d DICOM_folder -p id_subject -c config.txt -o sub-id


Quality Control raw data
------------------------

Quality control of raw data was performed using DMRIQC flow `DMRIQC flow <https://github.com/scilus/dmriqc_flow>`__.


Example of datasets GIF
-------------------

** DWI **

** T1w  **

** FLAIR **

** ihMT images **

* Alternative_positive_MTI - pos *


* Alternative_negative_MTI - neg *


* Alternative_negative-positive_MTI - altnp *


* Alternative_positive-negative_MTI - altpn *


* T1w_MTI - t1w *
