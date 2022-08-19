# CSC 370: Database Systems

## Course Overview
This course provides an overview of a relational database management system (RDBMS), from modelling 
the world and designing a database to querying the data and optimising performance in a manner that 
maintains the critical ACID properties of a database. This course includes elements of software engineering, 
theoretical computer science, programming, and computer systems.

## Contents Of This Repository 

**Assignment 1 - Relational Data Model**

- demonstrate knowledge of database decomposition (namely BCNF)
  - implement the calculation of attribute set closures to identify keys and normal form violations
  - implement a standard algorithm for decomposition, the BCNF Decomposition Algorithm
  
**Assignment 2 - Conceptual Data Modelling**

- demonstrate knowledge of conceptual data modelling and the SQL DDL
  - convert entity-relationship diagrams into a logical model
  - implement a model in a relational database with SQL
  
**Assignment 3 - SQL Golf**

- demonstrate data analysis skills with SQL
  - write SQL queries with varied complexity to extract desired information from a relational database
  - optimise SQL queries towards simplicity
  
**Assignment 4 - B+ Tree Implementation**

- demonstrate knowledge of some query optimisation concepts, particularly how B+-tree indexes work:
  - implement a B+-tree that handles insertions
  - implement efficient queries on the B+-tree


## Topics

- Logical Database Design with the Relational Data Model
  - The Relational Data Model
  - Basic Relational Algebra
  - Data Dependencies and Constraints
  - Normalisation
- Conceptual Database Design with the Entity-Relationship Model
  - Entity-Relationship Diagrams (ERD's)
  - Principles of good design
  - Mapping between ERD's and the relational data model
- Interacting with relational databases
  - Mathematically expressing the logic of complex queries (using a logic-based programming language called Datalog)
  - Writing queries in SQL (the de-facto standard declarative language for relational databases) to create databases, manipulate content, and perform data analysis
  - ACID properties, including transactions and isolation levels to support concurrency
  - Interfacing with relational databases using connectors like JDBC [optional content subject to the course's pace]
- Query Processing & Storage
  - The I/O Computational Model
  - Algorithms and data structures for efficiently computing query results
  - Physical and logical query plans expressed with relational algebra parse trees
  - Query cost estimation and query plan optimisation
  - Recovery, logging, redundancy, and resilience
  
 ## Objectives

- Database design: how can we describe the world in terms of data?
- Data analysis: how can we answer questions about the world in terms of questions on such data?
- Concurrency and robustness: how does the database management system (DBMS) allow multiple users to query and modify the same data? What happens when there is a system failure?
- Efficiency and scalability: how does the DBMS store large amounts of data and process them efficiently?


