
![[Pasted image 20250626132544.png]] Example Scheme 


## 1. Relational Database Concepts:

Before SQL, let's briefly touch upon the structure.

- **Database:** A structured collection of data. (e.g., Your "Blood Bank Management System" database).
    
- **Table (Relation):** A collection of related data organized into rows and columns. Each table represents an "entity" in your system.
    
    - **Example:** `patients`, `admissions`, `doctors`, `hospitals`, `province_names` are all tables.
        
- **Column (Attribute/Field):** A vertical set of data containing values for a specific characteristic. Each column has a name and a data type (e.g., text, number, date).
    
    - **Example:** In the `patients` table, `patient_id`, `patient_name`, `gender`, `date_of_birth` are columns.
        
- **Row (Record/Tuple):** A horizontal set of data representing a single entry or record in the table.
    
    - **Example:** A single entry in the `patients` table for "Alice Smith" is a row.
        
- **Primary Key (PK):** A column (or set of columns) that uniquely identifies each row in a table. It cannot contain `NULL` values and must be unique.
    
    - **Example:** `patient_id` in `patients` table, `admission_id` in `admissions` table.
        
- **Foreign Key (FK):** A column (or set of columns) in one table that refers to the Primary Key in another table. It establishes a link or relationship between tables. Foreign keys ensure referential integrity, meaning you can't have an `admission` for a `patient_id` that doesn't exist in the `patients` table.
    
    - **Example:** `patient_id` in `admissions` is a foreign key referencing `patient_id` in `patients`. `doctor_id` in `admissions` is a foreign key referencing `doctor_id` in `doctors`.
        

## 2. Core SQL Commands (The DML & DDL Basics):

SQL commands are broadly categorized. For core concepts, we'll focus on Data Manipulation Language (DML) and Data Definition Language (DDL).

### A. Data Definition Language (DDL) - For defining the database structure

1. **`CREATE TABLE`**: Used to create a new table in the database.
    
    - **Easy:** You build the blueprint for your data.
        
    - **In-depth:** You specify column names, data types (`INT`, `VARCHAR`, `DATE`), constraints (`PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`), and default values.
        
    - **Example:**
        
        SQL
        
        ```
        CREATE TABLE patients (
            patient_id INT PRIMARY KEY AUTO_INCREMENT, -- AUTO_INCREMENT for unique IDs
            patient_name VARCHAR(100) NOT NULL,
            gender CHAR(1),
            date_of_birth DATE
        );
        ```
        
2. **`ALTER TABLE`**: Used to modify an existing table structure.
    
    - **Easy:** Change the blueprint after it's made.
        
    - **In-depth:** Add/drop columns, change column data types, add/remove constraints.
        
    - **Example:** `ALTER TABLE patients ADD COLUMN phone_number VARCHAR(15);`
        
3. **`DROP TABLE`**: Used to delete an existing table.
    
    - **Easy:** Throw away the whole blueprint and all its data.
        
    - **In-depth:** Be very careful! This permanently deletes the table and all its data.
        
    - **Example:** `DROP TABLE old_records;`
        

### B. Data Manipulation Language (DML) - For managing data within tables

1. **`INSERT INTO`**: Used to add new rows (records) into a table.
    
    - **Easy:** Put new data into your table.
        
    - **In-depth:** You specify which columns to fill and their corresponding values. Values must match the column's data type.
        
    - **Example:**
        
        SQL
        
        ```
        INSERT INTO patients (patient_id, patient_name, gender, date_of_birth)
        VALUES (1, 'Alice Smith', 'F', '1990-05-15');
        ```
        
2. **`SELECT`**: Used to retrieve data from one or more tables. This is arguably the most fundamental and frequently used SQL command.
    
    - **Easy:** Ask the database for specific information.
        
    - **In-depth:** The powerhouse of SQL. It's often combined with other clauses (`FROM`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT`).
        
    - **Example:**
        
        - `SELECT * FROM patients;` -- Selects all columns and all rows from the `patients` table.
            
        - `SELECT patient_name, date_of_birth FROM patients;` -- Selects specific columns.
            
        - `SELECT diagnosis FROM admissions;` -- Selects the diagnosis from all admissions.
            
