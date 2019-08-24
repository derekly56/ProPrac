'''
Author: Derek Ly
Question: String Compression(Pg. 91)
---------------------------------------------------------------------
Implement a method to perform basic string compression using the
counts of repeated characters. For example, the string aabcccccaaa
would become a2b1c5a3. If the "compressed" string would not become
smaller than the original string, your method should return the
original string. You can assume the string has only uppercase and
lowercase letters(a-z).

Example
-------

Input: s1 = "aabcccccaaa"
Output: s1 = "a2b1c5a3"
---------------------------------------------------------------------
'''

'''
Function stringCompression
-------------------------

This function will take in a string of letters and compress them into
a manageable string with the count following each letter. There are two
methods of doing it: 1) iterate through the string, keep a running count
of each letter, form a string, then concatenate OR 2) iterate through the
string, keep a running count of each letter, form a string, and append it
to an array and combine it at the end. Method 1 and 2 BOTH WORKS. However,
method 1 runs in O(n^2) because concatenation runs in O(n^2). Method 2 runs
in O(n) because we are joining each string element in the array at the end,
one at a time.

Run-Time Complexity: O(n)
Space Complexity: O(n)
'''

def stringCompression(longString):

	l = len(longString)
	current = 0
	compress = []
	count = 1

	for i in range(1, l):
		if (longString[i] != longString[current]) or (i + 1 == l):
			comp = longString[current] + str(count)
			compress.append(comp)
			count = 1
			current = i
		else:
			count += 1

	compressed = ''.join(compress)

	if len(compressed) > len(longString):
		return longString

	return compressed


'''
Test Cases
'''

'''
This first test case will compress the string and return the new string

Input: aabcccccaaa
Output: a2b1c5a3
'''
testOne = "aabcccccaaa"
s1 = stringCompression(testOne)
print(s1)

'''
This second test case will compress the string, but will return the original
string since it is shorter.

Input: ABCD
Output: ABCD, since A1B1C1D1 is longer 
'''
testTwo = "ABCD"
s2 = stringCompression(testTwo)
print(s2)
