# Step 1: Read file FIRST - this creates 'sales' variable
with open('sales.csv', 'r') as f:
    sales = f.read()

# Step 2: NOW you can use 'sales'
lines = sales.split('\n')
header = lines[0] # Sale_ID,Book_ID,Customer_ID,Date,Qty,Total_Amount
data_rows = lines[1:] # skip header, take only data

# Step 3: Parse each row
for row in data_rows:
    cols = row.split(',') # split by comma
    print("Row:", cols) # see all columns
    print("Col 2:", cols[2], "Col 3:", cols[3]) # test both
    total = float(cols[5]) # Total_Amount is 6th column, index 5
    print(total) # test: see if amounts print

count = 0 # to store number of drops
drop_dates = [] # new list to store dates
prev = float(data_rows[0].split(',')[5]) # first day's sales
prev_date = data_rows[0].split(',')[1] # first day's date, index 3

for row in data_rows[1:]: # start from 2nd row
    cols = row.split(',')
    total = float(cols[5])
    date = cols[1] # Date column is 4th, index 3

    if total < prev: # sales dropped vs yesterday
        count += 1
        drop_dates.append(date) # save the date when drop happened

    prev = total # update for next comparison
    prev_date = date
print("Sales dropped", count, "times")   
print("Drop dates:", drop_dates) 