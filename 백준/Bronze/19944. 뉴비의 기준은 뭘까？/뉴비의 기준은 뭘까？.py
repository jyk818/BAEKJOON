N, M = map(int, input().split())

if M == 1 or M == 2:
  print('NEWBIE!')
elif M <= N and M > 2:  # 2 < M <= N
  print('OLDBIE!')
else:
  print('TLE!')