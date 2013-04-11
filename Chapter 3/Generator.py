'''This is for Exercise 7 in Chapter 2'''

import string

def generate_letters():
	while True:
		for letter in string.lowercase:
			yield letter
				

def main(script, *args):
	letters = generate_letters()
	digit = 1
	
	for letter in letters:
		if letter != 'z':
			print letter + str(digit)
		if letter == 'z':
			print letter + str(digit)
			digit += 1
	


if __name__ == '__main__':
    import sys
    main(*sys.argv)
