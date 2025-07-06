# Tuples

my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)
print(my_tuple[0])
print(my_tuple[2])
print(my_tuple[-1])

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

conc_tuple = tuple1 + tuple2 # to add the 2 is conc

print(conc_tuple)

rep_tuple = tuple1 * 3 # to multiply or use the same multiple times

print(rep_tuple)

# Tuples - We can't add, we can't remove, it's unchangeable.
# Tuples are suitable for situations when we want to store a collection of elements that should not be changed
# throughout your programs execution. common uses - storing fixed collections of data such as coordinates, R, G, B
# codes, database records.
