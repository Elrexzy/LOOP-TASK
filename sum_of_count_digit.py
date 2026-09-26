numbers = int(input("Enter the number: "))
digit_sum = 0

while numbers > 0:
    last_digit = numbers % 10
    numbers //= 10
    digit_sum += last_digit

print("The sum of the digits is:", digit_sum)
