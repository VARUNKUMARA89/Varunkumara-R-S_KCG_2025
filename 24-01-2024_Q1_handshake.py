def handshake(a):
    sum = 0
    for i in range (1,a):
        sum+=i
    print(sum)

n = int(input())
for i in range (n):
    a=int(input())
    handshake(a)