try:
    T= int(input())
    for i in range(T):
        X = 0
        O =0
        space=0

        pos=[]
        for i in range(3):
            row= input()
            pos.append(row)

        for i in range(3):
            for j in range(3):
                if pos[i][j] =='X': X +=1
                elif pos[i][j] =='O': O +=1
                elif pos[i][j] == '_': space +=1
        solX, solO = 0, 0
        if pos[0][0] == 'X' and pos[0][1]=='X' and pos[0][2] == 'X': solX=1
        if pos[1][0] == 'X' and pos[1][1]=='X' and pos[1][2] == 'X': solX=1
        if pos[2][0] == 'X' and pos[2][1]=='X' and pos[2][2] == 'X': solX=1
        if pos[0][0] == 'X' and pos[1][0]=='X' and pos[2][0] == 'X': solX=1
        if pos[0][1] == 'X' and pos[1][1]=='X' and pos[2][1] == 'X': solX=1
        if pos[0][2] == 'X' and pos[1][2]=='X' and pos[2][2] == 'X': solX=1
        if pos[0][0] == 'X' and pos[1][1]=='X' and pos[2][2] == 'X': solX=1
        if pos[0][2] == 'X' and pos[1][1]=='X' and pos[2][0] == 'X': solX=1


        if pos[0][0] == 'O' and pos[0][1]=='O' and pos[0][2] == 'O': solO=1
        if pos[1][0] == 'O' and pos[1][1]=='O' and pos[1][2] == 'O': solO=1
        if pos[2][0] == 'O' and pos[2][1]=='O' and pos[2][2] == 'O': solO=1
        if pos[0][0] == 'O' and pos[1][0]=='O' and pos[2][0] == 'O': solO=1
        if pos[0][1] == 'O' and pos[1][1]=='O' and pos[2][1] == 'O': solO=1
        if pos[0][2] == 'O' and pos[1][2]=='O' and pos[2][2] == 'O': solO=1
        if pos[0][0] == 'O' and pos[1][1]=='O' and pos[2][2] == 'O': solO=1
        if pos[0][2] == 'O' and pos[1][1]=='O' and pos[2][0] == 'O': solO=1


        if ((solX ==1 and solO ==1) or (X-O < 0) or (X-O > 1)):  # IMPOSSIBLE
            print(3)
        elif (X==0 and O==0 and space ==9):
            print(2)
        elif (solX ==1 and solO ==0 and X>O):    # DRAW
            print(1)
        elif (solX == 0 and solO == 1 and X == O):
            print(1)
        elif (solX == 0 and solO == 0 and space ==0):
            print(1)
        elif (solX == 0 and solO == 0 and space >0):
            print(2)
        else:
            print(3)

except:
    pass