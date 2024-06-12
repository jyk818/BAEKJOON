N = int(input())

for i in range(1, N*2, 1):
  if(i <= N):
    for j in range(0, N-i, 1):
      print(' ', end='')
    for j in range(0, 2*i-1, 1):
      print('*', end='')
    print()
  else:
    for j in range(i-N):
      print(' ', end='')
    for j in range((2*N-i)*2-1):
      print('*', end='')
    print()