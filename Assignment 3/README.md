# CSC 370 - SQL Golf

## Assignment Goals

In this assignment you will:

  * demonstrate data analysis skills with SQL

    + write SQL queries with varied complexity to extract desired information from a relational database
    + optimise SQL queries towards simplicity

## Task

[Code Golf](https://www.barrymichaeldoyle.com/code-golf/) is a sort of recreational programming activity in which one tries to implement functionality using as few characters as possible. The general goal is to think of alternative solutions to a problem and it derives its name from the sport of _golf_, in which one tries to minimise the number of whacks with an iron shaft to put a tiny ball in a far-flung hole. In this assignment, you will try not just to write SQL queries that are correct, but that also are "minimal." 

As an example, imagine that you have two relations: *Employee(<ins>employee_id</ins>, employee_name, dept_id)* and *Department(<ins>dept_id</ins>, dept_name)* and you would like to find the names of all employees in a department named "Shipping & Receiving". A simple solution would be:

```sql
SELECT `employee_name`
FROM `Employee`
    NATURAL JOIN `Department`
WHERE `dept_name` LIKE 'Shipping \& Receiving';
```

Certainly, another "correct" solution would be:

```sql
SELECT `employee_name`
FROM `Employee`
WHERE `dept_id` IN (
    SELECT `dept_id`
    FROM `Department`
    WHERE `dept_name` LIKE 'Shipping \& Receiving' );
```

Both queries retrieve the same result, but the second query is unnecessarily complex, or at the very least non-idiomatic. I hope that you prefer the first solution. Even if not, this assignment is designed to encourage you to write the first query by rewarding you inversely to the number of times any of the following tokens appears in your SQL query:

  * SELECT (i.e., projection operator)
  * FROM (i.e., the table- or index-scan operator)
  * , (i.e., the cross product operator, _including other appearances such as in a SELECT clause_)
  * JOIN (i.e., a theta-, natural, or outer join or per MySQL an intersection)
  * UNION (i.e., the bag union operator)
  * DISTINCT (i.e., the duplicate elimination operator)
  * GROUP (i.e., the group-by operator)
  * ORDER (i.e., the sort operator)
  * HAVING (i.e., the selection operator applied to groups)
  * WHERE (i.e., the selection operator applied to tuples)
  * LIMIT (i.e., the MySQL top-k operator)

This gives us a metric by which to claim the first query is better: it only uses 4 instances of the above set of operators (SELECT, FROM, JOIN, and WHERE), whereas the second query uses 6 instances (2×SELECT, 2×FROM, 2×WHERE). This is the metric that you should aim to minimise with the SQL queries that you submit. You would receive more marks for the first query than the second one.

It is important to remember that this is an exercise in code simplification and creative thinking, not in performance optimisation. Although you are trying to minimise the number of operator references, SQL is a _declarative language_ and there is no specific reason to assume that the first example query will run faster than the second one. However, simple and idiomatic code is easier for compilers to optimise, so there could be tangential performance benefits to striving for simpler—or at least shorter—queries. _The real intent here is to leverage an assumed correlation between this "golf score" metric and the quality of a SQL query to encourage you to write better SQL_.

You are given instructions to create (optionally) a MySQL database or to connect to one on a remote server. Moreover, you are given fiften `.sql` files that are unfortunately empty except for a comment indicating their intended query and their mapping between "SQL Golf" scores (i.e., total instances of the aforementioned operators/tokens) and grade. For example, the above problem would be represented by the following `example.sql` file:

```sql
-- Find the names of all employees in a department named "Shipping & Receiving"
-- 1.1 marks: <4 operators
-- 1.0 marks: <6 operators
-- 0.8 marks: correct answer

-- Replace this comment line with the actual query
```

Alongside the `.sql` file will be a `.tsv` file showing the expected result, which you can use for testing.


## Submission

You should submit all fifteen of the `.sql` files _without renaming them_, but after replacing the final comment line with an actual SQL query that achieves the stated objective. Ordinarily, you should submit fifteen `.sql` files, though it is okay to submit fewer files if you do not have a solution for all fifteen tests.


## Dataset

For this assignment, we will use [a compilation of US county-level census data](https://github.com/evangambit/JsonOfCounties) that has been transformed from a document-oriented to a relational format for the purpose of this assignment. The data has been loaded into MySQL and [exported into .sql format](./counties.sql). You can import it into your local instance of MySQL from the command line as follows:

```bash
mysql -u [username] -p -e "CREATE DATABASE counties;"
mysql -u [username] -p counties < counties.sql
```

(Or, you could simply copy-paste the whole file into a query window.)


Finally, you can also access a read-only, pre-populated version of this database on port 3306 and server csc370db.csc.uvic.ca. The server is only available from within the firewall; so, you must first connect to the intranet via VPN or to linux.csc.uvic.ca via SSH. 


