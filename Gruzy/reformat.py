import csv

with open("Data2.csv", mode='w') as write_file:
    fieldnames = [
        'Область',
        'Направление',
        'Транспорт',
        'Вес',
        'Загрузка',
        'Разгрузка',
        'Дата добавления',
        'Название компании',
        'Ставка',
        'Контакты'
    ]
    writer = csv.DictWriter(write_file, delimiter=';', fieldnames=fieldnames)
    writer.writeheader()

for i in range(1, 42):
    data = []
    with open(f"{i}.csv", mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            if len(row) > 7:
                try:
                    contacts = row[9]
                except IndexError:
                    contacts = ""
                data.append({
                    'Область': row[0],
                    'Направление': row[1],
                    'Транспорт': row[2],
                    'Вес': row[3],
                    'Загрузка': row[4],
                    'Разгрузка': row[5],
                    'Дата добавления': row[6],
                    'Название компании': row[7],
                    'Ставка': row[8],
                    'Контакты': contacts
                })

    with open("Data2.csv", mode='a') as write_file:
        fieldnames = [
            'Область',
            'Направление',
            'Транспорт',
            'Вес',
            'Загрузка',
            'Разгрузка',
            'Дата добавления',
            'Название компании',
            'Ставка',
            'Контакты'
        ]
        writer = csv.DictWriter(write_file, delimiter=';', fieldnames=fieldnames)
        writer.writerows(data)
