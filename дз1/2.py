spisok = [x**3 for x in range(1001) if x % 2 != 0]
print('Список кубов нечётных чисел {}'.format(spisok))
my_spisok = spisok[:]
sum_numbers = []
sum_numbers_17 = []
for i in my_spisok:
    if sum(map(int, str(i))) % 7 == 0:
        sum_numbers.append(i)
print('1. Сумма чисел, делящихся на 7:', sum(sum_numbers))

my_spisok = [i+17 for i in my_spisok]
for i in my_spisok:
    if sum(map(int, str(i))) % 7 == 0:
        sum_numbers_17.append(i)
print('2. Сумма чисел, делящихся на 7 (+17):', sum(sum_numbers_17))