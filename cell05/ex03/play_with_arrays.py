numbers = [2, 8, 9, 48, 8, 22, -12, 2]
print(numbers)
transformed = {x + 2 for x in numbers if x + 2 > 9}
print(transformed)