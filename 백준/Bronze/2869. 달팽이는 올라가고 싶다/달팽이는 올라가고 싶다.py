# finish in 0.25 seconds = not loops
A, B, V = map(int, input().split())

# V-B is because the last night's falling part doesn't count
# A-B is the amount moved each day
if((V-B) % (A-B) == 0): # if it falls right at V
  print((V-B)//(A-B))
else:                   # +1 if it goes higher than V
  print(((V-B)//(A-B)) +1)