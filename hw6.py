import unittest

# Name: Jonathan Chiu
# Assignment: 6 (Python)
# Section: CS 2600 TF

# sum3 - Given an array of ints length 3, return the sum of all the elements.

# sum3([1, 2, 3]) -> 6
# sum3([5, 11, 2]) -> 18
# sum3([7, 0, 0]) -> 7

def sum3(nums):
	return sum(nums)

# Given an array of ints length 3, return an array with  the elements "rotated
# left" so {1, 2, 3} yields {2, 3, 1}.

# rotate_left3([1, 2, 3]) -> [2, 3, 1]
# rotate_left3([5, 11, 9]) -> [11, 9, 5]
# rotate_left3([7, 0, 0]) -> [0, 0, 7]

def rotate_left3(nums):
	return nums[1:3] + [nums[0]]

# Given an array of ints length 3, figure out which is larger between the
# first and last elements  in the array, and set all the other elements to be
# that value. Return the changed array.

# max_end3([1, 2, 3]) -> [3, 3, 3]
# max_end3([11, 5, 9]) -> [11, 11, 11]
# max_end3([2, 11, 3]) -> [3, 3, 3]

def max_end3(nums):
	for x in range(0, 3):
		nums[x] = max(nums[0], nums[2])
	return nums

# Given an array of ints, return a new array length 2 containing the first and
# last elements  from the original array. The original array will be length 1
# or more.

# make_ends([1, 2, 3]) -> [1, 3]
# make_ends([1, 2, 3, 4]) -> [1, 4]
# make_ends([7, 4, 6, 2]) -> [7, 2]

def make_ends(nums):
	if len(nums) == 0:
		print("Length of array must be at least 1")
	else:
		return [nums[0], nums[-1]]

# Given an int array length 2, return True if it contains a 2 or a 3.

# has23([2, 5]) -> True
# has23([4, 3]) -> True
# has23([4, 5]) -> False

def has23(nums):
	return 2 in nums or 3 in nums

# Return the number of even ints in the given array. Note: the % "mod"
# operator computes the remainder, e.g. 5 % 2 is 1.

# count_evens([2, 1, 2, 3, 4]) -> 3
# count_evens([2, 2, 0]) -> 3
# count_evens([1, 3, 5]) -> 0

def count_evens(nums):
	evens = 0
	for x in range(0, len(nums)):
		if nums[x] % 2 == 0:
			evens += 1
	return evens

# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers that
# come immediately after a 13 also do not count.

# sum13([1, 2, 2, 1]) -> 6
# sum13([1, 1]) -> 2
# sum13([1, 2, 2, 1, 13]) -> 6

def sum13(nums):
	sum = 0
	x = 0
	while x < len(nums):
		if nums[x] == 13:
			x += 2
		else:
			sum += nums[x]
			x += 1
	return sum


# Given an array length 1 or more of ints, return the difference between the
# largest and smallest values in the array. Note: the built-in min(v1, v2) and
# max(v1, v2) functions return the smaller or larger of two values.

# big_diff([10, 3, 5, 6]) -> 7
# big_diff([7, 2, 10, 9]) -> 8
# big_diff([2, 10, 7, 2]) -> 8

def big_diff(nums):
	smalls = min(int(x) for x in nums)
	biggie = max(int(x) for x in nums)
	return biggie - smalls

# Return the sum of the numbers in the array, except ignore sections of
# numbers starting with a 6 and extending to the next 7 (every 6 will be
# followed by at least one 7). Return 0 for no numbers.

# sum67([1, 2, 2]) -> 5
# sum67([1, 2, 2, 6, 99, 99, 7]) -> 5
# sum67([1, 1, 6, 7, 2]) -> 4

def sum67(nums):
	while 6 in nums:
		index_of_6 = nums.index(6)
		index_of_7 = nums.index(7, index_of_6) # Look for index of 7 starting from index of 6
		del nums[index_of_6:index_of_7 + 1] # Delete all numbers between 6 and 7, inclusive
	return sum(nums)

# Return the "centered" average of an array of ints, which we'll say is the mean
# average of the values, except ignoring the largest and smallest values in the
# array. If there are multiple copies of the smallest value, ignore just one copy,
# and likewise for the largest value. Use int division to produce the final
# average. You may assume that the array is length 3 or more.

# centered_average([1, 2, 3, 4, 100]) -> 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) -> 5
# centered_average([-10, -4, -2, -4, -2, 0]) -> -3

