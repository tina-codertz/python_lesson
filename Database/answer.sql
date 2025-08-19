-- create a new dataabse called SalesDB--
CREATE DATABASE SalesDB;

-- drop the database called demo --
DROP DATABASE demo;

-- understanding the use of SELECT statement
-- select statement is the tool for interacting with your database and retrieving the data you need

SELECT * FROM Customers;

SELECT * FROM data_table_name;
-- this will select all columns from the table named data_table_name

-- retriving specific columns
SELECT first_name, last_name FROM Customers;

-- wilcards(%) for flexible searching
SELECT * FROM Customers WHERE first_name LIKE 'keywords%';
-- this query retrieves all records where the description 
-- contains a keyword anywhere in the text the % sysmbol acts as a wildcard matching any characters before or after the keyword

-- comparison operators for targeted filtering
SELECT * FROM Customers WHERE age > 30;
-- this query retrieves all records where the age is greater than 30

-- filtering by data range
SELECT * FROM Customers WHERE age BETWEEN 20 AND 30;
-- this query retrieves all records where the age is between 20 and 30, inclusive

-- combining techniques for powerful queries

SELECT first_name, last_name FROM Customers 
WHERE age > 30 AND first_name LIKE 'A%';
-- this query retrieves first and last names of customers older than 30 whose first name starts with 'A'

SELECT * FROM products
WHERE name LIKE '%pro%' AND price >= 50;

-- filtering data with precision 
-- understaing the WHERE clause

SELECT * column1, column2
FROM data_table_name WHERE condition:

-- the where clause follows the form clause and sets criteria for data retrieval
-- its like a sieve letting only the relevant data through

-- using comparison operators within where
SELECT * FROM transactions
WHERE amount > 100;

-- filtering by data range
SELECT * FROM events WHERE event_date BETWEEN '2023-01-01' AND '2023-12-31';

-- logical operators for complex conditions
-- AND:combine conditions OR:retrieve records meeting one or more conditions,NOT:exclude specific data points operators

SELECT * FROM users
WHERE age > 18 AND country = 'USA';

-- combining techniques for granular control
SELECT * FROM products WHERE name LIKE '%pro%' AND price >= 50
OR category = 'electronics';