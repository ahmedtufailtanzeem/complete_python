class Car:
	def __init__(self, make, model, price):
		self.make = make
		self.model = model
		self.price = price

	def drive(self):
		print(f"Driving ...")

	def brake(self):
		print(f"Coming to stop...")


class HatchBack(Car):
	def __init__(self, make, model, price, seats):
		super().__init__(make, model, price)
		self.seats = seats

	def hatch(self):
		print(f"Hatch hatch...")


class HatchBackSuv(HatchBack):
	def __init__(self, make, model, price, seats, roof):
		super().__init__(make, model, price, seats)
		self.roof = roof

	def hatch(self):
		print(f"Hatch hatch Suv Suv...")

	def suv(self):
		print(f"Suv Suv...")


c = Car("Honda", "CRV", 200000)
h = HatchBack("Maruthi", "Swift", 400000, 5)
s = HatchBackSuv("Hyundai", "i20", 600000, 5, True)

# Print attributes
print(s.__dict__)
# Print Method resolution
print(help(s))

s.hatch()

print(isinstance(s, HatchBackSuv))
print(isinstance(s, HatchBack))
print(isinstance(s, Car))

print(isinstance(h, HatchBackSuv,))
print(isinstance(h, (HatchBackSuv, Car)))


print(issubclass(HatchBackSuv, HatchBack))
print(issubclass(HatchBackSuv, Car))
