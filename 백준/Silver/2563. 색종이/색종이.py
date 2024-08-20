graph = []
for i in range(100):
  line = []                     # make 100 lists
  for j in range(100):          # put 100 0's in each list
    line.append(0)
  graph.append(line)            # put each list made and filled into graph list

N = int(input())

for test in range(N) :
  x, y = map(int, input().split())

  for i in range(10) :
    for j in range(10) :
        graph[y+i][x+j] = 1

# for i in range(100) :
#   print(graph[i])

sum = 0
for i in range(100):
  sum += graph[i].count(1)
print(sum)