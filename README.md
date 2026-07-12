# Bookstore Sales Analytics | SQL + Python + Power BI

**Completed:** May 28, 2026 | **Last Updated:** July 12, 2026  
**Tools:** SQL, Power BI, DAX, Python - Built-in functions only  
**Domain:** Publishing & Retail Analytics | As a former Author, I analyzed what drives book sales

### Business Problem
Identify revenue drivers and inventory optimization opportunities for a bookstore with 1,500+ sales records. 
Goal: Find which Category, City, and Book caused the most revenue change and detect MoM sales drops using LAG logic.

### My Approach - 2 Versions

#### Version 1: SQL + Power BI | July 2026
1. **SQL ETL:** 7 queries using JOINs, aggregations, window functions, and date functions to clean data and calculate KPIs
2. **Power BI:** Interactive dashboard with DAX measures for revenue tracking and MoM % change
3. **Key Files:** `SQL_All_Queries_28May.sql`, `Bookstore_Dashboard_May2026.pbix`

#### Version 2: Pure Python ETL | Apr 2026 - No Pandas, No SQL
**Why this version?** Built to understand JOIN and ETL logic at the fundamental level using `split(',')` and dicts.
**Method:**
- Loaded 3 CSVs: sales.csv, customers.csv, books.csv
- Used Python dictionaries for JOINs
- Manual aggregation logic to find top genres and books
- Generated 2 visualizations using Matplotlib

### Key Insights & Results
1. **Top Revenue Driver:** Self-Help genre drives 37% of total revenue. `Atomic Habits` is #1 title at ~3.1K revenue
2. **Anomaly Detected:** Using SQL `LAG()` window function, flagged `Atomic Habits` with a **65.35% MoM sales drop** from Feb to Mar 2024
3. **Trend Analysis:** Overall revenue peaked in Jan 2024, dropped 25% by April, with slight recovery in June
4. **DAX Impact:** Built `MoM % Revenue Change = 4.96%` measure to track performance in Power BI

### Technical Skills Demonstrated
- **SQL:** JOINs, GROUP BY, CTEs, Window Functions `LAG()`, Date functions, Case statements
- **DAX:** Calculated Measures, MoM calculations, KPIs
- **Python:** ETL from scratch, data cleaning, Matplotlib for visualization
- **Power BI:** Data modeling, Interactive dashboard, Card visuals, Bar/Donut/Line charts

### Project Files
| File | Description |
| --- | --- |
| `SQL_All_Queries_28May.sql` | All 7 SQL queries including LAG analysis |
| `sales_drops_report.csv` | Output of Q7: Books with >20% sales drop |
| `bookstore_*.py` | Python scripts for ETL and analysis |
| `matplotlib_analysis.ipynb` | Jupyter notebook with 2 charts |
| `monthly_trend.png` | Line chart: Monthly revenue trend |
| `top10_books.png` | Bar chart: Top 10 books by revenue |
| `Bookstore_Dashboard_May2026.pbix` | Interactive Power BI Dashboard |
| `Ankita_Kundu_Data_Analyst.pdf` | Resume |

### Learnings
This was my first portfolio project. I started with basic SQL and joins, and progressed to advanced window functions and DAX. 
Building both SQL and Python versions helped me understand data transformation at every level.

### Next Steps
Project 1 of 3. Coming up: HR Attrition Analysis + Food Delivery Analysis
