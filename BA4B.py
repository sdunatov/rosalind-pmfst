def Zamjena(text):
  t = ""
  for i in range(len(text)):
    if(text[i] == 'T'):
      t += 'U'    
    else:
      t += text[i]
  return t

def Inverz(text):
  tex = ""
  for i in range(len(text)):
    if(text[i] == 'A'):
      tex += 'T'
    if(text[i] == 'T'):
      tex += 'A'
    if(text[i] == 'G'):
      tex += 'C'
    if(text[i] == 'C'):
      tex += 'G'
  return tex[::-1]

def Translation(text):
  rjecnik = {"CAU":"H","CAC":"H","CAA":"Q","CAG":"Q", "CCU":"P","CCC":"P","CCA":"P","CCG":"P","CGU":"R", "CGC":"R","CGA":"R", "CGG":"R","CUU":"L","CUC":"L","CUA":"L","CUG":"L",
         "GAU":"D","GAC":"D","GAA":"E","GAG":"E","GCU":"A","GCC":"A","GCA":"A","GCG":"A","GGU":"G","GGC":"G","GGA":"G","GGG":"G","GUU":"V","GUC":"V","GUA":"V","GUG":"V","UAU":"Y",
         "UAC":"Y","UAA":"*","UAG":"*","UCG":"S", "UCA":"S","UCC":"S", "UCU":"S","UGU":"C","UGC":"C","UGA":"*","UGG":"W","UUU":"F", "UUC":"F","UUA":"L","UUG":"L", "AAU":"N",
         "AAC":"N","AAA":"K","AAG":"K", "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T","AGU":"S", "AGC":"S","AGA":"R","AGG":"R","AUU":"I","AUC":"I","AUA":"I","AUG":"M"}
  kodoni = []
  res = ""
  ulaz = Zamjena(text)

  for i in range(0, len(ulaz), 3):
    kodoni.append(ulaz[i:i+3])

  for k in kodoni:
    res += rjecnik[k]
  return res.replace("*","")

def Encoding(text, peptide):
  duljina = 3 * len(peptide)
  result = []

  for i in range(0, len(text) - duljina):
    kmer = text[i:i+duljina]
    pep = Translation(kmer)
    pep2 = Translation(Inverz(kmer))
    if(pep == peptide or pep2 == peptide):
      result.append(kmer)

  for r in result:
    print(r)
  return
