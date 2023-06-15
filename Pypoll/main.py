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


csv_file_path = 'Resources/election_data.csv'
columns_to_read = ['Ballot ID', 'County', 'Candidate']

data = read_csv_columns(csv_file_path, columns_to_read)
# print(data)

total = len(data)

# Extract Candidate names
candidates = set()
for candidate in data:
  candidates.add(candidate['Candidate'])


# this function filters candidates and aggregates their votes into a dictionary
def filteredCandidates(candidates, data):
  x = dict()
  for can in candidates:
    x[can] = len(list(filter(lambda y: (y['Candidate'] == can), data)))
  return x


# This function calculates a percentage to 3 decimal places
def percentage(num, total, decimals=3):
  return round(num / total * 100, decimals)


# Aggregate votes by candidate
candidateResults = filteredCandidates(candidates, data)


# This function accepts candidate results and returns the winner tuple: Ex. (Person A, 10000)
def winner(candidatesResults):
  nums = list(candidateResults.values())
  index = nums.index(max(nums))
  # return index
  return list(candidateResults.items())[index]


with open("analysis/Pypoll.txt", "w") as text_file:
  print("Election Results", file=text_file)
  print("-------------------------", file=text_file)
  print(f"Total Votes: {total}", file=text_file)
  print("-------------------------", file=text_file)
  for candidate in candidateResults.items():
    print(
      f"{candidate[0]}: {percentage(candidate[1], total)}% ({candidate[1]})",
      file=text_file)
  print("-------------------------", file=text_file)
  print(f"Winner: {winner(candidateResults)[0]}", file=text_file)
  print("-------------------------", file=text_file)

# Dump file to console to verify results
with open("analysis/Pypoll.txt", 'r') as text_file:
  print(text_file.read())
