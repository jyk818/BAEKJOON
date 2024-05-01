numbers = []

N, M = map(int, (input().split()))
for i in range(N):
  numbers.append(i+1)

for a in range(M):
  i, j = map(int, input().split())

  tmp = 0

  # switching numbers
  tmp = numbers[i-1]
  numbers[i-1] = numbers[j-1]
  numbers[j-1] = tmp

for c in numbers:
  print(c, end=' ')