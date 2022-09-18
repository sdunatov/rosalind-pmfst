import random
def RandomKmers(dna, k):
  motifs = []
  for linija in dna:
    r = random.randrange(0, len(linija) - k + 1) #zadnji element nije ukljucen
    motif = linija[r:r+k] #motif izrezan na random izabranom indeksu r u toj liniji
    motifs.append(motif)
  return motifs

def Profile(motifs, pseudocounts = False):
    k = len(motifs[0])
    D = dict()
    D["A"] = [0] * k
    D["C"] = [0] * k
    D["G"] = [0] * k
    D["T"] = [0] * k

    for pattern in motifs:
        for x in enumerate(pattern):
            D[x[1]][x[0]] = D[x[1]][x[0]] + 1

    if pseudocounts:
        D["A"] = [x + 1 for x in D["A"]]
        D["C"] = [x + 1 for x in D["C"]]
        D["G"] = [x + 1 for x in D["G"]]
        D["T"] = [x + 1 for x in D["T"]]

    for i in range(0, k):
        s = D["A"][i] + D["C"][i] + D["G"][i] + D["T"][i]
        D["A"][i] = D["A"][i] / s
        D["C"][i] = D["C"][i] / s
        D["G"][i] = D["G"][i] / s
        D["T"][i] = D["T"][i] / s
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
  for i in range(len(motifs[0])): #idemo od 0 do k (po duljini svakog motifa)
    j = [motif[i] for motif in motifs] #svaki motif rastavimo na niz od k slova
    score += len(j) - max(j.count("A"), j.count("C"), j.count("G"), j.count("T")) #izbrojimo sva velika slova tj kojih ima najvise => k minus taj br se dodaje score
  return score

# izvodi Gibbsovo sampliranje N puta
def GibbsSamplerAtom(dna, k, t, N):
  motifs = RandomKmers(dna, k)
  bestmotifs = motifs
  for j in range(1, N):
    i = random.randint(0, t-1) #biramo random liniju iz dna (t-1 ukljuceno)
    tmp = list(motifs) #od trenutnih motiva napravimo listu
    tmp.pop(i) #i izbacimo i-ti motiv
    profile = Profile(tmp, pseudocounts=True) #od tih motiva bez i-tog napravimo profilnu matricu
    najvjer = BestPattern(dna[i], k, profile) #s obzirom na tu matricu izaberemo novi kmer iz i-te linije
    motifs[i] = najvjer #i ubacimo ga u listu
    if Score(motifs) < Score(bestmotifs):
      bestmotifs = list(motifs) 
  return bestmotifs
  
# izvodi Gibbsovo N sampliranje 20 puta
def GibbsSampler(dnaList, k, t, N, rep = 20):
  dna = []
  tempI = 0
  for i in range(len(dnaList)):
    if dnaList[i] == "\n":
      dna.append(dnaList[tempI:i])
      tempI = i + 1
  dna.append(dnaList[tempI:])

  bestmotifs = GibbsSamplerAtom(dna, k, t, N) #napravi gibbsovo sampliranje N puta kao i pocetno
  for i in range(1, rep): #i onda dodatno 20 puta
    motifs = GibbsSamplerAtom(dna, k, t, N)
    if Score(motifs) < Score(bestmotifs):
      bestmotifs = list(motifs)

  for best in bestmotifs:
      print(best)
  return 
