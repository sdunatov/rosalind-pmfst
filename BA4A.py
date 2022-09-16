def ProteinTranslation(rna):
  trans = []
  novi = []
  for i in range(0, len(rna), 3):
    trans.append(rna[i:3+i])
  
  for el in trans:
    if(el[0] == 'A'):
      if(el[1] == 'U'):
        if(el[2] == 'G'):
          novi.append('M')
        else:
          novi.append('I')
      if(el[1] == 'G'):
        if((el[2] == 'G') or (el[2] == 'A')):
          novi.append('R')
        else:
          novi.append('S')
      if(el[1] == 'C'):
        novi.append('T')
      if(el[1] == 'A'):
        if((el[2] == 'G') or (el[2] == 'A')):
          novi.append('K')
        else:
          novi.append('N')

    if(el[0] == 'U'):
      if(el[1] == 'U'):
        if((el[2] == 'G') or (el[2] == 'A')):
          novi.append('L')
        else:
          novi.append('F')
      if(el[1] == 'G'):
        if(el[2] == 'G'):
          novi.append('W')
        elif(el[2] == 'A'):
          break
        else:
          novi.append('C')
      if(el[1] == 'C'):
        novi.append('S')
      if(el[1] == 'A'):
        if((el[2] == 'G') or (el[2] == 'A')):
          break
        else:
          novi.append('Y')

    if(el[0] == 'G'):
      if(el[1] == 'U'):
        novi.append('V')
      if(el[1] == 'G'):
        novi.append('G')    
      if(el[1] == 'C'):
        novi.append('A')
      if(el[1] == 'A'):
        if((el[2] == 'G') or (el[2] == 'A')):
          novi.append('E')
        else:
          novi.append('D')

    if(el[0] == 'C'):
      if(el[1] == 'U'):
        novi.append('L')
      if(el[1] == 'G'):
        novi.append('R')
      if(el[1] == 'C'):
        novi.append('P')
      if(el[1] == 'A'):
        if((el[2] == 'G') or (el[2] == 'A')):
          novi.append('Q')
        else:
          novi.append('H')
  rez = ''
  for el in novi:
    rez += el
  return rez
