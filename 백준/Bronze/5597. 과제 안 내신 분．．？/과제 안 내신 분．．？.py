# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
numbers = []
for i in range(1, 31, 1) :
  numbers.append(i)

for i in range(28): 
  n = int(input())
  numbers.remove(n)

print(numbers[0])
print(numbers[1])
