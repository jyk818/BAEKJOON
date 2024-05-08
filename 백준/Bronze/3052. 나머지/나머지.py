remainder = []

for i in range(10): 
  A = int(input())
  remainder.append(A%42)
set_remainder = set(remainder)    # set - 중복이 없는 list
print(len(set_remainder))