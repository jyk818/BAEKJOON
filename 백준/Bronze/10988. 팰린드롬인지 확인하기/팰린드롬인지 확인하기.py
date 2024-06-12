# Case 1 : reverse using string
# N = input()

# if N == N[::-1]:
#  print('1')
# else:
#  print('0')

 # Case 2 : reverse using list
N = list(input())

if list(reversed(N)) == N:
  print(1)
else:
  print(0)
