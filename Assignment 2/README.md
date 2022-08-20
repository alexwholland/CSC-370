# CSC 370 - Conceptual Data Modelling Assignment

## Assignment Goals

In this assignment you will:

  * demonstrate knowledge of conceptual data modelling and the SQL DDL

    + convert entity-relationship diagrams into a logical model
    + implement a model in a relational database with SQL

## Task

You should write a computer program in python (or another programming language with prior approval of the instructor) that will take as 
input an entity-relationship diagram (ERD) and identify the set of MySQL tables that match the ERD, specified in terms of table names, 
attributes, primary keys, and foreign keys.

You have been provided with an ERD class that can be directly instantiated. You are also provided with a Database class that has methods 
for comparing two databases for equality and for printing out CREATE TABLE statements. There is only one function missing, the one that you 
should implement, which converts an arbitrary ERD instance into a corresponding Database instance.

You will need to handle all concepts introduced in the lessons (e.g., weak entity sets, subclass hierarchies, many-many relationships), 
but you should assume that every one-many and many-one relationship requires referential integrity. You should not modify any identifiers.

The starter code, test harness, and README with build instructions has been shipped out in Python and attached as a compressed archive to 
this assignment description. For specific build and run instructions, refer to the relevant README.

## Build Instructions

This project uses Python3 and can be run in any environment that supports Python3 (e.g., command line interpreter or Jupyter Notebook). There are no specific build requirements; you can simply run the test suite by executing the main method in `tests.py`
```
python3 ./tests.py
```

## Dependencies

In order to run this code, you will need:

  * Python3 (for the ENUM library)
