# Encapsulation : Keep data and its relevant methods in same class

# Abstraction : Hide the inner working and just expose a way.

# Encapsulation & Abstraction go hand in hand and can not be separated

# Naming convention - No concept of Private, Protected and default.. Every thing is PUBLIC
	# _name : Treat is as private
	# __name__ : dunder/magic methods

# Name Mangling : Python changes __var to _Class__var? Let's wait for the reason

class Test:
	def __init__(self):
		self.__x = 5

t = Test()
print(t.__dict__)
print(t._Test__x)