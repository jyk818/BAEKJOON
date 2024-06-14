word = list(input().upper())
alphabet = list(set(word))        # set = deleting duplicates
count = []

for i in alphabet:                # letter of word
  cnt = word.count(i)             # count how many of that letter there is in the word
  count.append(cnt)               # add the number to count[]

# print(alphabet)
# print(count)
# print(count.count(max(count)))

if count.count(max(count)) >= 2:  #if there are more than 2 alphabets that are the max in 'count'
  print('?')
else:
  print(alphabet[count.index(max(count))])