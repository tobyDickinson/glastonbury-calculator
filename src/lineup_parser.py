import csv

DAYS = ["WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

def parse_lineup_csv(path: str) -> list:
  file = open(path)
  reader = csv.reader(file)
  rows = []
  for row in reader:
    rows.append(row)

  current_stage = rows[0][0]
  current_day = rows[1][0]

  parsed_rows = []
  for row in rows[2:]:
    if row[0] in DAYS:
      current_day = row[0]
    elif row[1] == '':
      current_stage = row[0]
    else:
      parsed_rows.append(parse_row(current_day, current_stage, row))
  
  return parsed_rows

def parse_row(day, stage, row: list[str]) -> str:
  [start_time, end_time] = row[1].split(' - ')

  return [row[0], start_time, end_time, day, stage]