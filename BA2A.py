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
  return set(neighborhood)

def PojavljujeSeUDna(k, d, pattern, dna):
  sadrzi = {}
  s = 0
  for i in range(len(dna)):
    for j in range(len(dna[i]) - k + 1):
      Pattern = dna[i][j:k+j]
      if(HammingDistance(Pattern, pattern) <= d):
        sadrzi[s] = 1
    s += 1
  
  if(sum(sadrzi.values()) == len(dna)):
    return True
  else:
    return False

def Patterns(text, k):
  patterns = []
  for i in range(len(text) - k + 1):
    pattern = text[i:k+i]
    if (pattern not in patterns):
      patterns.append(pattern)
  return patterns
    
def MotifEnumeration(k, d, dnaList):
  dna = []
  tempI = 0
  
  #odvajanje dnaList u listu dna
  for i in range(len(dnaList)):
    if dnaList[i] == "\n":
      dna.append(dnaList[tempI:i])
      tempI = i + 1
  dna.append(dnaList[tempI:])

  motifs = set()
  for text in dna:
    for pattern in Patterns(text, k):
      for neighbor in Neighborhood(pattern, d):
        if PojavljujeSeUDna(k, d, neighbor, dna):
          motifs.add(neighbor)

  res = " ".join(map(str, motifs))
  return res
