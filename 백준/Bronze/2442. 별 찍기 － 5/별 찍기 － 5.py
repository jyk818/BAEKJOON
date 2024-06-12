N = int(input())
stars = 1
line = 1

while True:
  if stars == ((2*N-1)+2):
    break

  else: 
    print(' '*(N-line)+'*'*stars)
    stars = stars + 2
    line = line + 1