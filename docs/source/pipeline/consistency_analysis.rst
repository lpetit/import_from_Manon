Consistency analysis
====================

The consistency analyses of each measure were carried out at the voxel-level
within the bundles mask in common space using this script (script alex).


Bundle-averaged 
---------------

For each bundle, a density map was computed and used to generate a binary mask of the whole bundle. 
To minimize the effect of partial volume, each whole bundle mask was eroded by one voxel to generate 
a conservative bundle mask that we called the “safe mask”. 

Bundle-profile
---------------

To generate the bundle-profile (also called track-profiles), Tractometry was applied to each subject-specific 
bundle to obtain 10 binary mask corresponding to 10 equidistant sections. Each binary mask was then intersected
with the safe mask. 

:: image: consistency_pipe.png

