.. _physics_reference:

Reference Physics Lists
-----------------------

Reference physics lists are pre-made, complete lists provided by Geant4.

One complication with reference lists is that they do not support use of Parallel Worlds. This means that you cannot place components into a parallel world, and, for the dividable components (TsBox, TsCylinder and TsSphere), you cannot score with a different set of divisions than you have set for the component itself (we handle such complex scoring by creating parallel worlds). TOPAS will give an error if you attempt to use a reference list in a situation where parallel worlds are needed. In such situations, use Geant4_Modular as described below.

The names of the reference physics lists, and their detailed descriptions, are `here
<http://geant4.web.cern.ch/geant4/support/proc_mod_catalog/physics_lists/referencePL.shtml>`_.

To use a reference physics list, specify the list name in the Type parameter, such as::

    s:Ph/Default/Type = "QGSP_BERT_HP"

Reference physics lists allow only one additional option::

    d:Ph/Default/CutForAllParticles = 0.05 mm # single range cut to use for all particles
