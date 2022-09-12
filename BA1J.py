from itertools import product

#dodano u odnosu na prethodni zadatak
def Reverse(dna):
  dnaList = []
  complement = []
  reverse = dna[::-1]

  for i in range(len(reverse)):
    dnaList.append(reverse[i])

  for el in dnaList:
    if el == "A":
      complement.append("T")
    if el == "C":
      complement.append("G")
    if el == "T":
      complement.append("A")
    if el == "G":
      complement.append("C")

  reverseComplement = "".join(complement)
  return reverseComplement

def MisAndReverse(text, k, d):
  trenutni_k_mers = []
  svi_najcesci = []
  frequentPatterns = []

  all_k_mers = [''.join(i) for i in product('ACGT', repeat = k)]
  for i in range(len(text) - k + 1):
    trenutni_k_mers.append(text[i:k+i])
    #dodano u odnosu na prethodni zadatak
    trenutni_k_mers.append(Reverse(text[i:k+i]))
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
