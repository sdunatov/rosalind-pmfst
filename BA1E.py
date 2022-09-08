def FrequentWords1(text, k, t):
  frequentPatterns = []
  d = dict()

  for i in range(len(text) - k  + 1):
    pattern = text[i:k+i]
    if pattern in d:
      d[pattern] = d[pattern] + 1
    else:
      d[pattern] = 1 
  for x in d.items():
    if x[1] == t:
      frequentPatterns.append(x[0])
  return frequentPatterns

def ClumpFinding(genome, k, L, t):
  li = []
  nova = []
  nova1 = []

  for i in range(len(genome) - L + 1):
    cl = FrequentWords1(genome[i:L+i], k, t)
    li.append(cl)

  for i in range(len(li)):
    for j in range(len(li[i])):
      nova.append(li[i][j])

  for el in nova:
    if el in nova1:
      continue
    else:
      nova1.append(el)
  nova1.sort()
  rez = " ".join(nova1)
  return rez
