N = int(input())
min = 1
max = 1
count = 1
while True: 
  if min <= N and N <= max: # if N is in between this range
    print(count)            # number of layers
    break
  else: 
    min = max+1             # start of next layer
    max = max + (6 * count) # end of next layer
    count += 1              # add one more layer to the bee hive


###

# N = int(input())
# max = 1
# count = 1

# while max < N :       # if N becomes greater than the max range
#   max += 6 * count    # end of next layer
#   count += 1          # another layer

# print(count)
