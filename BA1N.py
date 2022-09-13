from itertools import product

def HammingDistance(dna1, dna2):
  li = []
  for i in range(len(dna1)):
    if dna1[i] != dna2[i]:
      li.append(dna1[i])
  return len(li)

def Neighborhood(dna, d):
  all_k_mers = [''.join(i) for i in product('ACGT', repeat = len(dna))]
  neighborhood = []
  for i in range(len(all_k_mers)):
    if HammingDistance(all_k_mers[i], dna) <= d:
      neighborhood.append(all_k_mers[i])

  for el in neighborhood:
    print(el)
  return 
