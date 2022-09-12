from itertools import product

def HammingDistance(dna1, dna2):
  li = []
  for i in range(len(dna1)):
    if dna1[i] != dna2[i]:
      li.append(dna1[i])
  return len(li)
  
def Mis(text, k, d):
  trenutni_k_mers = []
  svi_najcesci = []
  frequentPatterns = []

  all_k_mers = [''.join(i) for i in product('ACGT', repeat = k)]
  for i in range(len(text) - k + 1):
    trenutni_k_mers.append(text[i:k+i])
  for i in range(len(trenutni_k_mers)):
    for j in range(len(all_k_mers)):
      if HammingDistance(trenutni_k_mers[i], all_k_mers[j]) <= d:
        svi_najcesci.append(all_k_mers[j])

  d = dict()
  for el in svi_najcesci:
    if el in d:
      d[el] = d[el] + 1
    else:
      d[el] = 1
      
  maxCount = max(d.values())

  for x in d.items():
    if x[1] == maxCount:
      frequentPatterns.append(x[0])
  

  res = " ".join(map(str, frequentPatterns))
  return res
