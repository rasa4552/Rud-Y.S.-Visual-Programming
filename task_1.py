numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers_new = numbers[:4] + numbers[5:]
a = sum(numbers_new) / len(numbers)
numbers[4] = a
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
