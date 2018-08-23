squares_map = {i: i ** 2 for i in range(1, 11)}
print(squares_map)

squares_cubes_map_odd_even = {i: i ** 2 if i % 2 == 0 else i ** 3 for i in range(1, 11)}
print(squares_cubes_map_odd_even)

odd_even = {i: "even" if i % 2 == 0 else "odd" for i in range(1, 11)}
print(odd_even)