3. **`UPDATE`**: Used to modify existing data in a table.
    
    - **Easy:** Change information that's already there.
        
    - **In-depth:** You specify the table, the column(s) to update, the new value(s), and critically, a `WHERE` clause to specify _which_ rows to update. **Without a `WHERE` clause, it updates ALL rows!**
        
    - **Example:** `UPDATE patients SET phone_number = '9876543210' WHERE patient_id = 1;`
        
4. **`DELETE FROM`**: Used to remove rows from a table.
    
    - **Easy:** Get rid of some data.
        
    - **In-depth:** You specify the table and, like `UPDATE`, a `WHERE` clause to specify _which_ rows to delete. **Without a `WHERE` clause, it deletes ALL rows!**
        
    - **Example:** `DELETE FROM patients WHERE patient_id = 1;`
        

## 3. The `SELECT` Statement - Deep Dive:

The `SELECT` statement is where most of the "logic" in SQL resides.

- **`FROM` Clause:** Specifies the table(s) from which to retrieve data.
    
    - **Example:** `FROM patients`
        
- **`WHERE` Clause:** Filters rows based on a specified condition. This is crucial for retrieving specific data.
    
    - **Easy:** Get only the rows that match my criteria.
        
    - **In-depth:** Uses comparison operators (`=`, `!=`, `<`, `>`, `<=`, `>=`), logical operators (`AND`, `OR`, `NOT`), `LIKE` (for pattern matching, e.g., `WHERE patient_name LIKE 'A%'`), `IN` (for multiple values, e.g., `WHERE patient_id IN (1, 5, 10)`), `BETWEEN` (for ranges).
        
    - **Example:** `SELECT patient_name FROM patients WHERE gender = 'F' AND date_of_birth < '2000-01-01';`
        
- **`ORDER BY` Clause:** Sorts the result set.
    
    - **Easy:** Arrange my results.
        
    - **In-depth:** Sorts by one or more columns, either `ASC` (ascending, default) or `DESC` (descending).
        
    - **Example:** `SELECT patient_name, date_of_birth FROM patients ORDER BY date_of_birth DESC;`
        
- **`LIMIT` (or `TOP`/`ROWNUM`):** Restricts the number of rows returned.
    
    - **Easy:** Only show me the first X results.
        
    - **In-depth:** Used for pagination or getting top N records. Syntax varies slightly by database (e.g., `LIMIT 10` in MySQL/PostgreSQL, `TOP 10` in SQL Server, `ROWNUM <= 10` in Oracle).
        
    - **Example:** `SELECT patient_name FROM patients ORDER BY patient_id LIMIT 5;`
        

## 4. Joins - Connecting Related Tables:

This is where the power of relational databases truly shines. Joins combine rows from two or more tables based on a related column between them (typically a primary key/foreign key relationship).

- **`INNER JOIN` (or just `JOIN`):** Returns only the rows where there is a match in _both_ tables.
    
    - **Easy:** Only show me data where there's a link on both sides.
        
    - **In-depth:** The most common join. If a patient has no admissions, or an admission has no matching patient, neither will appear.
        
    - **Example:** Get the patient name and their admission date.
        
        SQL
        
        ```
        SELECT p.patient_name, a.admission_date
        FROM patients AS p -- 'AS p' is an alias for brevity
        INNER JOIN admissions AS a ON p.patient_id = a.patient_id;
        ```
        
- **`LEFT JOIN` (or `LEFT OUTER JOIN`):** Returns all rows from the _left_ table, and the matching rows from the _right_ table. If there's no match on the right, `NULL` values are returned for the right table's columns.
    
    - **Easy:** Show me everything from the first table, and add info from the second if it exists.
        
    - **In-depth:** Useful when you want to see all patients, even those who have never been admitted.
        
    - **Example:** Get all patient names, and their admission dates if they have any.
        
        SQL
        
        ```
        SELECT p.patient_name, a.admission_date
        FROM patients AS p
        LEFT JOIN admissions AS a ON p.patient_id = a.patient_id;
        ```
        
