import random
def RandomKmers(dna, k): 
  motifs = []
  for linija in dna:
    r = random.randrange(0, len(linija) - k + 1) #random indeks u liniji na kojem rezemo
    motif = linija[r:r+k] #motiv izrezan na random izabranom indeksu r u toj liniji
    motifs.append(motif)
  return motifs



def Profile(motifs, pseudocounts = False):
  k = len(motifs[0]) 
  D = dict()
  D["A"] = [0] * k
  D["C"] = [0] * k
  D["G"] = [0] * k
  D["T"] = [0] * k

  for pattern in motifs: #svaki motif koji imamo prikazat cemo ka enumerate da bi lakse pristupali  njegovin slovima
    for x in enumerate(pattern): #elementi od enumerate(pattern) su uredeni parovi oblika (indeks,slovo)
      D[x[1]][x[0]] = D[x[1]][x[0]] + 1
  
  if pseudocounts:
    D["A"] = [x+1 for x in D["A"]] #za niz koji je value od A, povecaj sve el tog niza za 1
    D["C"] = [x+1 for x in D["C"]]
    D["G"] = [x+1 for x in D["G"]]
    D["T"] = [x+1 for x in D["T"]]

  for i in range(0, k): #idemo po stupcima count matrice
    s = D["A"][i] + D["C"][i] + D["G"][i] + D["T"][i] #suma el.i-tog stupca => sve el.stupca dilimo sumom stupca
    D["A"][i] = D["A"][i]/s
    D["C"][i] = D["C"][i]/s
    D["G"][i] = D["G"][i]/s
    D["T"][i] = D["T"][i]/s
  
  return D

def KmerProbability(kmer, profile):
  p = 1
  for x in enumerate(kmer):
    p = p * profile[x[1]][x[0]]
  return p


def BestPattern(dna, k, profile):
  bestpattern = ""
  bestprob = 0.0000
  for i in range(0, len(dna) - k + 1):
    kmer = dna[i:i+k]
    kmerprob = KmerProbability(kmer, profile)
    if kmerprob > bestprob:
      bestprob = kmerprob
      bestpattern = kmer
  return bestpattern

def Score(motifs):
  score = 0
  for i in range(len(motifs[0])): 
    j = [motif[i] for motif in motifs] #svaki motiv rastavimo na niz od k slova
    score += len(j) - max(j.count("A"), j.count("C"), j.count("G"), j.count("T"))
  return score

def RandomMotifSearch(dna, k, t):
  motifs = RandomKmers(dna, k)
  bestMotifs = motifs
  while(True):
    profile = Profile(motifs, pseudocounts = True)
    motifs = [] #spremamo nove izgenerirane motive i poslije ih provjeravamo
    for i in range(0, t):
      najvjer = BestPattern(dna[i], k, profile) #najvjrj kmer iz i-te  linije dna
      motifs.append(najvjer)
    if Score(motifs) < Score(bestMotifs): #provjerimo jesu novi motivi bolji od starih
      bestMotifs = motifs
    else:
      return bestMotifs
    
#N puta vrtimo trazenje najboljih motiva
def RandomizedMotifSearch(dnaList, k, t, N = 1000):
  dna = []
  tempI = 0
  for i in range(len(dnaList)):
    if dnaList[i] == "\n":
      dna.append(dnaList[tempI:i])
      tempI = i + 1
  dna.append(dnaList[tempI:])
  bestmotifs = RandomMotifSearch(dna, k, t)
  for i in range(1, N):
    motifs = RandomMotifSearch(dna, k, t)
    if Score(motifs) < Score(bestmotifs):
      bestmotifs = motifs

  for best in bestmotifs:
      print(best)
  return 
