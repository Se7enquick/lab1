import xlwt
from datetime import date


def export(name, model, option, general=None):
    options_decode = {
        0: 'Поломок не обнаружено',
        1: 'Утечка горюче-смазочных материалов из систем силового агрегата',
        2: 'Необходим анализ горячих частей двигателя ',
        3: 'Попадание моторного масла в бензин',
        4: 'В бензин попадает охлаждающая жидкость',
        5: 'Необходимо отрегулировать клапаны газораспределительного механизма',
        6: 'Детонация топлива в цилиндрах, необходимо срочное обслуживание двигателя'
    }

    general_decode = {
        1: 'Посторонний запах',
        2: 'Дым при запуске',
        3: 'Посторонние звуки'
    }
    wb = xlwt.Workbook()
    style1 = xlwt.easyxf('font: bold on; align: wrap on, vert top, horiz left')
    style2 = xlwt.easyxf('align: wrap on, vert top, horiz left')
    ws = wb.add_sheet('Отчет о осмотре двигателя')
    ws.write(0, 0, 'Дата проверки', style1)
    ws.write(0, 1, 'Имя оператора', style1)
    ws.write(0, 2, 'Марка авто', style1)
    ws.write(0, 3, 'Найденная проблема', style1)
    ws.write(0, 4, 'Общий анализ', style1)
    ws.write(1, 0, date.today().strftime("%d.%m.%Y"), style2)
    ws.write(1, 1, name, style2)
    ws.write(1, 2, model, style2)
    ws.write(1, 3, general_decode.get(general) if general else 'Нет информации', style2)
    ws.write(1, 4, options_decode.get(option), style2)
    wb.save('report.xlsx')
