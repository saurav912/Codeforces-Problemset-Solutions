year = input()
while(True):
    year=str(int(year)+1)
    if(len(set(year))==4):
        print(year)
        break
