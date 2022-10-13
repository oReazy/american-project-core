import asyncio
import json, re
import random, datetime

import aiomysql

loop = asyncio.get_event_loop()

# ---------------------------------------------------------------------------------------

USER = 'oreazygb_bot'
PASSWORD = 'Cloud9d'
HOST = 'oreazygb.beget.tech'
DATABASE = 'oreazygb_bot'

# ---------------------------------------------------------------------------------------

async def connect_base():  # Подключение к БД
    connected = await aiomysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        db=DATABASE,
        loop=loop,
        port=3306
    )
    return connected


async def registerNewAccaunt(user_id):  # Создание нового аккаунта в базе данных
    try:
        # ADMIN INFO
        # ------------------------------------------------------------
        # [0] = ИМЯ АДМИНИСТРАТОРА
        # [1] = СКОЛЬКО ЛЕТ АДМИНИСТРАТОРУ
        # [2] = ГОРОД ПРОЖИВАНИЯ АДМИНИСТРАТОРА
        # [3] = TELEGRAM НИК
        # [4] = ДАТА ПОСТАНОВЛЕНИЯ В АДМИНИСТРАТОРЫ
        # [5] = ЛОГИ ДЕЙСТВИЙ НАД АДМИНИСТРОРОМ
        # [6] = ДАТА СНЯТИЕ АДМИНИСТРАТОРА
        # [7] = ПРИЧИНА СНЯТИЯ
        # [8] = СТАТУС АДМИНИСТРАТОРА
        # [9] = ОСОБАЯ ДОЛЖНОСТЬ АДМИНИСТРАТОРА
        # ------------------------------------------------------------
        admin_info = ['', '', '', '', '', '', '', '', '', '']

        # VIP
        # ------------------------------------------------------------
        # [0] = НАЗВАНИЕ VIP
        # [1] = СРОК ДЕЙСТВИЯ VIP (ЕСЛИ БУДЕТ -100, ТО ВЕЧНАЯ)
        # ------------------------------------------------------------
        VIP_table = ['no vip', '0']

        License = ['❌ Отсутствует', '❌ Отсутствует', '❌ Отсутствует', '❌ Отсутствует', '❌ Отсутствует', '❌ Отсутствует',
                   '❌ Отсутствует', '❌ Отсутствует']
        clothes = ['Пусто', 'Пусто', 'Пусто', 'Пусто', 'Пусто', 'Пусто']
        inventory = [0, 0]


        connection = await connect_base()
        async with connection.cursor() as cursor:
            new_user = "INSERT INTO `users` (vk_id, state, nick, mail, telephone, lvl, exp, sex, nationality, admin, dollars, bank_dollars, donate, VIP, member, rang, license, warns, clothes, work, fighting, skillArmor, skillWorks, blacklist, history_punish, history_nicks, history_reports, passport, passport_serial, passport_number, marriage, military_card, admin_info, mailing_project, mailing_server, bank_card, temporary_var, limit_report, last_message, reDesign, inventory, family, timeEventCollectors, notes_telephone, promocode, temporary_var2) VALUES " \
                       f"('{user_id}', " \
                       f"'', " \
                       f"'На этапе регистрации', " \
                       f"'❌ Отсутствует', " \
                       f"'❌ Отсутствует', " \
                       f"'1', " \
                       f"'0', " \
                       f"'Пол не установлен!', " \
                       f"'Национальность не установлена!', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"\"{VIP_table}\", " \
                       f"'Без организации', " \
                       f"'0', " \
                       f"\"{License}\", " \
                       f"'[]', " \
                       f"\"{clothes}\", " \
                       f"'Безработный', " \
                       f"'[0, 0, 0, 0, 0]', " \
                       f"'[0, 0, 0, 0]', " \
                       f"'[0, 0, 0, 0, 0]', " \
                       f"'[]', " \
                       f"'[]', " \
                       f"'[]', " \
                       f"'[]', " \
                       f"'❌ Отсутствует', " \
                       f"'0', " \
                       f"'0', " \
                       f"'Не женат(а)', " \
                       f"'❌ Отсутствует', " \
                       f"\"{admin_info}\", " \
                       f"'❌ Не подписан', " \
                       f"'❌ Не подписан', " \
                       f"'❌ Отсутствует', " \
                       f"'', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"\"{inventory}\", " \
                       f"'-1', " \
                       f"'0', " \
                       f"'❌ Записей нет', " \
                       f"'', " \
                       f"''" \
                       f")"
            await cursor.execute(new_user)
            await connection.commit()
            connection.close()
            print(f'\033[38m[\033[33m!\033[38m][\033[33mDEBUG\033[38m] Встречайте нового пользователя')
            # [{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}]
    except Exception as ex:
        print(f'\033[38m[\033[31m!\033[38m][\033[33mDEBUG\033[38m] Не удалось создать пользователя, причина: {ex}')


