from collections import Counter

def EulerianCycle(D, end):
  pocetni = list(D.keys())[0]
  trenutni = pocetni
  ciklus = [pocetni]

  while D:
    if trenutni in D:
      ciklus.append(D[trenutni][0])
      if len(D[trenutni]) == 1:
        del D[trenutni]
      else:
        del D[trenutni][0]
      trenutni = ciklus[-1]
    else:
      for i,el in enumerate(ciklus):
        if el in D:
          noviciklus = ciklus[i:-1] + ciklus[:i+1]
          ciklus = noviciklus
          trenutni = el #taj element koji ima neiskoristenih bridova => iz njega nastavi trazit
          break
  return ciklus

def AddImaginaryEdge(D):
  ulazni = Counter()
  izlazni = Counter()

  for key, value in D.items():
    izlazni[key] += len(value)
    for v in value: 
      ulazni[v] += 1
  
  start = list(ulazni - izlazni)[0]
  end = list(izlazni - ulazni)[0]

  D[start] = [end]
  return start, end


def EulerianPath(adjacency_list):
  D = {}
  put = []
  adj_list = adjacency_list.split('\n')
  for edge in adj_list:
      first, second = edge.split(" -> ")
      second = second.split(",")
      D[first] = second

  start, end = AddImaginaryEdge(D)
  ciklus = EulerianCycle(D, end)[1:]
  
  for i in range(len(ciklus)):
    if ciklus[i] == start and ciklus[i+1] == end:
      put.append(ciklus[i+1:] + ciklus[:i+1])

  for i in range(len(put)):
    for j in range(len(put[i])):
      res = "->".join(put[i])

  return res
