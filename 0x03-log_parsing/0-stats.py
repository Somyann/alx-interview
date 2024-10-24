import sys

#!/usr/bin/python3

total_size = 0
status_codes = {
  "200": 0,
  "301": 0,
  "400": 0,
  "401": 0,
  "403": 0,
  "404": 0,
  "405": 0,
  "500": 0
}

def print_stats():
  print("File size: {}".format(total_size))
  for code in sorted(status_codes.keys()):
    if status_codes[code] > 0:
      print("{}: {}".format(code, status_codes[code]))

line_count = 0

try:
  for line in sys.stdin:
    parts = line.split()
    if len(parts) < 7:
      continue

    ip, _, _, date, _, request, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]

    try:
      total_size += int(file_size)
    except ValueError:
      continue

    if status_code in status_codes:
      status_codes[status_code] += 1

    line_count += 1

    if line_count % 10 == 0:
      print_stats()

except KeyboardInterrupt:
  print_stats()
  raise

print_stats()