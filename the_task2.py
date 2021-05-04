name_second = int(input('Введите время в секундах: '))
hour = name_second // 3600
minutes = (name_second % 3600) // 60
second = name_second % 60
print(f'чч:{hour}; мм:{minutes}; сс:{second}')
