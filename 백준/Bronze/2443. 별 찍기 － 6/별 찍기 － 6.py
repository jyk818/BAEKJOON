N = int(input())
space = 0
minus = -1

while True: 
  stars = (2*N) + minus

  if stars <= 0:
    break
  else: 
    print((' '*space)+('*'*stars))
    space = space + 1
    minus = minus - 2