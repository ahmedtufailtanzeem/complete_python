class Phone:
	def __init__(self, make, model, price):
		self.make = make
		self.model = model
		self.price = price

	def make_call(self, number):
		print(f"Calling {number}...")


class SmartPhone(Phone):
	def __init__(self, make, model, price, ram, internal_memory, rear_camera):
		super().__init__(make, model, price)
		self.ram = ram
		self.internal_memory = internal_memory
		self.rear_camera = rear_camera


one_plus_4 = SmartPhone("OnePlus", "T", 35000, 4, 16, 20)
one_plus_4.make_call(8888888888)
