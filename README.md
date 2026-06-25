# Bookstore Sales Analytics | SQL + Python + Power BI

**Completed:** May 29, 2026 | **Updated:** Apr 2026  
**Tools:** SQL, Power BI, DAX, Python - Built-in functions only

### Business Problem
Identify revenue drivers and inventory optimization opportunities for a bookstore with 1,000+ sales records. Find which Category, City, and Book caused the most sales drops using LAG logic.

### My Approach - 2 Versions

#### Version 1: SQL + Power BI | May 2026
1. **SQL ETL:** 6 queries using JOINs, aggregations, and date functions to clean data and calculate KPIs
2. **Power BI:** Interactive dashboard with DAX measures for revenue tracking
3. **Files:** `SQL_All_Queries_28May.sql`, `Bookstore_Dashboard_May2026.pbix`

#### Version 2: Pure Python ETL | Apr 2026 - No Pandas, No SQL
**Why this version?** Built to understand LAG logic and JOINs at the fundamental level using `split(',')` and dicts.

**Method:** 
- Loaded 3 CSVs: sales.csv, customers.csv, books.csv
- Used Python dictionaries for JOINs 
- Manual LAG logic: compared current day revenue vs previous day
- Flagged drops without any libraries

**Files:** See `/Python_No_Pandas/` folder

### Key Insights

**From Power BI/SQL version:**
- Self-Help drives 37.5% revenue despite History 50% avg discount
- Jan 2024 peak ₹2,397 - recommend Dec stock-up
- Kolkata VIP city - 4 of the top 5 customers, including Ananya Das ₹1,948
- Flagged 75% MoM decline in July 2024 for investigation

**From Pure Python version:**
- **6 total sales drops** detected across all dates using LAG comparison
- **The Alchemist: 3 drops** - most volatile product
- **Kolkata: 9 drops** - most volatile city  
- **Fiction category:** most drops overall

### Files & Folder Structure
├── SQL_All_Queries_28May.sql           - ETL queries with business insights
├── Bookstore_Dashboard_May2026.pbix    - Interactive Power BI source
├── Bookstore_Dashboard_May2026.png     - Dashboard screenshot
└── Python_No_Pandas/                   - Pure Python implementation
    ├── bookstore_sales.py              - Category drop analysis + LAG
    ├── bookstore_customers.py          - City drop analysis + JOIN
    ├── bookstore_products.py           - Book drop analysis + JOIN
    ├── sales_drops_report.csv          - Category results
    ├── sales_drops_by_city.csv         - City results
    └── sales_drops_by_book.csv         - Book results

### Skills Demonstrated
**SQL:** JOINs, Window Functions/LAG, Aggregations, Date functions  
**Python:** File I/O, Dicts for JOINs, List sorting, String parsing, Manual ETL  
**Power BI:** DAX measures, Dashboard design, Data modeling  
**Business:** Identified revenue drivers, flagged volatility, and gave stock recommendations

### Contact
ankitakundu1190@gmail.com    
