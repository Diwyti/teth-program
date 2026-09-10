
number = input("Введите трехзначное число: ")
number = int(number)

cifra1 = number // 100
cifra2 = (number // 10) % 10
cifra3 = number % 10


result = cifra3 * 100 + cifra2 * 10 + cifra1

print("Число в обратном порядке:", result)
