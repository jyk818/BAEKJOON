T = int(input())

for i in range(T):
  coins = []
  C = int(input())
  
  if C >= 25: 
    coins.append(C//25)
  else: 
    coins.append(0)
  if (C%25) >= 10:
    coins.append((C%25)//10)
  else: 
    coins.append(0)
  if ((C%25)%10) >= 5:
    coins.append(((C%25)%10)//5)
  else: 
    coins.append(0)
  if (((C%25)%10)%5) >= 1: 
    coins.append((((C%25)%10)%5)//1)
  else: 
    coins.append(0)

  # print(coins)
  for i in coins:
    print(i, end=' ')