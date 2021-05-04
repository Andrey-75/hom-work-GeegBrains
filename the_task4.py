nun_name = int(input('Введите целое положителье число'))
nun_max = nun_name % 10
nun_name = nun_name // 10
while nun_name > 0:
    if nun_name % 10 > nun_max:
        nun_max = nun_name % 10
    nun_name = nun_name // 10
print(nun_max)
