bonds = {'H-H':436,'C-C':348,'N-N':163,'O-O':146,'F-F':155,'Cl-Cl':242,\
         'Br-Br':193,'I-I':151,'Si-Si':226,'S-S':266,'C-N':293,'C-O':358,\
         'C-S':259,'C-F':485,'C-Cl':328,'C-Br':288,'C-I':216,'C-Si':301,\
         'H-C':413,'H-N':391,'H-O':463,'H-F':567,'H-Cl':431,'H-Br':366,\
         'H-I':299,'H-S':339,'H-Si':323,'O--O':495,'O-F':190,'O-Cl':203,\
         'O-Si':368,'S--O':323,'S--S':418,'C--O':799,'C---O':1072,'S-Br':218,\
         'S-F':218,'S-Cl':253,'N-N':163,'N---N':941,'N--C':615,'N---C':891,\
         'N-O':201,'N-Br':243,'N-Cl':200,'N-F':272,'C--C':614,'C---C':839,\
         'Cl-Si':464}

while True:
  bondInput = raw_input("Enter a bond: ")
  bondInput = bondInput.upper()
  try:
    print "Bond Enthalpy:", bonds[bondInput], "kJ/mol"
  except:
    numDashes = bondInput.count('-')
    firstElement = bondInput[0:bondInput.index(numDashes*'-')]
    secondElement = bondInput[bondInput.index(numDashes*'-')+numDashes:]
    bondInput = secondElement + numDashes*'-' + firstElement
    try:
      print "Bond Enthalpy:", bonds[bondInput], "kJ/mol"
    except:
      print "invalid input"
