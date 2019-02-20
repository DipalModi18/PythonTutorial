# all(iterable) - Return True if all elements of the iterable are true (or if the iterable is empty).
print("all([True, True, True]): ", all([True, True, True]))
print("all([True, False, True]): ", all([True, False, True]))
print("all([x>5 for x in range(1, 10)]): ", all([x > 5 for x in range(1, 10)]))
print("all([x>5 for x in range(6, 10)]): ", all([x > 5 for x in range(6, 10)]))


print()
# any(iterable) - Return True if any element of the iterable is true. If the iterable is empty, return False.
print("any([False, False, False]): ", any([False, False, False]))
print("any([True, False, True]): ", any([True, False, True]))
print("any([x>5 for x in range(1, 10)]): ", any([x > 5 for x in range(1, 10)]))
print("any([x>5 for x in range(6, 10)]): ", any([x > 5 for x in range(6, 10)]))



