# Almost identical to List except for using {}

names = ["Maira", "Nusayba", "Adiva", "Manha", "Ammara"]
short_names = {name[:3] for name in names}
print(short_names)
