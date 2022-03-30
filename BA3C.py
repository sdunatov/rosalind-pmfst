def OverLap(patterns):
  patterns = patterns.split("\n")
  k = len(patterns[0])
  for i in range(len(patterns)):
    first = patterns[i]
    for j in range(len(patterns)):
      second = patterns[j]
      if first[1:] == second[:k-1]:
        print(first + " -> " + second)
  return
