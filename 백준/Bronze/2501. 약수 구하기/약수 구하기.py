N, K = map(int, input().split())
factors = []

for x in range(N):
  if N% (x+1) == 0:
    factors.append(x+1)
for i in range(N):
  factors.append(0)

print(factors[K-1])