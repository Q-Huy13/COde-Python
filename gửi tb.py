for i in range(int(input())):
    a=input().split()
    b=0
    for j in a:
        if b+len(j)<=100:
            print(j,end=' ')
            b+=len(j)+1
        else:break
    print()