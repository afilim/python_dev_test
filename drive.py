fuel_consumption_for_100_kilometers = 6.2
fuel_left = 0.54
fuel_tank_liters = 40

# Нужно написать код вычисления
left_liters = fuel_tank_liters * fuel_left
kilometers_can_drive = (left_liters / fuel_consumption_for_100_kilometers) * 100

print('%.2f' % kilometers_can_drive)
