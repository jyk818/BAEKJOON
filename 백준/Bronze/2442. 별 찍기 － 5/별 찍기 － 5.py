# Case 1
# N = int(input())
# stars = 1
# line = 1

# while True:
#   if stars == ((2*N-1)+2):
#     break

#   else: 
#     print(' '*(N-line)+'*'*stars)
#     stars = stars + 2
#     line = line + 1


# Case 2 : split *
# N = int(input())

# for i in range(1, N+1, 1):
#   for j in range(0, N-i, 1):
#     print(' ', end='')
  
#   for j in range(0, i, 1):
#     print('*',end='')
  
#   if(i>=2):
#     for j in range(1, i, 1):
#       print('*',end='')
#   print()


# Case 3
N = int(input())

for i in range(1, N+1, 1):
  for j in range(0, N-i, 1):
    print(' ', end='')
  
  for j in range(0, 2*i-1, 1):
    print('*',end='')

  print()
