def CromosomeToCycle(seq):
  seq = seq.strip("()")
  seq = seq.split(" ")
  nodes = []
  chromosome = []
  st = ""

  for br in seq:
    chromosome.append(int(br))

  for i in range(len(chromosome)):
    if(chromosome[i] > 0):
      nodes.append(2 * abs(chromosome[i]) - 1)
      nodes.append(2 * abs(chromosome[i]))
    if(chromosome[i] < 0):
      nodes.append(2 * abs(chromosome[i]))
      nodes.append(2 * abs(chromosome[i]) - 1)
      
  for i in range(len(nodes)):
    st += str(nodes[i]) + " "
  st = st[:-1]
  res = "(" + st + ")"

  return res
