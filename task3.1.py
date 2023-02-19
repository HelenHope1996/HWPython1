# ``(*)``` **Усложнение.** Вывод результат на экран сделайте одной строкой(только один print), 
# для этого используйте тернарный оператор.

ticket = int(input("Введите номер билета:"))

sum1 = 0
sum2 = 0
for i in range(6):
    if i < 3:
        sum1 += ticket // 10**i % 10
    else:
        sum2 += ticket // 10**i % 10 
print("YES") if (sum1==sum2) else print("NO")