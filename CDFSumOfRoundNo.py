for x in range(int(input())):
    n=input()
    l=[]
    for i in range(len(n)):
        if n[i]!="0":
            l.append(n[i]+(len(n)-i-1)*"0")
    print(len(l))
    print(" ".join(l))
