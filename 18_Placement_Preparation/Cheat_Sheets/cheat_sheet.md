# High-Density Interview Cheat Sheet

A quick-reference sheet summarizing essential syntaxes and configurations for Python, SQL, Pandas, Scikit-learn, and Git.

---

## 1. Python Core Syntax

### Decorator Pattern
```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

### Generator Pattern
```python
def stream_numbers(limit):
    for i in range(limit):
        yield i
```

### List & Dictionary Comprehensions
```python
squares = [x**2 for x in range(10) if x % 2 == 0]
square_map = {x: x**2 for x in range(5)}
```

---

## 2. SQL Query Syntax

### Joins & Grouping
```sql
SELECT d.department_name, AVG(e.salary) AS avg_sal
FROM departments d
INNER JOIN employees e ON d.dept_id = e.dept_id
WHERE e.status = 'Active'
GROUP BY d.department_name
HAVING AVG(e.salary) > 50000;
```

### Window Functions (Ranking & Partitioning)
```sql
SELECT name, dept, salary,
       ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) as row_num,
       DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) as dense_rk
FROM employees;
```

### Common Table Expression (CTE)
```sql
WITH HighEarners AS (
    SELECT * FROM employees WHERE salary > 100000
)
SELECT dept, COUNT(*) FROM HighEarners GROUP BY dept;
```

---

## 3. Pandas Cheat Sheet

### Filtering & Aggregating
```python
# Filtering rows
df_filtered = df[(df["age"] > 30) & (df["city"] == "NY")]

# Groupby aggregations
df_grouped = df.groupby("department")["salary"].agg(["mean", "std", "count"])

# Pivot table creation
df_pivot = df.pivot_table(index="user_id", columns="movie_id", values="rating")
```

---

## 4. Scikit-Learn Fit-Predict Pipeline

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# 1. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Fit
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train_scaled, y_train)

# 4. Predict
y_pred = model.predict(X_test_scaled)
```

---

## 5. Git CLI Commands

```bash
# Clone a repository
git clone <repository_url>

# Branching
git checkout -b <new_branch_name>  # Create and switch to new branch
git branch -a                     # List all local and remote branches

# Committing Changes
git add .
git commit -m "feat: add model serving endpoints"

# Pulling & Pushing
git pull origin main              # Pull updates from remote repository
git push origin <branch_name>     # Push commits to remote branch
```
