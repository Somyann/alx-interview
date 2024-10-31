#!/usr/bin/env python3

def validUTF8(data):
  # Number of bytes in the current UTF-8 character
  num_bytes = 0

  # Masks to check the most significant bits
  mask1 = 1 << 7
  mask2 = 1 << 6

  for num in data:
    mask = 1 << 7
    if num_bytes == 0:
      # Count the number of leading 1's in the first byte
      while mask & num:
        num_bytes += 1
        mask = mask >> 1

      # 1 byte characters
      if num_bytes == 0:
        continue

      # Invalid scenarios according to UTF-8 encoding
      if num_bytes == 1 or num_bytes > 4:
        return False
    else:
      # Check if the byte is a valid continuation byte
      if not (num & mask1 and not (num & mask2)):
        return False

    num_bytes -= 1

  return num_bytes == 0