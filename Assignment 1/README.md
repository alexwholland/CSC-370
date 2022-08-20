# CSC 370 - Relational Data Model Assignment

## Assignment Goals

In this assignment you will:

  * demonstrate knowledge of database decomposition (namely BCNF)

    + implement the calculation of attribute set closures to identify keys and normal form violations
    + implement a standard algorithm for decomposition, the BCNF Decomposition Algorithm

## Task

You should write a computer program in either Python or Java (or, after consultation with the instructor, another language of your choice) that determines how many levels of recursion are required to decompose a relation into BCNF. More specifically, you are provided with a class definition for a set of relations R and a set of functional dependencies F, and you should implement a function that returns -1 if the relations are not in BCNF or a non-negative integer indicating how many recursive steps of BCNF decomposition are required to convert the union of elements of R into R using BCNF decomposition with F. 

Be careful that there is more than one possible decomposition for a given input, depending on the order in which you process BCNF violations. For example, if you were to decompose R(A,B,C,D,E) into BCNF with functional dependencies AB→C and BD→C, there are two correct decompositions for which your program should output 1:

  * R1(ABC) and R2(ABDE), corresponding to decomposing with the first BCNF violation first
  * R1(BCD) and R2(ABDE), corresponding to decomposing with the second BCNF violation first

Note that R1(ABC), R2(ABD), and R3(DE) is not a correct solution, even though this decomposition is in BCNF, because you would not arrive at it using the decomposition algorithm in the textbook. (It has been decomposed unnecessarily much.) Your program should output -1 on this input.

As a third example, given R(A,B,C) and functional dependency AB→C, your program should output 0, because the input is already in BCNF.  

## Build Instructions

This project uses Python3 and can be run in any environment that supports Python3 (e.g., command line interpreter or Jupyter Notebook). There are no specific build requirements; you can simply run the test suite by executing the main method in `tests.py`
```
python3 ./tests.py
```

## Dependencies

In order to run this code, you will need:

  * Python3 (python2 is not guaranteed to be supported)
  * The `timeout-decorator` package if you want to confirm time-outs under 15s (or you can comment out those lines)
