X = int(input())

# triangular number:n(n+1)/2

n = 1
triangular_number = 1

while(X>triangular_number):
  n+=1
  triangular_number = n*(n+1)/2

# subtract last number from X to find the index
last_triangular_number = ((n-1)*((n-1)+1)//2)
index=X-last_triangular_number
if n%2 ==0:
  print("%d/%d" % (index, n-index+1))
else: 
  print("%d/%d" % (n-index+1, index))