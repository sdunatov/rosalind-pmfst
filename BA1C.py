def Reverse(dna):
  dnaList = []
  complement = []
  reverse = dna[::-1]

  for i in range(len(reverse)):
    dnaList.append(reverse[i])

  for el in dnaList:
    if el == "A":
      complement.append("T")
    if el == "C":
      complement.append("G")
    if el == "T":
      complement.append("A")
    if el == "G":
      complement.append("C")

  reverseComplement = "".join(complement)
  return reverseComplement
