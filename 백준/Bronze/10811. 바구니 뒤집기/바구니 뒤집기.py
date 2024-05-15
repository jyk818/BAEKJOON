N, M = map(int, input().split(' '))
baskets = []
for x in range(N) :
  baskets.append(x+1)
# print(baskets)

for x in range(M) :
  i, j = map(int, input().split(' '))

  for y in range((j-i+1)//2):  # equation to find how many times you have to do the switching thing
    # switching 
    tmp = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = tmp
    
    i += 1   # i = i+1
    j -= 1
  # print(baskets)

for value in baskets:
  print(value, end=' ')
