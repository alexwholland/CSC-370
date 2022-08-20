# CSC 370 - B+-Tree Implementation

## Assignment Goals

In this assignment you will:

  * demonstrate knowledge of some query optimisation concepts, particularly how B+-tree indexes work:

    + implement a B+-tree that handles insertions 
    + implement efficient queries on the B+-tree 

## Task

You are provided with a class definition for a ternary B+-tree, but it does not have any methods for inserting or querying data. 
You are also provided with an empty ImplementMe class that contains a number of unimplemented static methods to provide functionality for a B+-tree. 

You should complete the implementation of the three empty static functions: one for inserting a new key into a tree, one to look up whether a 
specific key is in the index, and one to retrieve all keys in the index within a range. The implementations of these must be computationally 
efficient in order to obtain marks.

## Build Instructions

This project uses Python3 and can be run in any environment that supports Python3 (e.g., command line interpreter or Jupyter Notebook). 
There are no specific build requirements; you can simply run the test suite by executing the main method in `tests.py`
```
python3 ./tests.py
```

## Dependencies

In order to run this code, you will need:

  * Python3 (python2 is not guaranteed to be supported)
