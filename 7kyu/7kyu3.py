def square_digits(num):
    squared_digits = ''.join(str(int(digit) ** 2) for digit in str(num))
    return int(squared_digits)

print(square_digits(9119))
print(square_digits(765))