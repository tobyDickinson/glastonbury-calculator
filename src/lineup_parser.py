import csv

def parse_lineup_csv(path: str):
  file = open(path)
  reader = csv.reader(file)
  rows = []
  for row in reader:
    rows.append(row)

  return rows