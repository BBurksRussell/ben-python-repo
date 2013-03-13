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
	#consonant. If the first letter of the string is a vowel, then it adds 'ay' to the end.
	if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
		print original + pyg
	else: #if the first letter of the string is a consonant, then that letter is moved to
	      #end of the string, followed by 'ay'.
		rest = original[1:len(original)]
		new_word =  rest + first + pyg
		print new_word
	
else: # if the input is either not long enough or not made of letters, then this else statement 
      #prints 'empty'.
	print 'empty'
