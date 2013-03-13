#pyg contains the suffix that you add to the end of words
pyg = 'ay'

#original is the variable used to store the user input.

original = raw_input('Enter a word:')

#the first if/else block makes sure the word entered
#is made of letters and is long enough (not empty).
if len(original) > 0 and original.isalpha():
  word = original.lower()
	first = word[0]
	#this if/else block determines if the first letter is a vowel or 
	#consonant.
	if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
		print original + pyg
	else:
		rest = original[1:len(original)]
		new_word =  rest + first + pyg
		print new_word
	
else:
	print 'empty'
