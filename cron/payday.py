# ----------------------------------------------------------------------------------------------------------------------

# Игровой Role-Play чат-бот для ВКонтакте.
#
# Автор: Reazy, 2022 год.

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, ast, json, time, datetime, random, traceback
from vkbottle.bot import Bot, Message, MessageEvent
from vkbottle import API, LoopWrapper, GroupEventType

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

bot = Bot('aed307a7c1248aea24454fb0e44d8c6c94c92255e759f701023ab1963501be1683acfd6fea6fe0596a28a')
api = API('25a06c2cbdd3d2788f0af4bc75c6c4b5ede3e807d16143eafe0e03ff286ac2089760a2d7da9ac8b1a9415')
lw = LoopWrapper()

# ----------------------------------------------------------------------------------------------------------------------

async def PayDay():
    # Получаем данные от сервера
    DATA_SERVER = await database.getBdData('settings', "id", "'1'")
    DATA_CRON = await database.getBdData('cron', "id", "'1'")
    if DATA_CRON[1] == 1:
        # Делаем выборку игроков, которые играли в течении 20 минут на сервера
        math_count_online = int(time.time()) - 1200

        # Получаем текущее время
        real_time = datetime.datetime.now()

        # Подставляем точные значения в переменные
        real_time_hour = real_time.hour
        real_time_minute = real_time.minute

        # Дописываем нули, если дата выглядит так: 07:03
        if real_time.hour < 10: real_time_hour = f'0{real_time.hour}'
        if real_time.minute < 10: real_time_minute = f'0{real_time.minute}'

        # Получаем список всех пользователей, у которых последнее сообщение было 20 минут назад (или как в math_count_online)
        users = await database.getMultiProgramBdData('users', f"last_message >= {math_count_online}")
        for selected in users:
            zarplata = selected[16]
            if selected[22] != 'Без организации':
                data_fraction = await database.getBdData('fractions', 'name', f"'{selected[22]}'")
                data_faction = ast.literal_eval(data_fraction[6])
                data_faction = list(data_faction)
                if selected[23] == 1: vibor_zp = 9
                if selected[23] == 2: vibor_zp = 8
                if selected[23] == 3: vibor_zp = 7
                if selected[23] == 4: vibor_zp = 6
                if selected[23] == 5: vibor_zp = 5
                if selected[23] == 6: vibor_zp = 4
                if selected[23] == 7: vibor_zp = 3
                if selected[23] == 8: vibor_zp = 2
                if selected[23] == 9: vibor_zp = 1
                if selected[23] == 10: vibor_zp = 0
                zarplata = selected[16] + int(data_faction[vibor_zp])
                await database.setUserData(selected[1], 'bank_dollars', f"'{zarplata}'")

            # Получаем значения EXP и LVL
            exp = int(selected[7])
            lvl = int(selected[6])

            # Увеличиваем EXP на значения из базы данных
            new_exp = exp + (1 * DATA_SERVER[25])
            await database.setMultiUserData(selected[1], f"exp = '{new_exp}'")
            await bot.api.messages.send(
                user_id=selected[1],
                random_id=random.randint(100000, 999999999),
                peer_id=selected[1],
                message=f'🧾 Банковский чек — {real_time_hour}:{real_time_minute}\n\n'
                        f'💵 Текущая сумма долларов в банке » {await database.pretty(zarplata)}\n'
                        f'💶 Текущая сумма евро в банке » {await database.pretty(selected[17])}\n'
                        f'💴 Текущая сумма иен в банке » {await database.pretty(selected[18])}\n'
                        f'💷 Текущая сумма фунтов в банке » {await database.pretty(selected[19])}\n\n'
                        f'🌐 На данный момент у вас {selected[6]}-й уровень и {new_exp}/{lvl * DATA_SERVER[20]} очков опыта'
            )

            # Если у игрока EXP больше, чем необходимо, то повышаем уровень
            if new_exp >= (lvl * DATA_SERVER[20]):
                await database.def_new_lvl_payday(bot, api, selected, DATA_SERVER, new_exp)

        quit(1)
    else:
        quit(1)
# ----------------------------------------------------------------------------------------------------------------------

bot.loop_wrapper.add_task(PayDay())
bot.run_forever()