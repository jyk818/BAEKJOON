N, M = map(int, input().split())

A = []
B = []

for i in range(N*2):                          # how many rows there are
  li = list(map(int, input().split()))        # make input into list right away
  if (i<N):                                   
    A.append(li)
  else:
    B.append(li)

# to use a double list, double loop:
for row in range(N):
  for col in range(M):
    print(A[row][col]+B[row][col], end=' ')
  print()