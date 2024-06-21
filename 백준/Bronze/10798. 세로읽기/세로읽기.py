words = []
whole = ''

for _ in range(5):
  word = list(input())
  words.append(word)

for i in range(15): 
  for j in range(5):
    try:                            # even if the word is not 15 strings
      whole = whole + (words[j][i])
    except:                         # keep going
      continue
print(whole)