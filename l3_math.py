import math
radius = float(input("Введите радиус круга в сантиметрах "))

lenght = 2*math.pi*radius
area = math.pi * radius**2
print(f"Длина окружности: {int(lenght/100)} метров и {lenght%100} сантиметров")
print(f"Площадь окружности: {int(area/100)} метров и {area%100} сантиметров")

squareV = radius * (2**0.5)
triangleV = radius * (3**0.5)
print(f"Длина стороны квадрата , вписанного в окружность: {int(squareV /100)} метров и {squareV %100} сантиметров")
print(f"Длина стороны равностороннего треугольника , вписанного в окружность: {int(triangleV/100)} метров и {triangleV%100} сантиметров")

squareO = radius * 2
triangleO = 2 * radius * (3**0.5)
eightUgol = 2*radius * (2**0.5 - 1)
print(f"Длина стороны квадрата , описанного около окружности: {int(squareO /100)} метров и {squareO %100} сантиметров")
print(f"Длина стороны равностороннего треугольника , описанного около окружности: {int(triangleO/100)} метров и {triangleO%100} сантиметров")
print(f"Длина стороны правильного восьмиугольника , описанного около окружности: {int(eightUgol/100)} метров и {triangleO%100} сантиметров")


