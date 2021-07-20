'''
Palindrome is a word that can be read front and back the same
i.e. "Able was I" and "I was able"

First, pull out all punctuation, spaces
2nd, convert all to lower case
3rd, if first and last is the same, check the letters in between.
'''

def isPalindrome(s):
	def toChars(s):
		s = s.lower()
		ans = ''
		for c in s:
			if c in "abcdefghijklmnopqrstuvwxyz":
				ans = ans + c
		return ans

	def isPal(s):
		if len(s) <= 1:
			return True
		else:
			return s[0] == s[-1] and isPal(s[1:-1])

	return isPal(toChars(s))

print(isPalindrome("abeeba"))

print(isPalindrome("Able was I, ere I saw Elba"))
