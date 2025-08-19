-- writng a sql query to retrieve checkNumber, paymentData and amount from the payments table

SELECT * checkNumber, paymentData ,amount
FROM payments


--  sql to retrieve orderDate. requiredDate, and status that are currently in process fro orders table
-- sort in descending order of orderDate

SELECT * orderDate, requiredDate, paymentData, 
FROM orders
WHERE status = 'In process' 
ORDER BY orderDate DESC;


-- query to display firstName, lastName and email of employees whole job title is salesRep and order in descending order
-- of employeeNumber

SELECT * firstName, lastName,email 
FROM employees
WHERE jobTitle = 'salesRep '
ORDER BY employeeNumber DESC;


-- query to retrieve all columns and records from offices
SELECT * FROM offices

-- query to fetch productName and quantityinStock from products table÷ 
-- sort results in ascwnding order of buyPrice and limit output to 5records

SELECT * productName, quantityinStock
FROM products
ORDER BY buyPrice ASC
LIMIT 5;
