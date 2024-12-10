def kt(n):
    for i in n:
        if i not in ['0','1','2']:
            return False
    return True
for i in range(int(input())):
    t=input()
    if kt(t):
        print('YES')
    else:
        print('NO')
