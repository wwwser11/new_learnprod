# Тренировочная задача по созданию медицинской анкеты
# Не отражает действительность:)

name = input('Введите выдуманное имя: ')
surname = input('Введите выдуманную фамилию: ')
weight = int(input('Введите вес выдуманного человека: '))
age = int(input('Введите возраст выдуманного человека: '))

if age <= 39:
    if weight > 120:
        output = f'Hello, {name} {surname}! Тебе пора следить за собой'
        print(output)
    elif weight >= 50:
        output = f'Prived {surname}!! Good work'
        print(output)
    else:
        output = f'HI. {name} must eat more meat'
        print(output)
else:
    if weight > 120:
        output = f'Hello, {name} {surname}! Тебе пора к врачу'
        print(output)
    elif weight >= 50:
        output = f'Prived {surname}!! Good work'
        print(output)
    else:
        output = f'HI. {name} must eat more meat, но лучше сходи к врачу,а то тебе уже {age} лет и ты весишь всего {weight} кг.'
        print(output)