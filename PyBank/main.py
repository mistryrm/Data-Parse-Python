import csv


# This function reads a CSV file and outputs it as a list
def read_csv_columns(csv_file, columns):
  with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    result = []

    for row in reader:
      column_data = {column: row[column] for column in columns}
      result.append(column_data)

  return result


# This function finds differences between Profit/Losses and outputs the differences as a list
def getDifferences(itr):
  result = []
  start = 0
  end = 1
  while end < len(itr):
    num1 = int(itr[start]['Profit/Losses'])
    num2 = int(itr[end]['Profit/Losses'])
    finNum = num2 - num1
    result.append(finNum)
    start += 1
    end += 1
  return result


csv_file_path = 'Resources/budget_data.csv'
columns_to_read = ['Date', 'Profit/Losses']

# csv as a list
column_data = read_csv_columns(csv_file_path, columns_to_read)

# get total months
total = 0
for num in column_data:
  total += int(num['Profit/Losses'])

# get the difference between each month
priceChanges = getDifferences(column_data)

# get maximum diff
maxPriceDiff = max(priceChanges)

# get minimum diff
minPriceDiff = min(priceChanges)

# average price changes, rounded to 2 decimal points
avgPriceChanges = round(sum(priceChanges) / len(priceChanges), 2)

#Greated increase month
greatestIncreaseMonth = column_data[priceChanges.index(maxPriceDiff) +
                                    1]['Date']

# Greatest Decrease month
greatestDecreaseMonth = column_data[priceChanges.index(minPriceDiff) +
                                    1]['Date']

# output to file
with open("analysis/PyBank.txt", "w") as text_file:

  print("Financial Analysis", file=text_file)
  print("------------------------", file=text_file)
  print("Total Months: ", len(column_data), file=text_file)
  print(f"Total: ${total}", file=text_file)
  print(f"Average change: ${avgPriceChanges}", file=text_file)
  print(
    f"Greatest Increase in Profits: {greatestIncreaseMonth} (${maxPriceDiff})",
    file=text_file)
  print(
    f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${minPriceDiff})",
    file=text_file)

# Dump file to console to verify results
with open("analysis/PyBank.txt", 'r') as text_file:
  print(text_file.read())
