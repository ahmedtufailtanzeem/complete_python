# Operators in Python
print("Operators in Python")
print(2 + 2)
print(2 * 2)
print(2 - 2 * 5)
print(4 / 2)
print(8 // 2)
print(2 ** 4)
print(round(22 / 7))
print(round(22 / 7, 2))
print(48 % 7)

# Precedence and Associativity
# ()
# ** R --> L
# *,/,//,% L --> R
# +, - L --> R

print("Precedence and Associativity")
print((2 + 3) * 4 / 2 % 7 + (7 + 4))
# R --> L Associativity
print(2 ** 3 ** 2)


# Short hand

x = 2
x +=4
x *=4
print(x)
