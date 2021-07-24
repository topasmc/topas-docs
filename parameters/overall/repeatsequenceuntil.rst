Set run duration based on statistical goals
-------------------------------------------

Users have requested a way to have TOPAS continue running until dose accuracy reaches
a user-determined limit (rather than just running a pre-determined number of histories).
This feature is now available, and we have done it in a general purpose way.

Because TOPAS supports time features, any accuracy test is only meaningful once the
entire run sequence has occurred. Accordingly, the new system works by evaluating various
tests only after the entire run sequence is complete (all Histories of all Runs).
TOPAS then evaluates various tests, and repeats the entire run sequence until all such
tests have been satisfied.

You create these "RepeatSequenceUntil" tests by attaching them to scorers.
Up to three tests can be applied to any scorer:

* RepeatSequenceUntilStandardDeviationLessThan repeat until a given standard deviation is achieved.
* RepeatSequenceUntilSumGreaterThan repeat until a given sum is reached.
* RepeatSequenceUntilCountGreaterThan repeat until a given number of counts are made.

The second two tests above are necessary because the StandardDeviation is subject to
statistical noise until a reasonable amount of data has been collected.
By requiring a minimum Sum or minimum number of Counts, one can insure that there is
enough data to use the StandardDeviation.

Tests can be applied to as many scorers as you wish.
The entire simulation will repeat until All tests on All scorers are satisfied.

New parameters are::

    d:Sc/*/RepeatSequenceUntilSumGreaterThan = 1. MeV # type can be d, u or i depending on scoring quantity
    d:Sc/*/RepeatSequenceUntilStandardDeviationLessThan = .004 MeV # type can be d, u or i
    i:Sc/*/RepeatSequenceUntilCountGreaterThan = 1200

If the scorer has been binned in X, Y, Z, E or T, you must also specify which specific bin
should be evaluated, using the parameters::

    i:Sc/*/RepeatSequenceTestXBin = 2
    i:Sc/*/RepeatSequenceTestYBin = 2
    i:Sc/*/RepeatSequenceTestZBin = 2
    i:Sc/*/RepeatSequenceTestEBin = 5
    i:Sc/*/RepeatSequenceTestTimeBin = 0

Remember that the tests will be evaluated only after the entire simulation sequence is complete.
You should therefore set
So/*/NumberOfHistoriesInRun
to a value small enough that this end of test will be reached in a reasonable time.
The final total number of histories will be that NumberOfHistoriesInRun times the number of
times the testing process causes TOPAS to re-run the entire sequence.