async def getUserData(user_id):  # получение данных пользователя
    connection = await connect_base()
    async with connection.cursor() as cursor:
        select_row = f"SELECT * FROM `users` WHERE `vk_id` = {user_id}"
        await cursor.execute(select_row)
        rows = await cursor.fetchall()
        for row in rows:
            data = row
        connection.close()
    return data


async def setUserData(user_id, key, value):  # Изменение переменных у пользователя (по одной переменной)
    connection = await connect_base()
    async with connection.cursor() as cursor:
        update_row = f"UPDATE `users` SET {key} = {value} WHERE vk_id = {user_id}"
        await cursor.execute(update_row)
        await connection.commit()
        connection.close()


async def setMultiUserData(user_id, value):  # Изменение переменных у пользователя (несколько переменных)
    connection = await connect_base()
    async with connection.cursor() as cursor:
        update_row = f"UPDATE `users` SET {value} WHERE vk_id = {user_id}"
        await cursor.execute(update_row)
        await connection.commit()
        connection.close()


async def deleteUserData(user_id):  # Удаление данных пользователя
    connection = await connect_base()
    async with connection.cursor() as cursor:
        delete_row = f"DELETE from `users` WHERE `vk_id` = {user_id}"
        await cursor.execute(delete_row)
        await connection.commit()
        connection.close()


async def findBaseData(key, value):  # найти значения в базе данных. Выводит их количестве в БД
    count_row = 0
    connection = await connect_base()
    async with connection.cursor() as cursor:
        select_row = f"SELECT * FROM `users` WHERE `{key}` = {value}"
        await cursor.execute(select_row)
        rows = await cursor.fetchall()
        for row in rows:
            count_row = count_row + 1
        connection.close()
    return count_row




async def findBaseDataSetting(table, where_key, where_value):  # найти значения в базе данных. Выводит их количестве в БД
    count_row = 0
    connection = await connect_base()
    async with connection.cursor() as cursor:
        select_row = f"SELECT * FROM `{table}` WHERE `{where_key}` = {where_value}"
        await cursor.execute(select_row)
        rows = await cursor.fetchall()
        for row in rows:
            count_row = count_row + 1
        connection.close()
    return count_row



async def yourSQL(sql):  # получение данных пользователя
    connection = await connect_base()
    async with connection.cursor() as cursor:
        select_row = f"{sql}"
        await cursor.execute(select_row)
        rows = await cursor.fetchall()
        connection.close()
    return rows


# --------------------------------------------------------------------------------------------------

async def getBdData(table, key, value):  # получение данных (выводит только последнее)
    connection = await connect_base()
    async with connection.cursor() as cursor:
        select_row = f"SELECT * FROM `{table}` WHERE {key} = {value}"
        await cursor.execute(select_row)
        rows = await cursor.fetchall()
        for row in rows:
            data = row
        connection.close()
    return data


async def getMultiBdData(table, key, value):  # получение данных (выводит все)
    connection = await connect_base()
    async with connection.cursor() as cursor:
        select_row = f"SELECT * FROM `{table}` WHERE {key} = {value}"
        await cursor.execute(select_row)
        rows = await cursor.fetchall()
        connection.close()
    return rows


