# City A temperatures
city_a = [25, 28, 30, 27, 26, 29, 31]

# City B temperatures
city_b = [20, 35, 25, 40, 18, 32, 22]

# Find minimum and maximum manually
min_a = city_a[0]
max_a = city_a[0]

for x in city_a:
    if x < min_a:
        min_a = x
    if x > max_a:
        max_a = x

min_b = city_b[0]
max_b = city_b[0]

for x in city_b:
    if x < min_b:
        min_b = x
    if x > max_b:
        max_b = x

# Calculate range
range_a = max_a - min_a
range_b = max_b - min_b

print("Range - City A:", range_a)
print("Range - City B:", range_b)