while True:
  factors = []
  result = ''
  n = int(input())

  if n == -1:
      break

  for x in range(1, n, 1):
    if n % x == 0:
      factors.append(x)

  # print(factors)
  if (sum(factors)) == n:
    # print('yes')
    result += "%d = " % n
    for y in factors:
      result += "%d + " % y
    print(result[:len(result)-3])   # to delete the + at the very end
  else:
    print("%d is NOT perfect." % n)
