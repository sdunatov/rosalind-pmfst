def FrequentWords(text, k):
  frequentPatterns = []
  d = dict()

  for i in range(len(text) - k  + 1):
    pattern = text[i:k+i]
    if pattern in d:
      d[pattern] = d[pattern] + 1
    else:
      d[pattern] = 1
      
  maxCount = max(d.values())

  for x in d.items():
    if x[1] == maxCount:
      frequentPatterns.append(x[0])
  return frequentPatterns
