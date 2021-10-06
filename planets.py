planets = {'Меркурий': 57910006,
           'Венера': 108199995,
           'Земля': 149599951,
           'Марс': 227939920,
           'Юпитер': 778330257,
           'Сатурн': 1429400028,
           'Уран': 2870989228,
           'Нептун': 4504299579,
           }

AverToSun = sum(list(planets.values())) / len(planets)
SortPlanet = sorted(list(planets.keys()))
Dist = planets['Нептун'] / planets['Земля']

print('Средняя расстояние: ', AverToSun)
print('Сортированные названия: ', SortPlanet)
print('Нептун дальше чем Земля в : %.1f раз' % Dist)