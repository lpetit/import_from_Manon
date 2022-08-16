Data collection and organization
================================

Imaging Protocol
-----------------
Twenty healthy adults were scan (4 men, 16 women), aged between 20 and 40 y.o.

.. raw:: html
  :file: description/acquisition_description.html (png ?/pdf? could be possible ? > GUILLAUME)

Data conversion: DICOM to BIDS
------------------------------

To convert data we use the`BIDS standard <http://bids.neuroimaging.io/>`__.
An example of the data structure for one subject is shown below:

    data-subject
    │
    ├── dataset_description.json
    ├── participants.json
    ├── participants.tsv
    ├── sub-003-01
    │   │
    │   ├── anat
    │   │   ├── sub-003-01_T1w.json
    │   │   ├── sub-003-01_T1w.nii.gz
    │   │   ├── sub-003-01_FLAIR.json
    │   │   ├── sub-003-01_FLAIR.nii.gz
    │   │   ├── sub-003-01_acq-pos_ihmt.json
    │   │   ├── sub-003-01_acq-pos_ihmt.nii.gz
    │   │   ├── sub-003-01_acq-neg_ihmt.json
    │   │   ├── sub-003-01_acq-neg_ihmt.nii.gz
    │   │   ├── sub-003-01_acq-altnp_ihmt.json
    │   │   ├── sub-003-01_acq-altnp_ihmt.nii.gz
    │   │   ├── sub-003-01_acq-altpn_ihmt.json
    │   │   ├── sub-003-01_acq-altpn_ihmt.nii.gz
    │   │   ├── sub-003-01_acq-T1w_ihmt.json
    │   │   └── sub-003-01_acq-T1w_ihmt.nii.gz
    │   │
    │   └── dwi
    │       ├── sub-003-01_dwi.bval
    │       ├── sub-003-01_dwi.bvec
    │       ├── sub-003-01_dwi.json
    │       ├── sub-003-01_dwi.nii.gz
    │       ├── sub-003-01_b0.json
    │       ├── sub-003-01_b0.nii.gz
    │       ├── sub-003-01_rev-b0.json
    │       └── sub-003-01_rev-b0.nii.gz
    │
    └── derivatives



To convert your DICOM data folder to the compatible BIDS structure, you need to install
`dcm2bids <https://github.com/cbedetti/Dcm2Bids#install>`__.

.. code-block:: bash

  dcm2bids -d DICOM_folder -p id_subject -c config.txt -o sub-id


Quality Control raw data
------------------------

Quality control of raw was performed using DMRI QC flow.
See https://github.com/scilus/dmriqc_flow

+Ref guillaume 


Example of datasets (+ param des images ?)
-------------------

** DWI **

.. raw:: html

    <iframe src="_static/sub-003-01_dwi.html"  width=800 height=400 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>

** T1w  **

.. raw:: html

    <iframe src="_static/sub-003-01_T1w.html"  width=800 height=500 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>

** FLAIR **

.. raw:: html

    <iframe src="_static/sub-003-01_FLAIR.html"  width=800 height=300 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>

** ihMT images **
** Alternative_positive_MTI - pos **

.. raw:: html

    <iframe src="_static/sub-003-01_acq-pos_ihmt.html"  width=800 height=400 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>

** Alternative_negative_MTI - neg **

.. raw:: html

    <iframe src="_static/sub-003-01_acq-neg_ihmt.html" width=800 height=400 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>

** Alternative_negative-positive_MTI - altnp **

.. raw:: html

    <iframe src="_static/sub-003-01_acq-altnp_ihmt.html"  width=800 height=400 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>

** Alternative_positive-negative_MTI - altpn **

.. raw:: html

    <iframe src="_static/sub-003-01_acq-altpn_ihmt.html" width=800 height=400 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>

** T1w_MTI - t1w **

.. raw:: html

    <iframe src="_static/sub-003-01_acq-T1w_ihmt.html"  width=800 height=400 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>
