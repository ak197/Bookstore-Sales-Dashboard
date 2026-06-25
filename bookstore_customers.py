# Step 1: Build CustomerID -> City dict
customer_dict = {}
with open('customers.csv', 'r') as f:
    customer_rows = f.readlines()

for row in customer_rows[1:]:
    cols = row.split(',')
    customer_id = cols[0] # CustomerID
    city = cols[2].strip() # City is column 2
    customer_dict[customer_id] = city

print("Cities loaded:", len(customer_dict))

# Step 2: Read sales.csv and group revenue by SaleDate
with open('sales.csv', 'r') as f:
    data_rows = f.readlines()

daily_revenue = {} # {date: total_revenue}
customer_city_by_date = {} # {date: [list of cities]}

for row in data_rows[1:]:
    cols = row.split(',')
    date = cols[1] # SaleDate
    customer_id = cols[3] # CustomerID is column 3
    revenue = float(cols[6]) # Revenue is column 6
    city = customer_dict.get(customer_id, "Unknown")

    if date not in daily_revenue:
        daily_revenue[date] = 0
        customer_city_by_date[date] = []

    daily_revenue[date] += revenue
    customer_city_by_date[date].append(city)

# Step 3: Sort dates and find drops with LAG
sorted_dates = sorted(daily_revenue.keys())
prev = float(daily_revenue[sorted_dates[0]])
city_drops = {}

for date in sorted_dates[1:]:
    total = float(daily_revenue[date])
    if total < prev:
        # Get cities for this date
        cities_today = customer_city_by_date[date]
        for city in cities_today:
            if city not in city_drops:
                city_drops[city] = []
            city_drops[city].append(date)
    prev = total

# Step 4: Sort and export
sorted_drops = sorted(city_drops.items(), key=lambda x: len(x[1]), reverse=True)

with open('sales_drops_by_city.csv', 'w') as f:
    f.write('City,Drop_Count,Drop_Dates\n')
    for city, dates in sorted_drops:
        dates_str = "; ".join(dates)
        f.write(f'{city},{len(dates)},"{dates_str}"\n')

print("Report saved as sales_drops_by_city.csv")