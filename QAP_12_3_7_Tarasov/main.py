# ЗАДАНИЕ 12.7.3.
a, b, c, d = 5.6, 5.9, 4.28, 4.0 #определяем значение переменных
per_cent = {'ТКБ': a, 'СКБ': b, 'ВТБ': c, 'СБЕР': d} #список % по банкам
money = input("введите сумму депозита : ") #определяем сумму вклада
m = (float(money)) #преобразуем  строку в число, с плавующей запятой
deposit = [] # создаем список deposit
a1, b1, c1, d1 = (a * m / 100), (b * m / 100), (c * m / 100), (d * m / 100) #вычисляем % за год
deposit = [a1, b1, c1, d1] #формируем список значений накоплений
i = max (deposit) #определяем максимальное значение списка
i = round(i,2) #округляем до 2х знаков после запятой
print ("Максимальная сумма, которую вы можете заработать - " , i) # печать максимального значения

