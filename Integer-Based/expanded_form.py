"""Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'"""

import itertools

def expanded_form(num):
	"""takes an integer of n-digits and returns a string where each non-zero digit is followed by as many zeros as its position in the integer (modulo 10)"""
		#The main challenges here is going to be that integers are not iterables
		# Normally, I would try iterating on something of the likes of the second suggestion here: https://stackoverflow.com/questions/974952/split-an-integer-into-digits-to-compute-an-isbn-checksum
		#But since the end output is going to be a string, we might as well string methods
	string_num= str(num)
	expanded= ""
	#We'll keep adding to the empty string as we process each digit
	for idx, digit in enumerate(string_num, 1):
		# The second argument is to ensure that indexing starts from 1 instead of 0
		# Taking advice from here on keeping indices while looping: https://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops
		if not digit="0":
			num_zeros= len(string_num)- idx
			for _ in itertools.repeat(None, num_zeros):
				digit+="0"
			expanded+= digit
			while idx< len(string_num):
				expanded+= " + "
		else:
			continue
	return expanded

