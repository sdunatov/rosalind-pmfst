def CycloSpectrum(peptide):
    integerMassTable = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
              'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}
    masa_cijelog_peptida = 0
    for slovo in peptide:
        masa_cijelog_peptida += integerMassTable[slovo]
    niz = [0,masa_cijelog_peptida]
    tmp = peptide + peptide[:-1]

    for i in range(1, len(peptide)):
        for j in range(0, len(peptide)):
            subpeptide = tmp[j:(j+i)]
            masa = 0
            for slovo in subpeptide:
                masa += integerMassTable[slovo]
            niz.append(masa)
    niz.sort()
    res = " ".join(map(str,niz))
    return res
