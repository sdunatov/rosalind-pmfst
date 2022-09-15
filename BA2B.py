from itertools import product

def HammingDistance(dna1, dna2):
  li = []
  for i in range(len(dna1)):
    if dna1[i] != dna2[i]:
      li.append(dna1[i])
  return len(li)

def Patterns(text, k):
  patterns = []
  for i in range(len(text) - k + 1):
    pattern = text[i:k+i]
    if (pattern not in patterns):
      patterns.append(pattern)
  return patterns

def PatternD(text, pattern, k):
  mini = k
  for pat in Patterns(text, k):
    distance = HammingDistance(pattern, pat)
    if distance < mini:
      mini = distance
  return mini

def DnaD(dna, pattern, k):
  suma = 0
  for i in range(len(dna)):
    suma = suma + PatternD(dna[i], pattern, k)
  return suma

def MedianString(k, dnaList):
  dna = []
  tempI = 0
  d = float('inf')
  median = ""

  #odvajanje dnaList u listu dna
  for i in range(len(dnaList)):
    if dnaList[i] == "\n":
      dna.append(dnaList[tempI:i])
      tempI = i + 1
  dna.append(dnaList[tempI:])

  all_k_mers = [''.join(i) for i in product('ACGT', repeat = k)]

  for kmer in all_k_mers:
    dnaD = DnaD(dna, kmer, k)
    if(dnaD < d):
      d = dnaD
      median = kmer
  
  return median
