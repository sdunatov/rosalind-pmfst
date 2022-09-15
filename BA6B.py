def Breakpoint(p):
  p = p.strip("()")
  p = p.split(" ")
  p1 = []
  counter = 0

  for br in p:
    p1.append(int(br))

  produzeni_p = [0]  + p1 + [len(p1) + 1]
  for i in range(len(p1)):
    if(produzeni_p[i+1] != produzeni_p[i] + 1):
      counter += 1

  return counter
