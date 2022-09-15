def CycleToCromosome(seq):
  seq = seq.strip("()")
  seq = seq.split(" ")
  nodes = []
  chromosome = []
  st = ""

  for node in seq:
    nodes.append(int(node))
    
  for i in range(0, len(nodes)-1, 2):
    if(nodes[i] < nodes[i+1]):
      chromosome.append("+" + str(nodes[i+1] // 2))
    else:
      chromosome.append("-" + str(nodes[i] // 2))

  for i in range(len(chromosome)):
    st += str(chromosome[i]) + " "
  st = st[:-1]
  res = "(" + st + ")"

  return res 
