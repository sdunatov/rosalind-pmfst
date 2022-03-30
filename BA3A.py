def Composition(k, text):
  li = []
  for i in range(len(text) - k + 1):
    li.append(text[i:k+i])
  li.sort()
  for el in li:
    print(el)
  return
