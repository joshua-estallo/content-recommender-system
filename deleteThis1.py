numbers = [5, 3, -2, 1, 4]

print(numbers)
print(sorted(numbers, key= lambda x: x*x))


# Sort a list of strings in alphabetical order by their length:
strings = ["apple", "banaasdfna", "cherry", "orange"]
sorted_strings = sorted(strings, key=len)
print(sorted_strings)