async def getMultiProgramBdData(table, where):  # получение данных (программное)
    connection = await connect_base()
    async with connection.cursor() as cursor:
        select_row = f"SELECT * FROM `{table}` WHERE {where}"
        await cursor.execute(select_row)
        rows = await cursor.fetchall()
        connection.close()
    return rows


async def setBdData(table, where_key, where_value, key, value):  # Изменение переменных (по одной переменной)
    connection = await connect_base()
    async with connection.cursor() as cursor:
        update_row = f"UPDATE `{table}` SET {key} = {value} WHERE {where_key} = {where_value}"
        await cursor.execute(update_row)
        await connection.commit()
        connection.close()


async def setMultiDbData(table, where_key, where_value, value):  # Изменение переменных (несколько переменных)
    connection = await connect_base()
    async with connection.cursor() as cursor:
        update_row = f"UPDATE `{table}` SET {value} WHERE {where_key} = {where_value}"
        await cursor.execute(update_row)
        await connection.commit()
        connection.close()


async def addMultiBdData(table, keys, values):  # Изменение переменных (по одной переменной)
    connection = await connect_base()
    async with connection.cursor() as cursor:
        update_row = f"INSERT INTO `{table}` ({keys}) VALUES ({values})"
        await cursor.execute(update_row)
        await connection.commit()
        connection.close()









async def newDataInBase(table, keys, values):  # Создание нового аккаунта в базе данных
    try:
        connection = await connect_base()
        async with connection.cursor() as cursor:
            new_data = f"INSERT INTO `{table}` ({keys}) VALUES ({values})"
            await cursor.execute(new_data)
            await connection.commit()
            connection.close()
    except Exception as ex:
        print(f'\033[38m[\033[31m!\033[38m][\033[33mDEBUG\033[38m] Произошла ошибка в базе данных: {ex}')



















# ----------------------------------------------------------------------------------------------------------------------
# Код который ниже написан не связан с базами данных


async def exitBot():  # делает выход из активной переписки
    return
    # try:
    #     exit(0)
    # except:
    #     pass


async def pretty(num):
    num1 = re.sub(r'\d(?=(?:\d{3})+(?!\d))', r'\g<0> ', str(num))
    return num1


async def regularCheck(key, value):
    # data = database.getUserData(message.from_id)
    # database.setUserData(message.from_id, 'state', "'settings.addMail_check'")
    validate = re.match(rf'{key}', value, flags=re.IGNORECASE)
    validate = str(validate)
    if validate == 'None':
        return 0, value
    else:
        return 1, value


# ----------------------------------------------------------------------------------------------------------------------

async def def_new_lvl(message, bot, api, data, server_data):
    new_exp = int(data[7]) - (int(int(data[6]) * int(server_data[20])))
    new_lvl = int(data[6]) + 1
    await setMultiUserData(message.from_id, f"lvl = '{new_lvl}', exp = '{new_exp}'")
    await message.answer(
        message=f"⏫ Поздравляем. Теперь у вас {new_lvl} уровень")
    data = await getUserData(message.from_id)
    if int(data[7]) >= int(int(data[6]) * int(server_data[20])):
        await def_new_lvl(message, bot, api, data, server_data)



async def def_new_lvl_payday(bot, api, data, server_data, new_exp):
    new_exp = new_exp - (int(int(data[6]) * int(server_data[20])))
    new_lvl = int(data[6]) + 1
    await setMultiUserData(data[1], f"lvl = '{new_lvl}', exp = '{new_exp}'")
    await bot.api.messages.send(
        user_id=data[1],
        random_id=random.randint(100000, 999999999),
        peer_id=data[1],
        message=f'⏫ Поздравляем. Теперь у вас {new_lvl} уровень'
    )
    data = await getUserData(data[1])
    if int(data[7]) >= int(int(data[6]) * int(server_data[20])):
        await def_new_lvl_payday(bot, api, data, server_data, new_exp)