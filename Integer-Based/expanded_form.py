"""Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'"""

def expanded_form(num):
	"""takes an integer of n-digits and returns a string where each non-zero digit is followed by as many zeros as its position in the integer (modulo 10)"""
		#The main challenges here is going to be that integers are not iterables
		# Normally, I would try iterating on something of the likes of the second suggestion here: https://stackoverflow.com/questions/974952/split-an-integer-into-digits-to-compute-an-isbn-checksum
		#But since the end output is going to be a string, we might as well string methods
		string_num= str(num)
		expanded= ""
		#We'll keep adding to the empty string as we process each digit
		for digit in string_num:
			