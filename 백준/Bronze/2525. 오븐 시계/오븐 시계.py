A, B = map(int, input().split())
C = int(input())

if B+C < 60:
  print(A, B+C)
else:
  N = (B+C) // 60
  R = (B+C) % 60
  if A+N >= 24: 
    print(A+N-24, R)
  else: 
    print(A+N, R)