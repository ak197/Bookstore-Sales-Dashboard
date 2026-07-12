/*=======================================================


Project: Bookstore Sales Analysis - SQL Script
Author: Ankita
Date: 28 May 2026  
Database: SQLite | Schema: Books, Customers, Sales
Purpose: Deloitte DA Portfolio Project 1 - Business Insights
Total Queries: 6 | Status: Complete


KEY BUSINESS INSIGHTS - 28 MAY 2026

1. TOP MONTH: 2024-01 generated ₹2397 revenue. Q1 stronger than Q2.
   Action: Stock up in Dec for Jan peak.

2. #1 CUSTOMER: Ananya Das, Kolkata, ₹1948 total spend. 
   Top 5 customers = 4 from Kolkata. 
   Action: Kolkata is VIP city. Run targeted campaign.

3. DISCOUNT VERDICT: High discount ≠ high volume. 
   History avg 50% discount → 1.0 qty. Self-Help 18.75% → highest revenue.
   Action: Reduce History/Finance discounts. Promote Self-Help at current price.

-- =======================================================*/

-- DAY 1 QUERIES
-- Q1: Revenue by Genre
SELECT b.Genre, SUM(s.Revenue) AS TotalRevenue, SUM(s.Quantity) AS BooksSold
FROM Sales s JOIN Books b ON s.BookID = b.BookID 
GROUP BY b.Genre ORDER BY TotalRevenue DESC;

-- Q2: All Books with Sales incl 0 sales  
SELECT b.Title, COALESCE(SUM(s.Revenue), 0) AS TotalRevenue
FROM Books b LEFT JOIN Sales s ON b.BookID = s.BookID 
GROUP BY b.Title ORDER BY TotalRevenue ASC;

-- Q3: Revenue by City + Genre for Kolkata
SELECT b.Genre, c.City, SUM(s.Revenue) AS CityGenreRevenue
FROM Sales s JOIN Books b ON s.BookID = b.BookID 
JOIN Customers c ON s.CustomerID = c.CustomerID 
WHERE c.City = 'Kolkata' GROUP BY b.Genre, c.City ORDER BY CityGenreRevenue DESC;

-- DAY 2 QUERIES
-- Q4: Total Revenue by Month
SELECT STRFTIME('%Y-%m', s.SaleDate) AS SalesMonth, SUM(s.Revenue) AS MonthlyRevenue, COUNT(s.SaleID) AS OrdersCount
FROM Sales s GROUP BY STRFTIME('%Y-%m', s.SaleDate) ORDER BY SalesMonth ASC;

-- Q5: Top 5 Customers by Total Spend
SELECT c.CustomerID, c.Name, c.City, COUNT(s.SaleID) AS TotalOrders, SUM(s.Revenue) AS TotalSpent
FROM Customers c JOIN Sales s ON c.CustomerID = s.CustomerID 
GROUP BY c.CustomerID, c.Name, c.City ORDER BY TotalSpent DESC LIMIT 5;

-- Q6: Avg Discount vs Avg Qty by Genre
SELECT b.Genre, ROUND(AVG(s.Discount), 2) AS AvgDiscount, ROUND(AVG(s.Quantity), 1) AS AvgQtySold, SUM(s.Revenue) AS GenreRevenue
FROM Sales s JOIN Books b ON s.BookID = b.BookID 
GROUP BY b.Genre ORDER BY GenreRevenue DESC;

-- Q7: Detect Books with >50% Sales Drop MoM using LAG - SQLite Compatible
WITH MonthlySales AS (
  SELECT 
    b.Title,
    strftime('%Y-%m', s.SaleDate) AS SaleMonth, -- SQLite uses strftime instead of FORMAT
    SUM(s.Revenue) AS MonthlyRevenue
  FROM sales s
  JOIN books b ON s.BookID = b.BookID
  GROUP BY b.Title, strftime('%Y-%m', s.SaleDate)
),
SalesWithLag AS (
  SELECT 
    Title,
    SaleMonth,
    MonthlyRevenue,
    LAG(MonthlyRevenue) OVER (PARTITION BY Title ORDER BY SaleMonth) AS PrevMonthRevenue
  FROM MonthlySales
)
SELECT 
  Title,
  SaleMonth,
  MonthlyRevenue,
  PrevMonthRevenue,
  ROUND(100.0 * (MonthlyRevenue - PrevMonthRevenue) / PrevMonthRevenue, 2) AS DropPct
FROM SalesWithLag
WHERE PrevMonthRevenue IS NOT NULL 
  AND MonthlyRevenue < PrevMonthRevenue * 0.5
ORDER BY DropPct;