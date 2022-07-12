my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
lenght_spisok:int = len(my_list)

for i in range(lenght_spisok):
    elem = my_list.pop(0)

    if elem.isdigit() and elem.isalnum():
        my_list.append(f'"{int(elem):02d}"')

    elif elem[0] == "+" and elem[1].isdigit():
        my_list.append(f'"+{int(elem):02d}"')

    else:
        my_list.append(elem)

print(' '.join(my_list))
