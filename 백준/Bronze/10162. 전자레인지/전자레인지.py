T = int(input())
A = 300
B = 60
C = 10
if T%10 != 0:
  print(-1)
else:
  A_button = T//A
  B_button = (T%A)//B
  C_button = ((T%A)%B)//C
  print(A_button, B_button, C_button)