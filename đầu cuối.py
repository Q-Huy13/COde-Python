def kt(n):
    for j in n:
        if n[0]==n[-2] and n[1]==n[-1]:
            return True
    return False
for i in range(int(input())):
    n=input()
    if kt(n):
        print('YES')
    else:
        print('NO')
