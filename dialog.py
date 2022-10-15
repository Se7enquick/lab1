from export_xls import export


def dialog():
    print('Приветствуем в автоматизированной системе "Автосервис. Диагностика неисправностей двигателя"')
    name = input('Укажите ваше имя: ')
    model = input('Укажите модель авто: ')
    print('Попробуйте запустить двигатель в аварийном режиме')
    start_point = int(input('Двигатель завелся без проблем? введите цифру 1 если да, 2 если нет \n'))
    if start_point == 1:
        print('С двигателем все хорошо, отчет сформирован')
        option = 0
        return export(name=name, model=model, option=option)
    else:
        print('Проведите ручную диагностику и по окончанию ответьте на вопрос ниже...')
    general = int(input('Что удалось обнаружить? Вводите цифру в поле ниже: \n'
                        '1: Посторонний запах \n'
                        '2: Дым при запуске \n'
                        '3: Посторонние звуки \n'
                        ))
    if general == 1:
        option = int(input('Укажите подробнее о поломке: \n'
                           '1: Запах моторного масла или запах топлива \n'
                           '2: Запах жженой резины \n'))
    elif general == 2:
        answer = int(input('Укажите подробнее о поломке: \n'
                           '1: Дым синего цвета \n'
                           '2: Дым белого цвета \n'))
        if answer == 1:
            option = 3
        else:
            option = 4
    else:
        answer = int(input('Укажите подробнее о поломке: \n'
                           '1: Стук \n'
                           '2: Треск \n'))
        if answer == 1:
            option = 5
        else:
            option = 6
    print('Отчет сформирован, спасибо за ответы.')
    return export(name=name, model=model, general=general, option=option)
