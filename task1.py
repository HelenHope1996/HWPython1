# Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод
# Например для числа 145 сумма цифр будет 10: 1 + 4 + 5
# Примеры/Тесты:
# 123 >>> Сумма чисел числа 123 равна 6
# 100 >>> Сумма чисел числа 100 равна 1

num = int(input("Введите трехзначное число:"))
sum = 0


while (num != 0):
    sum = sum + num % 10
    num = num // 10
    
print(f"Сумма цифр числа равна:{sum}")