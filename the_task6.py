kilo_name_1 = int(input('Скольк километров вы пробежали?'))
kilo_name_2 = int(input('Сколько километров вы хотите пробегать?'))
day = 1
if kilo_name_1 > kilo_name_2:
    print(day)
while kilo_name_1 < kilo_name_2:
    kilo_name_1 = kilo_name_1 + kilo_name_1 / 10
    day += 1
    print(day,"день:", '{:.3f}'.format(kilo_name_1))
