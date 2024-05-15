N = int(input())
scores = list(map(int, input().split(' ')))
average = []

M = max(scores)

for i in range(N):
  S = (scores[i-1]/M) * 100
  average.append(S)

print(sum(average)/N)