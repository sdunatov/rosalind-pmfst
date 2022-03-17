def count(text, pattern):
  li = []
  br = 0
  for i in range(len(text)-len(pattern)+1):
    li.append(text[i:len(pattern)+i])
  for el in li:
    if el == pattern:
      br += 1
  return br