def centered_average(nums):
	smalls = min(int(x) for x in nums)
	biggie = max(int(x) for x in nums)
	nums.remove(smalls)
	nums.remove(biggie)
	return sum(nums) / len(nums)


# Given an array of ints, return True if the array contains a 2 next to a 2
# somewhere.

# has22([1, 2, 2]) -> True
# has22([1, 2, 1, 2]) -> False
# has22([2, 1, 2]) -> False

def has22(nums):
	for x in range(0, len(nums) - 1):
		if nums[x] == 2 and nums[x+1] == 2:
			return True
	return False

# Given a string, return a new string made of 3 copies of the last 2 chars of
# the original string. The string length will be at least 2.

# extra_end('Hello') -> 'lololo'
# extra_end('ab') -> 'ababab'
# extra_end('Hi') -> 'HiHiHi'

def extra_end(str):
	return str[len(str)-2:]*3 # Splice the string to last two characters and multiply it by 3 

# Given a string, return a version without the first and last char, so "Hello"
# yields "ell". The string length will be at least 2.

# without_end('Hello') -> 'ell'
# without_end('java') -> 'av'
# without_end('coding') -> 'odin'

def without_end(str):
	return str[1:len(str)-1] # Splice string omitting first and last character

# Given a string, return a string where for every char in the original, there
# are two chars.

# double_char('The') -> 'TThhee'
# double_char('AAbb') -> 'AAAAbbbb'
# double_char('Hi-There') -> 'HHii--TThheerree'

def double_char(str):
	result = ""
	for x in range(0, len(str)):
		result += str[x:x+1]*2
	return result


# Return the number of times that the string "code" appears anywhere in the
# given string, except we'll accept any letter for the 'd', so "cope" and
# "cooe" count.

# count_code('aaacodebbb') -> 1
# count_code('codexxcode') -> 2
# count_code('cozexxcope') -> 2

def count_code(str):
	result = 0
	for i in range(0, len(str) - 3):
		if str[i:i+2] == 'co' and str[i+3] == 'e':
			result = result + 1
	return result


# Return the number of times that the string "hi" appears anywhere in the
# given string.

# count_hi('abc hi ho') -> 1
# count_hi('ABChi hi') -> 2
# count_hi('hihi') -> 2

def count_hi(str):
	return str.count('hi')


# Given two strings, return True if either of the strings appears at the very
# end of the other string, ignoring upper/lower case differences (in other
# words, the computation should not be "case sensitive"). Note: s.lower()
# returns the lowercase version of a string.

# end_other('Hiabc', 'abc') -> True
# end_other('AbC', 'HiaBc') -> True
# end_other('abc', 'abXabc') -> True

def end_other(a, b):
	return a[-len(b):].lower() == b.lower() or a.lower() == b[-len(a):].lower()

# Return True if the string "cat" and "dog" appear the same number of times in
# the given string.

# cat_dog('catdog') -> True
# cat_dog('catcat') -> False
# cat_dog('1cat1cadodog') -> True

def cat_dog(str):
	return str.count('cat') == str.count('dog')

# Return True if the given string contains an appearance of "xyz" where the
# xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz"
# does not.

# xyz_there('abcxyz') -> True
# xyz_there('abc.xyz') -> False
# xyz_there('xyz.abc') -> True

def xyz_there(str):
	str = str.replace('.xyz', '')
	return 'xyz' in str

# Now write a Python function
#   def wordCount(str):
#     return <add Python expression here>
# Where the expression should be a single line.  It should produce a Python list (array)
# of three elements:  number of lines in str, number of words in str, and number of chars.

def wordCount(str):
	line_count = str.count('\n')
	word_count = len(str.split(' '))
	char_count = len(str) - str.count(' ')
	return [line_count, word_count, char_count]

# For hw2, we had to rewrite a C program that counts the number of times each
# digit occurs, the number of times a whitespace occurs, and the number of other characters.
# It returns a list of 12 elements (a count for each of the ten digits, plus whitespace,
# plus other characters).
# Do this in Python.

def mycount(str):
	digit_count = [str.count(c) for c in "0123456789 \t\n"]
	digit_count[10] = sum(digit_count[10:13])
	del digit_count[11:13]

	other_count = [0]
	for x in str:
		if x not in "0123456789 \t\n":
			other_count[0] += 1
	# print([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'White Space', 'Other'])
	return digit_count + other_count
