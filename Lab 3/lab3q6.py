import csv
with open('G:\Downloads\data.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row)