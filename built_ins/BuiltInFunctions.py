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


# LISTS

# Sorting a list form low to high
list_1 = [7, 26, 34, 2, 12, 98, 56]
print("sorted: {}".format(sorted(list_1)))

# Getting the max, min, and sum of a list
list_sum = sum(list_1)
print("min: {} max: {}".format(min(list_1), max(list_1)))

# Convert a string to a list where each element is a character
print("list(bob): {}".format(list("bob")))

# You can quickly reverse a list
print("list_1.reverse(): {}".format(list_1.reverse()))


# You can loop through a list's values AND indices simultaneously
for index, value in enumerate(list_1):
    print("index: {} value: {}".format(index, value))


# STRINGS

# Check if a string contains a substring
sentence = "Hi I'm Bob!"
if "Bob" in sentence:
    print("YES")
# Let's take care of those capital letters too, just in case the ### string for "bOb" looks a little bit different ...
if "bOb".lower() in sentence.lower():
    print("YES")
# These two will convert a string to lower and upper case letters
sentence.lower()
sentence.upper()
# Check the properties of your string
sentence.isalpha()  # Alphabetic characters only (no symbols or nums)
sentence.isnumeric()  # Numbers only
sentence.islower()  # Is it all lower case?
sentence.isupper()  # Is it all upper case?
# Clean up your string
sentence.capitalize()  # First char is capitalized
sentence.lstrip()  # Remove whitespace on left side
sentence.rstrip()  # Remove whitespace on right side
sentence.strip()  # Remove whitespace on both sides
# The .join() method can concatenate strings with a separator
# list --> string
str1 = " ".join(["Bob", "has", "a", "balloon"])  # "Bob has a balloon"

# The .split() method does the opposite of .join()
# string --> list
str2 = "Bob has a balloon".split(" ")  # ["Bob","has","a","balloon"]

# The .replace() method can replace a substring with another
str3 = "Bob has a balloon".replace("has", "is")  # "Bob is a balloon"

