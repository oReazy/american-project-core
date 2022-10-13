License = ['❌ Отсутствует', '❌ Отсутствует', '❌ Отсутствует', '❌ Отсутствует', '❌ Отсутствует', '❌ Отсутствует', '❌ Отсутствует', '❌ Отсутствует']
inventory = [0, 0, 0, 0, 0, 0, 0]
clothes = ['Пусто', 'Пусто', 'Пусто', 'Пусто', 'Пусто', 'Пусто']
admin_info = ['', '', '', '', '', '', '',  '', '', '']
VIP_table = ['no vip', 0]

NAME = ['vk_id', 'state', 'nick', 'mail', 'telephone', 'lvl', 'exp', 'sex', 'age', 'nationality', 'admin', 'dollars', 'euro', 'yen', 'pounds', 'bank_dollars', 'bank_euro', 'bank_yen', 'bank_pounds', 'donate', 'VIP', 'member', 'rang', 'license', 'warns', 'clothes', 'work', 'fighting', 'skillArmor', 'skillWorks', 'blacklist', 'history_punish', 'history_nicks', 'history_reports', 'passport', 'passport_serial', 'passport_number', 'marriage', 'military_card', 'admin_info', 'mailing_project', 'mailing_server', 'bank_card', 'temporary_var', 'limit_report', 'last_message', 'reDesign', 'inventory', 'family', 'timeEventCollectors', 'notes_telephone', 'promocode', 'warn_fraction', 'temporary_var2']
VALUES = ['ID ПОЛЬЗОВАТЕЛЯ', '', 'На этапе регистрации', '❌ Отсутствует', '❌ Отсутствует', '1', '0', 'Не выбран', '0', 'Не выбран', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', f'\"{VIP_table}\"', 'Без организации', '0', f'\"{License}\"', '[]', f'\"{clothes}\"', 'Безработный', '[0, 0, 0, 0, 0]', '[0, 0, 0, 0]', '[0, 0, 0, 0, 0]', '[]', '[]', '[]', '[]', '❌ Отсутствует', '0', '0', 'Не женат(а)', '❌ Отсутствует', f'\"{admin_info}\"', '❌ Не подписан', '❌ Не подписан', '❌ Отсутствует', '', '0', '0', '0', f'\"{inventory}\"', '-1', '0', '❌ Заметок нет', '', '0', '']

res = input('---------------------------------------------------------\n'
            '1 - ПРОВЕРИТЬ МЕСТА ПЕРЕМЕННЫХ\n'
            '2 - ПОЛУЧИТЬ РЕЗУЛЬТАТ SQL\n'
            '---------------------------------------------------------\n')
print('---------------------------------------------------------')
if int(res) == 1:
    i = 0
    for item in NAME:
        print(f'{i + 1} | {item}: {VALUES[i]}')
        i = i + 1

if int(res) == 2:
    STR_NAMES = ''
    for item in NAME:
        STR_NAMES = f'{STR_NAMES}, {item}'
    STR_VALUES = ''
    for item in VALUES:
        STR_VALUES = f"{STR_VALUES}, '{item}'"
    print(f'"INSERT INTO `users` ({STR_NAMES}) VALUES ({STR_VALUES})"')