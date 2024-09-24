N = int(input())
min = 1
max = 1
count = 1
while True: 
  if min <= N and N <= max:
    print(count)
    break
  else: 
    min = max+1
    max = max + (6 * count)
    count += 1