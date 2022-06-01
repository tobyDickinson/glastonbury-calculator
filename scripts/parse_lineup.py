import csv

from src.lineup_parser import parse_lineup_csv

LINEUP_FILEPATH = 'infile/glastonbury-lineup-2022-raw.csv'
OUT_FILEPATH = 'infile/glastonbury-lineup-2022-parsed.csv'

parsed_lineup = parse_lineup_csv(LINEUP_FILEPATH)

outfile = open(OUT_FILEPATH, 'w')
csv_writer = csv.writer(outfile)
for row in parsed_lineup:
  csv_writer.writerow(row)
