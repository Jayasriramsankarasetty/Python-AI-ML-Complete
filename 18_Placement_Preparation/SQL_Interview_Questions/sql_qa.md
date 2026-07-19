# SQL Interview Questions & Answers (Top 15)

This document contains 15 advanced SQL and Database design interview questions frequently asked during technical placement screenings.

---

### Q1: What is the difference between `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL JOIN`?
* **Answer**: 
  * `INNER JOIN`: Returns records that have matching values in both tables.
  * `LEFT JOIN` (or LEFT OUTER JOIN): Returns all records from the left table, and the matched records from the right table. (If no match, returns NULL for the right columns).
  * `RIGHT JOIN`: Returns all records from the right table, and the matched records from the left table.
  * `FULL JOIN` (or FULL OUTER JOIN): Returns all records when there is a match in either left or right table.

---

### Q2: What are SQL Window Functions and how do they differ from `GROUP BY`?
* **Answer**: Window functions perform a calculation across a set of table rows that are related to the current row. 
* **Difference**: Unlike `GROUP BY` (which collapses rows into a single summary output row), window functions calculate aggregates while retaining the individual rows in the output dataset. Syntax: `AGG_FUNC() OVER (PARTITION BY col ORDER BY col)`.

---

### Q3: What is the difference between `RANK()`, `DENSE_RANK()`, and `ROW_NUMBER()`?
* **Answer**:
  * `ROW_NUMBER()`: Assigns a unique sequential integer to each row starting at 1, regardless of duplicate values.
  * `RANK()`: Assigns sequential integers, but duplicate values receive the same rank. The next rank is skipped (e.g. 1, 2, 2, 4).
  * `DENSE_RANK()`: Assigns sequential integers, but duplicate values receive the same rank. The next rank is NOT skipped (e.g. 1, 2, 2, 3).

---

### Q4: Explain ACID properties in Relational Databases.
* **Answer**: ACID guarantees that database transactions are processed reliably:
  1. **Atomicity**: "All or nothing". Either the entire transaction succeeds, or it is completely rolled back.
  2. **Consistency**: A transaction must move the database from one valid state to another, adhering to constraints (e.g. foreign keys).
  3. **Isolation**: Concurrent execution of transactions leaves the database in the same state as if they were executed sequentially.
  4. **Durability**: Once a transaction is committed, its changes survive system crashes (stored in non-volatile memory).

---

### Q5: What is Database Indexing and how does it speed up queries?
* **Answer**: An index is a data structure (usually a B-Tree or B+ Tree) that stores pointer locations of key column values, allowing the query planner to locate rows without performing a slow O(N) sequential scan (Full Table Scan).
* **Tradeoff**: Indexes speed up GET/SELECT queries, but slow down write operations (INSERT, UPDATE, DELETE) since index trees must be recalculated on every write.

---

### Q6: What is Database Normalization and explain 1NF, 2NF, and 3NF?
* **Answer**: Normalization structures a database schema to minimize data redundancy and dependency anomalies:
  * **1NF (First Normal Form)**: Cell values must be atomic (no arrays or lists). Columns must have unique names.
  * **2NF (Second Normal Form)**: Must be in 1NF. All non-key attributes must be fully functionally dependent on the entire primary key (removes partial dependencies in composite keys).
  * **3NF (Third Normal Form)**: Must be in 2NF. No non-key attributes can have transitive dependencies on the primary key (no non-key attribute can depend on another non-key attribute).

---

### Q7: What is the difference between `WHERE` and `HAVING` clauses?
* **Answer**: 
  * `WHERE`: Filters individual rows *before* any grouping aggregates are calculated.
  * `HAVING`: Filters grouped summary rows *after* the `GROUP BY` aggregates are calculated. (Can contain aggregate functions like `SUM()` or `COUNT()`).

---

### Q8: What are Common Table Expressions (CTEs) and why are they used?
* **Answer**: A CTE is a temporary named result set defined using the `WITH` keyword, which can be referenced inside a subsequent SELECT statement.
* **Use case**: CTEs break down complex nested queries into readable segments, and recursive CTEs can traverse hierarchal tree charts.

---

### Q9: What is a Clustered vs Non-Clustered Index?
* **Answer**:
  * **Clustered Index**: Determines the physical storage order of the actual table rows on disk. There can only be ONE clustered index per table (typically the Primary Key).
  * **Non-Clustered Index**: Maintains a separate index tree structure containing key values and pointers pointing to the actual row storage address. There can be multiple non-clustered indexes.

---

### Q10: What is a Foreign Key constraint?
* **Answer**: A foreign key is a column or group of columns in one table that references the primary key of another table. It enforces referential integrity, ensuring records cannot be inserted with non-existent parent keys, and preventing parent record deletion when child records point to it (unless configured with `ON DELETE CASCADE`).

---

### Q11: Explain the difference between `UNION` and `UNION ALL`.
* **Answer**:
  * `UNION`: Merges the results of two queries and removes duplicate records (performs a sorting operation to deduplicate).
  * `UNION ALL`: Merges the results of two queries but retains all duplicate records, making it significantly faster since no sorting/deduplication is performed.

---

### Q12: What is database sharding?
* **Answer**: Sharding is a horizontal partitioning technique where database rows are split across multiple database instances (shards) based on a shard key. This allows systems to scale horizontally across multiple machines to handle heavy traffic loads.

---

### Q13: What is a SQL view and what is a materialized view?
* **Answer**:
  * **SQL View**: A virtual table representing a saved query. It does not store physical data; the query executes every time the view is read.
  * **Materialized View**: A view whose query results are physically cached on disk. It updates periodically or on triggers, allowing fast reads at the cost of stale data risks.

---

### Q14: Explain transaction isolation levels.
* **Answer**: SQL standards define 4 isolation levels:
  1. **Read Uncommitted**: Can read uncommitted data (dirty reads allowed).
  2. **Read Committed**: Can only read committed data (prevents dirty reads, but non-repeatable reads allowed).
  3. **Repeatable Read**: Re-reading data within the same transaction yields identical results (prevents non-repeatable reads, but phantom reads allowed).
  4. **Serializable**: Enforces strict execution order, locking resources entirely (prevents dirty, non-repeatable, and phantom reads; slowest performance).

---

### Q15: What is a database transaction deadlock?
* **Answer**: A deadlock occurs when two or more transactions are waiting for each other to release locks, creating a circular dependency block where neither transaction can proceed. Relational database engines detect deadlocks and abort/roll back one of the transactions to break the loop.
