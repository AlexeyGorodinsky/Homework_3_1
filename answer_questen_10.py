
mass = [12, 10, 24, 5, 6, 8, 9, 10, 50, 24, 48]

new_mass = [i ** 3 for i in mass if i % 3 == 0 and i % 4 == 0]

print(new_mass)

# [1728, 13824, 13824, 110592]
