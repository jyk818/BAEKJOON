numbers = {"ABC":2, "DEF":3, "GHI":4, "JKL":5, "MNO":6, "PQRS":7, "TUV":8, "WXYZ":9} # dictionary {key:value, key, value}

T = input()
time = 0

for i in T :
    for j in numbers:       # dictionary's key get saved into j
      if i in j:
        time += numbers[j]  # when accessing values in a dictionary, they are referenced using keys

print(time+len(T))