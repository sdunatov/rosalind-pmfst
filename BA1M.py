def NumberToSymbol(indeks):
  symbol = ""

  if indeks == 0:
    symbol = "A"
  if indeks == 1:
    symbol = "C"
  if indeks == 2:
    symbol = "G"
  if indeks == 3:
    symbol = "T"

  return symbol



def NumberToPattern(indeks, k):
  if k == 1:
    return NumberToSymbol(indeks)
 
  prefixIndex = indeks // 4
  r = indeks % 4
  symbol = NumberToSymbol(r)
  prefixPattern = NumberToPattern(prefixIndex, k - 1)

  return prefixPattern + symbol
