value = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = 0

N, B = input().split()
B = int(B)

length = len(N)

for i in N:
  # print(value.index(i), length)
  length = length - 1                   # exponent value going down
  sum += (value.index(i) * (B**length))   # keep adding len(N) times

print(sum)