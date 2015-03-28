#!/usr/bin/python

import sys
import time
from random import randint


class Quick3way():
	"""
	Quick3Way is a Python miniLibrary to assist in running a list through
	the Quick3 sorting algorithm.

	The use of 'random' and 'time' is just while testing.
	"""

	def __init__(self, array, v=0):
		"""
		:param array: The array you wish to sort.
		:param v: Verbosity. None is default.
		:return: Nothing
		"""
		self._array = array
		self._array_len = len(self._array) - 1
		self._sorted = ""
		self._verbosity = v

		# Globals
		self.ERR = -1
		self.SUCCESS = 0


	def sort(self):
		"""
		Will call the sorter and return the sorted array + time if mentioned.
		:return: Struct with array and timing information.
		"""
		if self._verbosity == 1:
			"""
			Verbosity is marked on
			So i will be checking for time performance
			"""
			start = time.clock()
			self.sort3way(self._array, 0, self._array_len)
			end = time.clock()
			return {"Start": start, "End": end, "Duration": (end - start) / 1000, "Array": self._sorted}

		else:
			self.sort3way(self._array, 0, self._array_len)
			return self._sorted



	def sort3way(self, array, lo, hi):
		"""
		This function does the actual sorting.
		It will receive an array with init vector and max size.
		It will return the output to the global array.
		:param array: Array to sort.
		:param lo: Starting item of the list
		:param hi: Ending element of the list
		:return:to self._sorted
		"""

		if lo >= hi:
			return self.ERR

		pivot = array[lo]
		gt = hi
		lt = lo
		i = lo + 1

		while i <= gt:
			if array[i] < pivot:
				array[i], array[lt] = array[lt], array[i]
				lt += 1
				i += 1
			elif array[i] > pivot:
				array[i], array[gt] = array[gt], array[i]
				gt -= 1
			else:
				i += 1

		self.sort3way(array, lo, lt - 1)
		self.sort3way(array, gt + 1, hi)

		self._sorted = array
		return self.SUCCESS


class TestStructs():
	"""
	This class is just for testing performance of the Quick3 sort process.
	"""
	def __init__(self):
		"""
		Just zeroing avgArray. Returns nothing.
		:return:
		"""
		self._avgArray = []


	def RunTest(self, array_size, number_of_tests, dbg=0):
		"""
		Since this is a different class from the QuickSort if will need parameters to be fed to it
		manually. This is run tests on performance of said class.
		:param array_size: Size of arrays to create.
		:param number_of_tests: Number of arrays to create and sort.
		:param dbg: Whether debugging mode is enabled. Default is 0.
		:return:Output based on result. Either array or indexed list in debugging.
		"""
		i = 1
		arr = []
		while i <= number_of_tests:
			for c in range(0, array_size):
				arr.append(randint(1, 20))

			a = Quick3way(arr, dbg)

			tmp = a.sort()

			if dbg == 1:
				self._avgArray.append({"Index": i, "Duration": tmp["Duration"], "Length": len(arr)})
			else:
				print tmp

			# Zeroing and incrementing
			arr = []
			c = ""
			i += 1

	def CalcAvg(self):
		"""
		CalcAvg will calculate the results of the tests to see what are the real
		performance of the class.
		:return:Nothing.
		"""

		total = 0
		items = 0
		total_length = 0

		for each in self._avgArray:
			# print str(each["Index"]) + ":" + str(each["Duration"]) + ":" + str(each["Length"])
			items += 1
			total += each["Duration"]
			total_length += each["Length"]

		print "Total of %s arrays sorted at an average of %s each.\nAvarage array length is %s." \
		      % (items, (total/items), (total_length/items))
		print "Total sorting time: %s seconds" % total


if __name__ == "__main__":
	print "This class should not be ran as standalone."
	print "But if we're already here here is how to use it:"
	print """
		a = TestStructs()
		a.RunTest(10000, 10, 1)
		a.CalcAvg()"""
	a = TestStructs()
	a.RunTest(10000, 10, 1)
	a.CalcAvg()
	sys.exit(0)
