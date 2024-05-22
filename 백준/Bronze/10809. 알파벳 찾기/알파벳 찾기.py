S = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(26): 
  if alphabet[i] in S: 
    print(S.index(alphabet[i]), end=' ')
  else: 
    print(-1, end=' ')