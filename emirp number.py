def nt(k):
    if k<2:
        return False
    for i in range(2,int(k**0.5)+1):
        if k%i==0:
            return False
    return True
def kt(k):
    if k==str(k)[::-1]:
        return False
    return True
for _ in range(int(input())):
    n=int(input())
    for i in range(10,n+1):
        if nt(i) and nt(int(str(i)[::-1])) and kt(n):
            print(i)


