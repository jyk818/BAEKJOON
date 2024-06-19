A = []
maximum = -1    # input is somewhere between 0~100 so if everything is 0 then the index can't be found
row = 0
col = 0

for i in range(9):
  li = list(map(int, input().split()))
  A.append(li)

  if maximum < max(li):
    maximum = max(li)
    row = i+1
    col = (li.index(max(li))) + 1

print(maximum)
print(row, col)