- **`RIGHT JOIN` (or `RIGHT OUTER JOIN`):** The opposite of `LEFT JOIN`. Returns all rows from the _right_ table, and matching rows from the _left_.
    
- **`FULL OUTER JOIN`:** Returns all rows when there is a match in one of the tables. If there's no match, `NULL` is used. (Less common in MySQL).
    

## 5. Aggregation Functions & `GROUP BY`/`HAVING`:

- **Aggregation Functions:** Perform calculations on a set of rows and return a single summary value.
    
    - **`COUNT()`:** Counts rows. `COUNT(*)` counts all rows; `COUNT(column_name)` counts non-NULL values.
        
        - **Example:** `SELECT COUNT(*) FROM patients;` (Total patients)
            
    - **`SUM()`:** Calculates the sum of a numeric column.
        
    - **`AVG()`:** Calculates the average of a numeric column.
        
    - **`MIN()`:** Finds the minimum value in a column.
        
    - **`MAX()`:** Finds the maximum value in a column.
        
- **`GROUP BY` Clause:** Groups rows that have the same values in specified columns into summary rows, typically with aggregate functions.
    
    - **Easy:** Group my data by a specific category (e.g., gender, doctor, hospital) and then summarize each group.
        
    - **In-depth:** All columns in the `SELECT` list that are _not_ part of an aggregate function _must_ be in the `GROUP BY` clause.
        
    - **Example:** Count how many patients of each gender.
        
        SQL
        
        ```
        SELECT gender, COUNT(*) AS number_of_patients
        FROM patients
        GROUP BY gender;
        ```
        
- **`HAVING` Clause:** Filters groups created by the `GROUP BY` clause. It's like `WHERE`, but for groups.
    
    - **Easy:** Filter the summarized groups based on some condition.
        
    - **In-depth:** `WHERE` filters _rows_ before grouping; `HAVING` filters _groups_ after grouping and aggregation.
        
    - **Example:** Find genders with more than 10 patients.
        
        SQL
        
        ```
        SELECT gender, COUNT(*) AS number_of_patients
        FROM patients
        GROUP BY gender
        HAVING COUNT(*) > 10;
        ```
        

## 6. Subqueries (Nested Queries):

A query nested inside another SQL query.

- **Easy:** Use the result of one query as input for another.
    
- **In-depth:** Can be used in `SELECT`, `FROM`, `WHERE`, `INSERT`, `UPDATE`, `DELETE` clauses. Can return a single value, a list of values, or a table.
    
- **Example:** Find patients who have been admitted.
    
    SQL
    
    ```
    SELECT patient_name
    FROM patients
    WHERE patient_id IN (SELECT DISTINCT patient_id FROM admissions);
    ```
    

## 7. `UNION` Operator:

Combines the result sets of two or more `SELECT` statements into a single result set.

- **Easy:** Stack results from different queries on top of each other.
    
- **In-depth:**
    
    - All `SELECT` statements within the `UNION` must have the same number of columns.
        
    - The columns must have similar data types.
        
    - The columns must be in the same order.
        
    - `UNION` (default) removes duplicate rows. `UNION ALL` keeps all rows, including duplicates.
        
- **Example (Conceptual for your schema):** List all names that appear as either a `patient_name` or a `doctor_name`.
    
    SQL
    
    ```
    SELECT patient_name AS Name FROM patients
    UNION ALL
    SELECT doctor_name AS Name FROM doctors;
    ```
    

## 8. Comments:

Used to add notes within SQL code, which are ignored by the database.

- **Single-line:** `-- This is a comment` (MySQL, PostgreSQL, SQL Server) or `# This is a comment` (MySQL).
    
- **Multi-line:** `/* This is a multi-line comment */`
    

