N, K = map(int,input().split())
num = list()
for i in range(1, N+1) :
    if N % i == 0 :
        num.append(i)
    else :
        continue
if len(num) < K :
    print(0)
else :
    print(num[K-1])

