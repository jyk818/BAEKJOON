while True: 
  A, B = map(int, input().split())
  if A==B:
    break
  if B%A == 0: 
    print('factor')
  if A%B == 0:
    print('multiple')
  if (B%A != 0) and (A%B !=0):
    print('neither')