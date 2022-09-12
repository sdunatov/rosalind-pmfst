def MinSkew(genome):
  skew = []
  minimalni = []
  skewTrenutni = 0
  skew.append(skewTrenutni)
  for i in range(len(genome)):
    if genome[i] == 'C':
      skewTrenutni -= 1
      skew.append(skewTrenutni)
    elif genome[i] == 'G':
      skewTrenutni += 1
      skew.append(skewTrenutni)
    else:
      skew.append(skewTrenutni)
  
  mini = min(skew)
  for i in range(len(skew)):
    if skew[i] == mini:
      minimalni.append(i)

  return minimalni
