import csv

import src.lineup_parser as lineup_parser


def test_lineup_parser():
  raw_lineup_path = '__tests__/assets/short-lineup-raw.csv'
  parsed_lineup_path = '__tests__/assets/short-lineup-parsed.csv'
  parsed_lineup_file = open(parsed_lineup_path)
  expected_parsed_rows = []
  for row in csv.reader(parsed_lineup_file):
    expected_parsed_rows.append(row)

  parsed_rows = lineup_parser.parse_lineup_csv(raw_lineup_path)

  assert parsed_rows == expected_parsed_rows  
