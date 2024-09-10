# value = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# N, B = map(int, input().split())
# num = 0
# ans = ''

# while True: 
#   if N > (B**num):
#     num +=1
#   else:
#     break
# exponent = num

# for i in range(num):
#   for j in value[::-1]:   # [::-1] : reverse
#     s = value.index(j) * (B ** (exponent - 1))
#     if s <= N:
#       ans = ans+j
#       N = N-s
#       exponent -= 1
#       # print(exponent)
#       break
# print(ans)


value = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ''

N, B = map(int, input().split())

while(N>0):
  ans = value[N % B] + ans
  N //= B
print(ans)