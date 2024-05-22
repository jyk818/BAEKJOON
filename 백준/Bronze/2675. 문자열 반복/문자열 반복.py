T = int(input())

for i in range(T): 
  R, S = input().split()
  R = int(R)
  
  for x in range(len(S)): 
    print(S[x] * R, end='')
  print()