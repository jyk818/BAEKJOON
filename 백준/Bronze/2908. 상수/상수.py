A, B = input().split()

A = int(A[2] + A[1] + A[0])     # making str into int
B = int(B[2] + B[1] + B[0])

# print(A, B)

if A > B: 
  print(A)
else: 
  print(B)