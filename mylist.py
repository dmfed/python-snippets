'''
Inheritance example
'''

class MyList(list):
	def indexes(self, elem):
		'''
		Same as index() method in the original list
		but returns indixes of all matching elements
		'''
		return tuple(i for i in range(len(self)) if self[i] == elem)
		
a = [1, 2, 3, 4, 5, 3, 6, 7, 8, 3]
b = MyList(a)
c = MyList([1, 2, 2, 2, 1])

print(b.index(3))
print(b.indexes(3))
print(c.indexes(2))
