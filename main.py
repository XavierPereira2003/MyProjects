import math
from random import randint


def mainplay(Entrybox):#(Entry Box)

    def shuffleValues(arr2d):
        chooseNumber = -1
        replacingNumber = -1
        while(replacingNumber == chooseNumber):
            chooseNumber = randint(1, 9)
            replacingNumber = randint(1, 9)
        for i in range(0, 9):
            for j in range(0, 9):
                if(arr2d[i][j] == chooseNumber):
                    arr2d[i][j] = replacingNumber
                elif(arr2d[i][j] == replacingNumber):
                    arr2d[i][j] = chooseNumber
    
        sizeOfInnerMatrix = int(math.sqrt(9))
        if (sizeOfInnerMatrix > 1):
            chooseRowIndex = -1
            replacingRowIndex = -1
            while(chooseRowIndex == replacingRowIndex):
                chooseRowIndex = randint(1, sizeOfInnerMatrix)
                replacingRowIndex = randint(1, sizeOfInnerMatrix)
            multiplier = randint(0, sizeOfInnerMatrix-1)
            chooseRowIndex+=(multiplier*sizeOfInnerMatrix)
            replacingRowIndex+=(multiplier*sizeOfInnerMatrix)
            arr2d[chooseRowIndex - 1], arr2d[replacingRowIndex - 1] = arr2d[replacingRowIndex -1], arr2d[chooseRowIndex - 1]
            arr2d = [[x[i] for x in arr2d] for i in range(9)]
            chooseRowIndex-=(multiplier*sizeOfInnerMatrix)
            replacingRowIndex-=(multiplier*sizeOfInnerMatrix)
            multiplier = randint(0, sizeOfInnerMatrix-1)
            chooseRowIndex+=(multiplier*sizeOfInnerMatrix)
            replacingRowIndex+=(multiplier*sizeOfInnerMatrix)
            arr2d[chooseRowIndex - 1], arr2d[replacingRowIndex - 1] = arr2d[replacingRowIndex -1], arr2d[chooseRowIndex - 1]
            
        return arr2d
    
    global A1,A2,A3,B1,B2,B3,C1,C2,C3,A4,A5,A6,B4,B5,B6,C4,C5,C6,A7,A8,A9,B7,B8,B9,C7,C8,C9
    global D1,D2,D3,E1,E2,E3,F1,F2,F3,D4,D5,D6,E4,E5,E6,F4,F5,F6,D7,D8,D9,E7,E8,E9,F7,F8,F9
    global G1,G2,G3,H1,H2,H3,I1,I2,I3,G4,G5,G6,H4,H5,H6,I4,I5,I6,G7,G8,G9,H7,H8,H9,I7,I8,I9
    global row1,row2,row3,row4,row5,row6,row7,row8,row9,Values
    
    A1=A2=A3=A4=A5=A6=A7=A8=A9=None
    B1=B2=B3=B4=B5=B6=B7=B8=B9=None
    C1=C2=C3=C4=C5=C6=C7=C8=C9=None
    D1=D2=D3=D4=D5=D6=D7=D8=D9=None
    E1=E2=E3=E4=E5=E6=E7=E8=E9=None
    F1=F2=F3=F4=F5=F6=F7=F8=F9=None
    G1=G2=G3=G4=G5=G6=G7=G8=G9=None
    H1=H2=H3=H4=H5=H6=H7=H8=H9=None
    I1=I2=I3=I4=I5=I6=I7=I8=I9=None
    
    
    row1=[A1,A2,A3,B1,B2,B3,C1,C2,C3]
    row2=[A4,A5,A6,B4,B5,B6,C4,C5,C6]
    row3=[A7,A8,A9,B7,B8,B9,C7,C8,C9]
    
    row4=[D1,D2,D3,E1,E2,E3,F1,F2,F3]
    row5=[D4,D5,D6,E4,E5,E6,F4,F5,F6]
    row6=[D7,D8,D9,E7,E8,E9,F7,F8,F9]
    
    row7=[G1,G2,G3,H1,H2,H3,I1,I2,I3]
    row8=[G4,G5,G6,H4,H5,H6,I4,I5,I6]
    row9=[G7,G8,G9,H7,H8,H9,I7,I8,I9]
    
    Values=[row1,row2,row3,row4,row5,row6,row7,row8,row9]
    for i in range(0, 9):
        for j in range(0, 9):
            Values[i][j] = int((i * math.sqrt(9) + int(i / math.sqrt(9)) + j) % 9) + 1
    
    
    randomInt = randint(8, 15)
    for _ in range(randomInt):
        Values = shuffleValues(Values)
    
    for i in range(9):
        for j in range(9):
            Entrybox[i][j].insert(0,Values[i][j])

    
    
