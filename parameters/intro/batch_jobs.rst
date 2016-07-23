.. _parameters_batch:

Controlling Multiple Batch Jobs
-------------------------------

The hierarchical nature of parameter files makes it easy to control multiple batch jobs.

Make up a parameter file (or hierarchy of files) that has most of your settings:

* MostOfMySettings.txt

Then make small additional parameter files for each job you want to submit:

* Job1.txt
* Job2.txt
* Job3.txt

where each of these files has::

    includeFile = MostOfMySettings.txt
    Ts/Seed = 1 # Set this differently for each of Job1, Job2, Job3, ...
    Sc/MyScorer/OutputFile = "Job1Output" # Set this differently for each of Job1, Job2, Job3,

Each job will thus have a unique starting random number seed (and hence produce a statistically distinct sample) and a unique output file specification, but all other aspects of the simulation will be identical from one job to the next.
