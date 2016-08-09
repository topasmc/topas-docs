.. _multithreading:

Multithreading
--------------

TOPAS fully supports the Multi-Threaded simulation capability of Geant4.

By default, TOPAS will occupy just one CPU thread. To use more, adjust::

    i:Ts/NumberOfThreads # defaults to 1

* If set to a positive integer, TOPAS will use that number of threads
* If set to 0, TOPAS will use all of your computer's threads (may be number of hardware cores or number of virtual cores (which includes hyper-threading cores) depending on your hardware architecture.
* If set to a negative number, TOPAS will use all BUT this number of threads, leaving you some threads reserved for other tasks (email, web browsing, etc.).

By default, console output from various threads will be interleaved. Output from each worker thread will have a distinctive prefix, such as:

.. code-block:: text

    G4WT0 >
    G4WT1 >

To instead make Geant4 buffer the output, showing first everything from one thread and then everything from another thread, set::

    b:Ts/BufferThreadOutput = "True" # Causes console output to be show one thread at a time
