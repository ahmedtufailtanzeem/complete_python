class Person:
	instance_count = 0

	def __init__(self, first_name, last_name, age):
		Person.instance_count += 1
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	# Class method
	@classmethod
	def get_instance_count(cls):
		return f"{cls.__name__} instance = {cls.instance_count}"

	# Class method as constructor
	@classmethod
	def from_string(cls, string):
		first, last, age = string.split(",")
		return cls(first, last, age)

	@staticmethod
	def static_method():
		return Person.get_instance_count()


tanz = Person('Tanzeem', 'Ahmed', 31)
print(f"{tanz.first_name} - {tanz.last_name} : {tanz.age}")

nussi = Person('Nusayba', 'Tanzeem', 3)
print(f"{nussi.first_name} - {nussi.last_name} : {nussi.age}")

ammu = Person.from_string("Ammara,Tanzee,1")
print(ammu)
print(Person.get_instance_count())
print(Person.static_method())
print(ammu.static_method())












# Method are generally referred to when they are inside a class in OOP. If util's they are referred to Functions

# below demonstrate a way of overwriting a global variable.
# First check if instance variable is present if not check if Global is present
# If both fails Generate an Exception
class Circle:
	pi = 3.14

	def __init__(self, radius):
		self.radius = radius

	def calculate_circumference(self):
		return self.pi * (self.radius ** 2)


normal_circle = Circle(5)
print(f"Normral circle R: {normal_circle.radius} C {normal_circle.calculate_circumference()} ")
print(normal_circle.__dict__)
abnormal_circle = Circle(5)
print(abnormal_circle.__dict__)
print(f"Abnormral circle R: {abnormal_circle.radius} C {abnormal_circle.calculate_circumference()} ")

# Let's overwrite the pi
abnormal_circle.pi = 4
print(abnormal_circle.__dict__)
print(f"Abnormral circle R: {abnormal_circle.radius} C {abnormal_circle.calculate_circumference()} ")

print(Circle.calculate_circumference(normal_circle))
