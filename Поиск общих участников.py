# TODO Напишите функцию find_common_participants
def find_common_participants(group_1, group_2, delimiter='|'):
    participants_1 = set(group_1.split(delimiter))
    participants_2 = set(group_2.split(delimiter))
    common_participants = participants_1 & participants_2
    return list(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group)

print("Общие участники:", ', '.join(common_participants))