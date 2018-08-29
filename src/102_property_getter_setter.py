class Phone:
	def __init__(self, make, model, price):
		self.make = make
		self.model = model
		# What if some set's -ve value, also we said treat this a private and don't use directly
		self._price = max(price, 0)
		# Problem here is if any of the above is updated specification still print's 1st assigned value
		self.specification = f"This a phone from '{self.make}' with model '{self.model}' priced at INR '{self._price}'"

	@property
	# Don't need () and can be used as attribute
	def specs(self):
		return f"This a phone from '{self.make}' with model '{self.model}' priced at INR '{self._price}'"

	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, new_price):
		self._price = max(new_price, 0)


a1 = Phone("Mi", "A1", 13999)
print(a1.specification)

# Assume "A1" price is slash by 1000 yet the earlier specification will print older value
# See the difference between 2 specifications.
a1.price = -12999
print(a1.specs)


# We can still set using and this will work
a1.price = -12999