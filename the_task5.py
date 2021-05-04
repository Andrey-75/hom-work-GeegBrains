proceeds = int(input('Введите значение выручки: ')) #выручка
cost = int(input('Введите значение издержки: '))    #издержка
vprofit = proceeds - cost
prof_1 = cost * 100 / proceeds
if proceeds > cost:
    print('Ваша фирма работает на прибыль в', prof_1,'%')
else:
    print('Ваша фирма работает на убыток')
prof = ((proceeds - cost) / proceeds) * 100
worker = int(input('Сколько сотрудников в фирме? '))
profit_n = vprofit // worker
print('Прибыль в фирме на одного человека: ',profit_n, '')
