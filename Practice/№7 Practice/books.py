def data(file):
    with open(file, encoding='utf-8') as f:
        data = f.read().splitlines()
    format_data = [i.split('|') for i in data]
    return format_data


def get_totals(list, number):
    otvet = []
    for i in range(1, len(list)):
        if int(list[i][3]) * float(list[i][4]) < number:
            otvet.append((list[i][0], int(list[i][3]) * float(list[i][4]) + 100))
        else:
            otvet.append((list[i][0], int(list[i][3]) * float(list[i][4])))
    return otvet


def get_books(arr, word='python'):
    otvet = []
    for i in arr:
        for j in i:
            if word in j.lower():
                otvet.append(i)
    return otvet
