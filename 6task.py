list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Поменяйте местами значения согласно условию
max_value = list_numbers[0]  # предполагаемый максимум
last_max_index = 0           # индекс последнего максимума

# Проходим по списку начиная со второго элемента
for i, num in enumerate(list_numbers):
    if num >= max_value:
        max_value = num
        last_max_index = i

last_element_index = len(list_numbers) - 1

list_numbers[last_max_index], list_numbers[last_element_index]= list_numbers[last_element_index], list_numbers[last_max_index]
print(list_numbers)
# Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
