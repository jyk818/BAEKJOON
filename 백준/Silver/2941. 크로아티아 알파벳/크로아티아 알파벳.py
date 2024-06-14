word = input()
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alphabet:
  word = word.replace(i,'*')  # replace(replace this thing, with this thing)

print(len(word))