T = int(input())

for _ in range(T):
    S1 = input()
    S2 = input()
    X = input()
    i,j =0,0
    result = 0
    print("Start")
    while len(S1)>i or len(S2)>j:
        P = S1[:i+1]
        Q = S2[:j+1]
        sum = P+Q
        print(sum)
        count = X.count(sum)

        if count>0:
            result+= count
        if len(S1)<i:
            i+=1
        if len(S2)<j:
            j+=1
        break
    print(result)