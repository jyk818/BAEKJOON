H, M = map(int, input().split())

if M-45 >= 0: 
  print(H, M-45)

if M-45 < 0:
  M = M+60
  H = H-1
  if H<0: 
    H = 23
  print(H, M-45)