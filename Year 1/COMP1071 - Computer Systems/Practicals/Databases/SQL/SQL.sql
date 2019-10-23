-- Q1
 SELECT staffNo,fName,sName,salary FROM staff;
 SELECT staffNo,sName FROM staff WHERE salary>9000;
 SELECT * FROM staff;
 SELECT fName FROM staff;
 SELECT DISTINCT fName FROM staff;
 SELECT sName, salary/12 FROM staff;
 SELECT staffNo FROM staff WHERE salary<10000;
-- Q2 SELECT
SELECT customerid, item, price FROM staff WHERE customerid=10449;
SELECT * FROM staff WHERE item=tent;
SELECT customerid, order_date, item WHERE SUBSTRING(item,1,1)=S;
SELECT DISTINCT * FROM items_ordered;
-- Q2 AGGREGATE
SELECT MAX(price) FROM items_ordered;
SELECT AVG(price) FROM items_ordered WHERE order_date=*Dec*;
SELECT COUNT(*) FROM items_ordered;
SELECT MIN(price) FROM items_ordered WHERE item=Tent;
-- Q2 GRPUP BY
SELECT state,COUNT(*) FROM customers GROUP BY state;
-- ORDER BY
SELECT lastname, firstname, city FROM customers ORDER BY lastname;
-- Combining Conditions and Boolean Operators
SELECT customerid, order_date, item FROM items_ordered WHERE item!=Snow shoes OR Ear Muffs
-- Table Join
SELECT customers.customerid,customers.firstname, customers.lastname,
 items_ordered.customerid,items_ordered.order_date, items_ordered.item, items_ordered.price
 FROM customers,items_ordered
INNER JOIN customers ON customers.customerid=items_ordered.customerid;
