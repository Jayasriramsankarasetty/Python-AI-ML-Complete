# SQL Placement Interview Questions

This folder covers solutions to high-frequency database interview questions (inspired by LeetCode Database problems).

---

## Question 1: Second Highest Salary (LeetCode 176)

### Problem Statement
Write an SQL query to find the second highest salary from the `Employee` table. If there is no second highest salary, return `null`.

**Schema**:
```sql
CREATE TABLE Employee (
    id INT,
    salary INT
);
```

### Solution (Subquery approach)
```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
```

### Solution (LIMIT OFFSET approach with NULL check wrapper)
```sql
SELECT (
    SELECT DISTINCT salary 
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
```

---

## Question 2: Nth Highest Salary (LeetCode 177)

### Problem Statement
Write an SQL query to report the $N^{th}$ highest salary from the `Employee` table. If there is no $N^{th}$ highest salary, the query should report `null`.

### Solution (UDF/Function template)
```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
      SELECT DISTINCT salary 
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N
  );
END
```

---

## Question 3: Combine Two Tables (LeetCode 175)

### Problem Statement
Write an SQL query to report the first name, last name, city, and state of each person in the `Person` table. If the address of a `personId` is not in the `Address` table, report `null` instead.

**Schema**:
```sql
CREATE TABLE Person (
    personId INT PRIMARY KEY,
    lastName VARCHAR(50),
    firstName VARCHAR(50)
);

CREATE TABLE Address (
    addressId INT PRIMARY KEY,
    personId INT,
    city VARCHAR(50),
    state VARCHAR(50)
);
```

### Solution (LEFT JOIN)
```sql
SELECT 
    p.firstName, 
    p.lastName, 
    a.city, 
    a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;
```

---

## Question 4: Department Highest Salary (LeetCode 184)

### Problem Statement
Write an SQL query to find employees who have the highest salary in each of the departments.

**Schema**:
```sql
CREATE TABLE Employee (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT,
    departmentId INT
);

CREATE TABLE Department (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
```

### Solution (Window Function approach)
```sql
SELECT 
    Department,
    Employee,
    Salary
FROM (
    SELECT 
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER(PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
    FROM Employee e
    INNER JOIN Department d ON e.departmentId = d.id
) temp
WHERE temp.rnk = 1;
```

### Solution (Correlated Subquery approach)
```sql
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
INNER JOIN Department d ON e.departmentId = d.id
WHERE e.salary = (
    SELECT MAX(salary)
    FROM Employee
    WHERE departmentId = e.departmentId
);
```
