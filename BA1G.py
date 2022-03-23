def HammingDistance(dna1, dna2):
  li = []
  for i in range(len(dna1)):
    if dna1[i] != dna2[i]:
      li.append(dna1[i])
  return len(li)
