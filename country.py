coutries = [8.56, 3.5, 139, 32, 23.6, 2.8, 357]

coutries_sort = sorted(coutries)

aver_p = sum(coutries) / len(coutries)
min_p = coutries_sort[0]
max_p = coutries_sort[len(coutries) - 1]
max3 = coutries_sort[(len(coutries) - 3):]

print('Средняя плотность: %.2f' % aver_p)
print('Низкая плотность: ', min_p)
print('Высокая плотность: ', max_p)
print('3 самых больших: ', max3)
