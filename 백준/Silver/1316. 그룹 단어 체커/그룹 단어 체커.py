N = int(input())

for i in range(N):
  word = input()
  for j in range(len(word)-1):
    if word[j] != word[j+1]:        # taking out all the things where the first and second letters are the same
      if word[j+1] in word[:j]:     # if the second letter is has ever come out before the first letter
        N = N -1
        break                       # stop repeating when N has already become N-1

print(N)