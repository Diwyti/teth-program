number = int(input("Введите пятизначное число: "))

digit_1 = number // 10000
digit_2 = number // 1000 % 10
digit_3 = number // 100 % 10
digit_4 = number // 10 % 10
digit_5 = number % 10

digit_sum = digit_1 + digit_2 + digit_3 + digit_4 + digit_5
reversed_number = (
	digit_5 * 10000
	+ digit_4 * 1000
	+ digit_3 * 100
	+ digit_2 * 10
	+ digit_1
)

print("Сумма цифр:", digit_sum)
print("Число в обратном порядке:", reversed_number)