<<<<<<< HEAD
#file = open('words.txt')

#for line in file:
 # word = line.strip()
  #print word
  
def has_no_e(word):
 return not "e" in word

print has_no_e("hi")
print has_no_e("hello")


def uses_only(word, available):
 for letter in word:
  if not letter in available: return False
 return True

print uses_only("abbcc", "abc")
print uses_only("abbccd", "abc")

def uses_all(word, available):
 return uses_only(available, word)
 
print uses_all("ab", "abc")
print uses_all("abcc", "abc")

def is_abecedarian(word):
 return "".join(sorted(word))==word # join the string elements of the list word, separated by ""
 
print is_abecedarian("randomword")
print is_abecedarian("abcde")
=======
file = open('words.txt')

for line in file:
  word = line.strip()
  print word
>>>>>>> upstream/master
