def ChromosomeToCycle(chromosome):
  cycle = []
  for el in chromosome:
    if el > 0:
      cycle.append(2 * el - 1) #tail
      cycle.append(2 * el) #head
    else:
      cycle.append(-2 * el) #head
      cycle.append(-2 * el-1) #tail
  return cycle


def ColoredEdges(P):
  obojenibridovi = []
  for kromosom in P:
    nodes = ChromosomeToCycle(kromosom) #svaki kromosom pretvorimo u ciklus
    for i in range(1, len(nodes), 2):
      if i != len(nodes) - 1:
        obojenibridovi.append([nodes[i], nodes[i+1]]) #svaki obojeni brid je jedan dvoclani niz
      else:
        obojenibridovi.append([nodes[i], nodes[0]])
  return obojenibridovi



def NadiSljedeci(trenutni, edges):
  if len(edges) == 0:
    return -1 #nemamo vise obojenih bridova
  idx = 0  #pocinjemo trazit ciklus od prvog obojenog brida iz niza
  while not(trenutni[0] in edges[idx] or trenutni[1] in edges[idx]):
    idx += 1
    if idx == len(edges):
      return -1 #tad smo dosli do kraja ciklusa
  return edges[idx]


def TwoBreakDistance(P, Q):
  P = P[1:-1]
  P = P.split(')(')
  for i in range(len(P)):
    P[i] = [int(x) for x in P[i].split(' ')]

  Q = Q[1:-1]
  Q = Q.split(')(')
  for i in range(len(Q)):
    Q[i] = [int(x) for x in Q[i].split(' ')]
  

  edgesP = ColoredEdges(P) #crveni
  edgesQ = ColoredEdges(Q) #plavi
  edges = edgesP + edgesQ #oboje

  blocks = set() #synteny blocks
  cycles = [] # obojani ciklusi u breakpointgraph

  for edge in edges: 
    blocks.add(edge[0])
    blocks.add(edge[1]) #ovako pokupimo sve synteny blokove ali uduplo

  while len(edges) != 0:
    start = edges[0]
    edges.remove(edges[0])
    ciklus = [start]

    current = NadiSljedeci(start, edges)
    while current != -1:
      ciklus.append(current)
      edges.remove(current)
      current = NadiSljedeci(current, edges)
    cycles.append(ciklus)
  
  return len(blocks)//2 - len(cycles) #ovo po formuli
