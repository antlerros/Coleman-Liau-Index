import sys
import string


with open(str(sys.argv[1]), 'r') as file:
	content = file.read()
	L = 0; # number of letters or digits
	S = content.count('.') # number of sentence
	for i in content:
		if i.isalpha() or i.isdigit():
			L = L + 1
	print '# of sentences: ', S
	print '# of letters: ', L
	print 'CLI: ', 0.0558*L - 0.296*S - 15.8

	