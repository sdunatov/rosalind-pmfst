def ManhattanTourist(n, m, dw, rt):
  down = []
  dw = dw.split("\n")
  for i in range(n): #jer ima n redaka
    sniz = dw[i].split() #splitani niz
    rj = [int(x) for x in sniz]
    down.append(rj)

  right = []
  rt = rt.split("\n")
  for i in range(n + 1): #jer ima n+1 redaka 
    sniz = rt[i].split() #splitani niz
    rj = [int(x) for x in sniz]
    right.append(rj)
  
  #matrica nxm ispunjena s nulama
  s = [] #matrica putova(udaljenosti)
  for i in range(n + 1): #za svaki redak na karti
    s.append([0] * (m+1)) #niz od m+1 nula

  for i in range(1, n+1):
    s[i][0] = s[i-1][0] + down[i-1][0]

  for j in range(1, m+1):
    s[0][j] = s[0][j-1] + right[0][j-1]
    
  for i in range(1, n+1):
    for j in range(1, m+1):
      s[i][j] = max(s[i-1][j] + down[i-1][j], s[i][j-1] + right[i][j-1])
      
  return s[n][m] #vracamo zadnji el matrice
