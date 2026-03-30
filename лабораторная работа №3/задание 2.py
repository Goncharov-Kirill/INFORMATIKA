def find_common_participants(group1, group2, delim = ','):
    lst1 = group1.split(delim)
    lst2 = group2.split(delim)
    common = []
    for el in lst1:
        if el in lst2 and el not in common:
            common.append(el)
    common.sort()
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_second_group, participants_second_group)# TODO Провеьте работу функции с разделителем отличным от запятой
print('общие участники:', participants)