N = int(input())

for x in range(N+1):
  if(x > 0):
    print(' '*(N-x)+'*'*x)