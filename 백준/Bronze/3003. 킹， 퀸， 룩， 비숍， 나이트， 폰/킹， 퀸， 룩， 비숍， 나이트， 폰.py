original = [1, 1, 2, 2, 2, 8]
new = list(map(int, input().split()))
extra = []

for i in range(6):
  extra.append(original[i] - new[i])

for j in extra:
  print(j, end=' ')