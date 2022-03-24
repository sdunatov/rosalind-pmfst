def HammingDistance(dna1, dna2):
  li = []
  for i in range(len(dna1)):
    if dna1[i] != dna2[i]:
      li.append(dna1[i])
  return len(li)

def PatternMatching(pattern, text, d):
  pos = []
  for i in range(len(text) - len(pattern) + 1):
    if HammingDistance(pattern, text[i:len(pattern)+i]) <= d:
      pos.append(i)
      
  position = " ".join(map(str, pos))
  return position
