
--1. Basic Queries and Filtering
-- List all tracks that cost more than $0.99
SELECT Name, UnitPrice
FROM tracks t
WHERE t.UnitPrice > 0.99;

--List all tracks with the word "Love" in their name
SELECT Name
FROM tracks t
WHERE Name LIKE '%Love%';

--Show all employees who are sales agents
SELECT e1.FirstName || ' ' || e1.LastName AS "Employee Name"
FROM employees e1
WHERE e1.Title = "Sales Support Agent";

--2. Advanced Filtering and Sorting
--List all tracks between 5 and 10 minutes
SELECT Name, Milliseconds
FROM tracks t
WHERE Milliseconds BETWEEN 300000 AND 600000;

--Find all customers whose first name starts with A and sort them by country
SELECT FirstName, Country
FROM customers c
WHERE c.FIRSTNAME LIKE 'A%'
ORDER BY Country ASC;

--List all invoices from 2009, sorted by total amount (highest to lowest)
SELECT InvoiceId, InvoiceDate, Total
FROM invoices i
WHERE i.InvoiceDate LIKE '2009%'
ORDER BY i.Total DESC;

--3.Aggregation and Grouping
--Find total number of tracks in each album
SELECT a.Title as Album_title, COUNT(*) as total_tracks
FROM tracks t, albums a 
JOIN albums a2 ON t.AlbumId = a.AlbumId
GROUP BY a.Title
ORDER BY total_tracks DESC;

--Show total sales amount for each country
SELECT BillingCountry, COUNT(*) as total_orders, ROUND(SUM(Total),2) as total_sales
FROM invoices i
GROUP BY BillingCountry
ORDER BY total_sales DESC;

--4 Multiple table operations
--Show all albums with their aritst names
SELECT albums.Title as Album_Title, artists.Name as Artist_Name
FROM albums 
RIGHT JOIN Artists ON Albums.ArtistId = Artists.ArtistId;


--List all tracks with their album name, genre, and media type
SELECT t.Name as TrackName,
a.Title as AlbumTitle,
g.Name as Genre,
m.Name as MediaType
FROM tracks t 
JOIN albums a ON t.AlbumId = a.AlbumId
JOIN genres g ON t.GenreId = g.GenreId
JOIN media_types m ON t.MediaTypeId = m.MediaTypeId;

--Show the total numner of tracks purchased by each customer
SELECT c.FirstName || ' ' || c.LastName as 'Customer Name', 
COUNT(ii.TrackId) as total_tracks
FROM customers c
join invoices i on c.CustomerId  = i.CustomerId  
join invoice_items ii on i.InvoiceId  = ii.InvoiceId  
group by c.CustomerId
ORDER BY c.FirstName;
