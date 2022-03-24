def PatternToNumber(pattern):
    symbolToNumber = 0

    if pattern == "":
      return 0

    symbol = pattern[-1]
    prefix = pattern[:-1]

    if symbol == "A":
      symbolToNumber = 0
    if symbol == "C":
      symbolToNumber = 1
    if symbol == "G":
      symbolToNumber = 2
    if symbol == "T":
      symbolToNumber = 3
    
    return 4 * PatternToNumber(prefix) + symbolToNumber
