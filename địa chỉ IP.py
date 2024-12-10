def kt(n):
    if len(n)!=4:
        return 'NO'
    for i in n:
        if not i.isdigit() or not (0<=int(i)<=255):
            return 'NO'
    else:
        return 'YES'
for t in range(int(input())):
    a=input().split('.')
    print(kt(a))