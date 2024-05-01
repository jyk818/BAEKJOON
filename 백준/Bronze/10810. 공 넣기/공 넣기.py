numbers = []

N, M = map(int, (input().split()))
for i in range(N):
  numbers.append(0)

for a in range(M):
  i, j, k = map(int, input().split())
  for b in range(i-1, j, 1):
    del(numbers[b])           #b is the number in () starting from the start value
    numbers.insert(b, k)  #insert(index, object)

for c in numbers:
  print(c, end=' ')