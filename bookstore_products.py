# Step 1: Build BookID -> Title dict from books.csv
book_dict = {}
with open('books.csv', 'r') as f:
    book_rows = f.readlines()

for row in book_rows[1:]:
    cols = row.split(',')
    book_id = cols[0] # BookID
    title = cols[1].strip() # Title is column 1
    book_dict[book_id] = title

print("Books loaded:", len(book_dict))

# Step 2: Read sales.csv and group revenue by SaleDate + BookID
with open('sales.csv', 'r') as f:
    data_rows = f.readlines()

daily_revenue_by_book = {} # {date: {book_id: revenue}}

for row in data_rows[1:]:
    cols = row.split(',')
    date = cols[1] # SaleDate
    book_id = cols[2] # BookID is column 2
    revenue = float(cols[6]) # Revenue is column 6

    if date not in daily_revenue_by_book:
        daily_revenue_by_book[date] = {}

    if book_id not in daily_revenue_by_book[date]:
        daily_revenue_by_book[date][book_id] = 0

    daily_revenue_by_book[date][book_id] += revenue

# Step 3: Sort dates and find drops per BookID with LAG
sorted_dates = sorted(daily_revenue_by_book.keys())
prev_total = sum(daily_revenue_by_book[sorted_dates[0]].values())
book_drops = {}

for date in sorted_dates[1:]:
    current_total = sum(daily_revenue_by_book[date].values())
    if current_total < prev_total:
        # Which books sold on this drop date?
        books_today = daily_revenue_by_book[date]
        for book_id in books_today:
            title = book_dict.get(book_id, book_id)
            if title not in book_drops:
                book_drops[title] = []
            book_drops[title].append(date)
    prev_total = current_total

# Step 4: Sort and export
sorted_drops = sorted(book_drops.items(), key=lambda x: len(x[1]), reverse=True)

with open('sales_drops_by_book.csv', 'w') as f:
    f.write('Book_Title,Drop_Count,Drop_Dates\n')
    for title, dates in sorted_drops:
        dates_str = "; ".join(dates)
        f.write(f'{title},{len(dates)},"{dates_str}"\n')

print("Report saved as sales_drops_by_book.csv")