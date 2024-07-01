# start = int(input("Введіть початок діапазону: "))
# end = int(input("Введіть кінець діапазону: "))

# sum_even = 0
# count_even = 0

# sum_odd = 0
# count_odd = 0

# sum_multiples_of_9 = 0
# count_multiples_of_9 = 0

# for number in range(start, end + 1):
#     if number % 2 == 0:
#         sum_even += number
#         count_even += 1
#     if number % 2 != 0:
#         sum_odd += number
#         count_odd += 1
#     if number % 9 == 0:
#         sum_multiples_of_9 += number
#         count_multiples_of_9 += 1

# average_even = sum_even / count_even if count_even > 0 else 0
# average_odd = sum_odd / count_odd if count_odd > 0 else 0
# average_multiples_of_9 = sum_multiples_of_9 / count_multiples_of_9 if count_multiples_of_9 > 0 else 0

# print(f"Сума парних чисел: {sum_even}")
# print(f"Середньоарифметичне парних чисел: {average_even}")

# print(f"Сума непарних чисел: {sum_odd}")
# print(f"Середньоарифметичне непарних чисел: {average_odd}")

# print(f"Сума чисел, кратних 9: {sum_multiples_of_9}")
# print(f"Середньоарифметичне чисел, кратних 9: {average_multiples_of_9}")

# length = int(input("Введіть довжину лінії: "))
# symbol = input("Введіть символ для заповнення лінії: ")


# for i in range(length):
#     print(symbol)
# while True:
#     number = int(input("Введіть число: "))

#     if number == 7:
#         print("Good bye!")
#         break
#     elif number > 0:
#         print("Number is positive")
#     elif number < 0:
#         print("Number is negative")
#     else:
#         print("Number is equal to zero")
# sum_numbers = 0
# max_number = None
# min_number = None

# while True:
#     number = int(input("Введіть число: "))

#     if number == 7:
#         print("Good bye!")
#         break

#     sum_numbers += number

#     if max_number is None or number > max_number:
#         max_number = number

#     if min_number is None or number < min_number:
#         min_number = number

# print(f"Сума введених чисел: {sum_numbers}")
# print(f"Максимум введених чисел: {max_number}")
# print(f"Мінімум введених чисел: {min_number}")
