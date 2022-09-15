def CycleToCromosome(seq):
  seq = seq.strip("()")
  seq = seq.split(" ")
  nodes = []
  chromosome = []
  st = ""

  for br in seq:
    nodes.append(int(br))

  for i in range(len(nodes)):
    if(nodes[i] > 0):
      chromosome.append(2 * abs(nodes[i]) - 1)
      chromosome.append(2 * abs(nodes[i]))
    if(nodes[i] < 0):
      chromosome.append(2 * abs(nodes[i]))
      chromosome.append(2 * abs(nodes[i]) - 1)
      
  for i in range(len(chromosome)):
    st += str(chromosome[i]) + " "
  st = st[:-1]
  res = "(" + st + ")"

  return res
