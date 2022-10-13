
# Центральный банк

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.Show'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    if data[43] == '❌ Отсутствует':
        await message.answer(
            message=f"🎯 » 🗺 » 🏛 » 🏦 Центральный банк\n\n"
                    f"👱‍♀ Доброго времени суток, меня зовут Мария и я являюсь сотрудницей Центрального Банка штата {server_settings[2]}. Чем я могу вам помочь?",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("💳 Получение банковской карты", {"cmd": "CentralBank.CreateBankCard1"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    else:
        await message.answer(
            message=f"🎯 » 🗺 » 🏛 » 🏦 Центральный банк\n\n"
                    f"👱‍♀ Доброго времени суток, меня зовут Мария и я являюсь сотрудницей Центрального Банка штата {server_settings[2]}. Чем я могу вам помочь?",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("💳 Провести операцию с картой", {"cmd": "CentralBank.BankomatWelcome"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )


# -------------------------------------------------------------------------------------------------------------


async def BankomatWelcome(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"💳 Вы вставляете в банкомат карту"
    )
    await asyncio.sleep(5)
    await message.answer(
        message=f"👈 Вы прикладываете палец для идентификации"
    )
    await asyncio.sleep(5)
    await Bankomat(message, bot, api)



async def Bankomat(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.Bankomat'")
    data = await database.getUserData(message.from_id)
    count = await database.findBaseDataSetting('fractions', 'leader', f"'{data[3]}'")
    if count == 0:
        if data[22] == 'Без организации':
            await message.answer(
                message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 Банковские операции над картой\n\n"
                        f"👤 Здраствуйте, {data[3]}.\n\n"
                        f"💳 Выберите опцию, которой хотите воспользоваться",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("💳 Выйти", {"cmd": "CentralBank.Show"}), color=KeyboardButtonColor.PRIMARY)
                        .row()
                        .add(Text("ℹ Баланс карты", {"cmd": "CentralBank.Balance"}), color=KeyboardButtonColor.SECONDARY)
                        .row()
                        .add(Text("🔼 Пополнить", {"cmd": "CentralBank.addBalance1"}), color=KeyboardButtonColor.SECONDARY)
                        .add(Text("🔽 Списать", {"cmd": "CentralBank.vivodBalance1"}), color=KeyboardButtonColor.SECONDARY)
                        .row()
                        .add(Text("💸 Перевод денег", {"cmd": "CentralBank.transfer"}), color=KeyboardButtonColor.SECONDARY)
                        .row()
                        .add(Text("💱 Курс валют", {"cmd": "CentralBank.CourceVallet"}), color=KeyboardButtonColor.SECONDARY)
                        .add(Text("💱 Обменник валют", {"cmd": "CentralBank.exchanger1"}), color=KeyboardButtonColor.SECONDARY)
                        .get_json()
                )
            )
        else:
            await message.answer(
                message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 Банковские операции над картой\n\n"
                        f"👤 Здраствуйте, {data[3]}.\n\n"
                        f"💳 Выберите опцию, которой хотите воспользоваться",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("💳 Выйти", {"cmd": "CentralBank.Show"}), color=KeyboardButtonColor.PRIMARY)
                        .row()
                        .add(Text("ℹ Баланс карты", {"cmd": "CentralBank.Balance"}), color=KeyboardButtonColor.SECONDARY)
                        .row()
                        .add(Text("🔼 Пополнить", {"cmd": "CentralBank.addBalance1"}), color=KeyboardButtonColor.SECONDARY)
                        .add(Text("🔽 Списать", {"cmd": "CentralBank.vivodBalance1"}), color=KeyboardButtonColor.SECONDARY)
                        .row()
                        .add(Text("💸 Перевод денег", {"cmd": "CentralBank.transfer"}), color=KeyboardButtonColor.SECONDARY)
                        .row()
                        .add(Text("💱 Курс валют", {"cmd": "CentralBank.CourceVallet"}), color=KeyboardButtonColor.SECONDARY)
                        .add(Text("💱 Обменник валют", {"cmd": "CentralBank.exchanger1"}), color=KeyboardButtonColor.SECONDARY)
                        .row()
                        .add(Text("🏦 Пополнить счет фракции", {"cmd": "CentralBank.fractionAdd"}), color=KeyboardButtonColor.SECONDARY)
                        .get_json()
                )
            )
    else:
        await message.answer(
            message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 Банковские операции над картой\n\n"
                    f"👤 Здраствуйте, {data[3]}.\n\n"
                    f"💳 Выберите опцию, которой хотите воспользоваться",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("💳 Выйти", {"cmd": "CentralBank.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("ℹ Баланс карты", {"cmd": "CentralBank.Balance"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🔼 Пополнить", {"cmd": "CentralBank.addBalance1"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🔽 Списать", {"cmd": "CentralBank.vivodBalance1"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("💸 Перевод денег", {"cmd": "CentralBank.transfer"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("💱 Курс валют", {"cmd": "CentralBank.CourceVallet"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("💱 Обменник валют", {"cmd": "CentralBank.exchanger1"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🏦 Пополнить счет фракции", {"cmd": "CentralBank.fractionAdd"}),  color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🏦 Снять со счета фракции", {"cmd": "CentralBank.fractionVivod"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )






async def fractionVivod(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.fractionVivodCheck'")
    data_user = await database.getUserData(message.from_id)

    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🏦 Снять со счета фракции\n\n"
                f"📝 Введите количество денег для снятия со счета фракции",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.fractionVivodCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.fractionVivodCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.fractionVivodCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.fractionVivodCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.fractionVivodCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.fractionVivodCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.fractionVivodCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.fractionVivodCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.fractionVivodCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.fractionVivodCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.fractionVivodCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.fractionVivodCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.fractionVivodCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def fractionVivodCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    data_fraction = await database.getBdData('fractions', 'name', f"'{data[22]}'")
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data_fraction[7] >= count:
                new_balance = int(data[16]) + count

                await database.setMultiUserData(message.from_id, f"bank_dollars = '{new_balance}'")
                await database.setBdData('fractions', 'name', f"'{data[22]}'", 'bank', f"'{data_fraction[7] - count}'")
                await message.answer(
                    message=f"✅ Вы успешно сняли деньги со счета фракции"
                    )
                await Bankomat(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ На банковском счету фракции нету столько денег"
                )
                await Bankomat(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await fractionVivod(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await fractionVivod(message, bot, api)





async def fractionAdd(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.fractionAddCheck'")
    data_user = await database.getUserData(message.from_id)

    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🏦 Пополнить счет фракции\n\n"
                f"📝 Введите количество денег для пополнения счета фракции",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.fractionAddCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.fractionAddCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.fractionAddCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.fractionAddCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.fractionAddCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.fractionAddCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.fractionAddCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.fractionAddCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.fractionAddCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.fractionAddCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.fractionAddCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.fractionAddCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.fractionAddCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def fractionAddCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[16] >= count:
                new_balance = int(data[16]) - count
                data_fraction = await database.getBdData('fractions', 'name', f"'{data[22]}'")
                await database.setMultiUserData(message.from_id, f"bank_dollars = '{new_balance}'")
                await database.setBdData('fractions', 'name', f"'{data[22]}'", 'bank', f"'{data_fraction[7] + count}'")
                await message.answer(
                    message=f"✅ Вы успешно пополнили счет фракции"
                    )
                await Bankomat(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег в банке"
                )
                await Bankomat(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await fractionAdd(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await fractionAdd(message, bot, api)





async def CourceValletDollars(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.CourceValletDollars'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    data = ast.literal_eval(server_settings[16])
    data = list(data)
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💱 » 💵 Доллары\n\n"
                f"⚠ Вы просматриваете обмен с долларов на другие валюты.\n\n"
                f"1 доллар (💵) = {data[0]} евро (💶)\n"
                f"1 доллар (💵) = {data[1]} иен (💴)\n"
                f"1 доллар (💵) = {data[2]} фунтов (💷)\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "CentralBank.CourceVallet"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )


async def CourceValletEuro(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.CourceValletEuro'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    data = ast.literal_eval(server_settings[16])
    data = list(data)
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💱 » 💶 Евро\n\n"
                f"⚠ Вы просматриваете обмен с евро на другие валюты.\n\n"
                f"1 евро (💶) = {data[3]} доллары (💵)\n"
                f"1 евро (💶) = {data[4]} иен (💴)\n"
                f"1 евро (💶) = {data[5]} фунтов (💷)\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "CentralBank.CourceVallet"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )



async def CourceValletYen(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.CourceValletYen'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    data = ast.literal_eval(server_settings[16])
    data = list(data)
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💱 » 💴 Иены\n\n"
                f"⚠ Вы просматриваете обмен с иены на другие валюты.\n\n"
                f"1 иена (💴) = {data[6]} доллары (💵)\n"
                f"1 иена (💴) = {data[7]} евро (💶)\n"
                f"1 иена (💴) = {data[8]} фунтов (💷)\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "CentralBank.CourceVallet"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )


async def CourceValletPounds(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.CourceValletPounds'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    data = ast.literal_eval(server_settings[16])
    data = list(data)
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💱 » 💷 Фунты\n\n"
                f"⚠ Вы просматриваете обмен с иены на другие валюты.\n\n"
                f"1 фунт (💷) = {data[9]} доллары (💵)\n"
                f"1 фунт (💷) = {data[10]} евро (💶)\n"
                f"1 фунт (💷) = {data[11]} иен (💴)\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "CentralBank.CourceVallet"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )


async def CourceVallet(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.CourceVallet'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💱 Курс валют\n\n"
                f"⤵ Выберите валюту на которую хотите посмотреть курс",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("💵 Доллары", {"cmd": "CentralBank.CourceValletDollars"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💶 Евро", {"cmd": "CentralBank.CourceValletEuro"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💴 Иены", {"cmd": "CentralBank.CourceValletYen"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💷 Фунты", {"cmd": "CentralBank.CourceValletPounds"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def exchanger1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.exchangerError'")
    await database.setUserData(message.from_id, 'temporary_var', "'[]'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 💱 Обменник валют\n\n"
                f"Выберите валюту, с которой хотите произвести обмен",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("💵 Доллары", {"cmd": "CentralBank.exchanger2"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💶 Евро", {"cmd": "CentralBank.exchanger2"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💴 Иены", {"cmd": "CentralBank.exchanger2"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💷 Фунты", {"cmd": "CentralBank.exchanger2"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def exchanger2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.exchangerError'")
    data = await database.getUserData(message.from_id)

    data = ast.literal_eval(data[44])
    data = list(data)

    KEYBOARD = Keyboard(one_time=True, inline=False)
    KEYBOARD.add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
    KEYBOARD.row()
    if message.text == '💵 Доллары':
        data.append(0)
        KEYBOARD.add(Text("💶 Евро", {"cmd": "CentralBank.exchanger3"}), color=KeyboardButtonColor.SECONDARY)
        KEYBOARD.row()
        KEYBOARD.add(Text("💴 Иены", {"cmd": "CentralBank.exchanger3"}), color=KeyboardButtonColor.SECONDARY)
        KEYBOARD.add(Text("💷 Фунты", {"cmd": "CentralBank.exchanger3"}), color=KeyboardButtonColor.SECONDARY)
    if message.text == '💶 Евро':
        data.append(1)
        KEYBOARD.add(Text("💵 Доллары", {"cmd": "CentralBank.exchanger3"}), color=KeyboardButtonColor.SECONDARY)
        KEYBOARD.row()
        KEYBOARD.add(Text("💴 Иены", {"cmd": "CentralBank.exchanger3"}), color=KeyboardButtonColor.SECONDARY)
        KEYBOARD.add(Text("💷 Фунты", {"cmd": "CentralBank.exchanger3"}), color=KeyboardButtonColor.SECONDARY)
    if message.text == '💴 Иены':
        data.append(2)
        KEYBOARD.add(Text("💵 Доллары", {"cmd": "CentralBank.exchanger3"}), color=KeyboardButtonColor.SECONDARY)
        KEYBOARD.row()
        KEYBOARD.add(Text("💶 Евро", {"cmd": "CentralBank.exchanger3"}), color=KeyboardButtonColor.SECONDARY)
        KEYBOARD.add(Text("💷 Фунты", {"cmd": "CentralBank.exchanger3"}), color=KeyboardButtonColor.SECONDARY)
    if message.text == '💷 Фунты':
        data.append(3)
        KEYBOARD.add(Text("💵 Доллары", {"cmd": "CentralBank.exchanger3"}), color=KeyboardButtonColor.SECONDARY)
        KEYBOARD.row()
        KEYBOARD.add(Text("💶 Евро", {"cmd": "CentralBank.exchanger3"}), color=KeyboardButtonColor.SECONDARY)
        KEYBOARD.add(Text("💴 Иены", {"cmd": "CentralBank.exchanger3"}), color=KeyboardButtonColor.SECONDARY)
    KEYBOARD.get_json()
    await database.setUserData(message.from_id, 'temporary_var', f'"{data}"')
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 💱 Обменник валют\n\n"
                f"Выберите валюту, в которую хотите произвести обмен",
        keyboard=KEYBOARD
    )



async def exchanger3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.exchanger3_check'")
    data = await database.getUserData(message.from_id)

    server_settings = await database.getBdData('settings', 'id', "'1'")
    exchange = ast.literal_eval(server_settings[16])
    exchange = list(exchange)

    data = ast.literal_eval(data[44])
    data = list(data)
    if message.text == '💵 Доллары':
        data.append(0)
    if message.text == '💶 Евро':
        data.append(1)
    if message.text == '💴 Иены':
        data.append(2)
    if message.text == '💷 Фунты':
        data.append(3)
    if data[0] == 0:
        title = 'долларов (💵)'
        title_one = 'доллар (💵)'
        if data[1] == 1:
            minimum = 10
            data[1] = 0
        if data[1] == 2:
            minimum = 10
            data[1] = 1
        if data[1] == 3:
            minimum = 10
            data[1] = 2
    if data[0] == 1:
        title = 'евро (💶)'
        title_one = 'евро (💶)'
        if data[1] == 3:
            minimum = 10
            data[1] = 5
        if data[1] == 2:
            minimum = 10
            data[1] = 4
        if data[1] == 0:
            minimum = 10
            data[1] = 3
    if data[0] == 2:
        title = 'иен (💴)'
        title_one = 'иену (💴)'
        if data[1] == 0:
            minimum = 5000
            data[1] = 6
        if data[1] == 1:
            minimum = 5000
            data[1] = 7
        if data[1] == 3:
            minimum = 5000
            data[1] = 8
    if data[0] == 3:
        title = 'фунтов (💷)'
        title_one = 'фунт (💷)'
        if data[1] == 0:
            minimum = 10
            data[1] = 9
        if data[1] == 1:
            minimum = 10
            data[1] = 10
        if data[1] == 2:
            minimum = 10
            data[1] = 11
    await database.setUserData(message.from_id, 'temporary_var', f'"{data}"')
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 💱 Обменник валют\n\n"
                f"⚠ Минимальное количество для перевода {minimum} {title}\n"
                f"💱 За 1 {title_one} вы получите {exchange[data[1]]}\n\n"
                f"✏ Напиши количество {title} для перевода",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )


async def exchanger3_check(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data = await database.getUserData(message.from_id)
    temporary_var = ast.literal_eval(data[44])
    temporary_var = list(temporary_var)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    exchange = ast.literal_eval(server_settings[16])
    exchange = list(exchange)
    if temporary_var[0] == 0:
        minimum = 10
        type_vallet = 16
    if temporary_var[0] == 1:
        minimum = 10
        type_vallet = 17
    if temporary_var[0] == 2:
        minimum = 5000
        type_vallet = 18
    if temporary_var[0] == 3:
        minimum = 10
        type_vallet = 19

    if temporary_var[1] == 0:
        end_vallet = 17
    if temporary_var[1] == 1:
        end_vallet = 18
    if temporary_var[1] == 2:
        end_vallet = 19

    if temporary_var[1] == 3:
        end_vallet = 16
    if temporary_var[1] == 4:
        end_vallet = 18
    if temporary_var[1] == 5:
        end_vallet = 19

    if temporary_var[1] == 6:
        end_vallet = 16
    if temporary_var[1] == 7:
        end_vallet = 17
    if temporary_var[1] == 8:
        end_vallet = 19

    if temporary_var[1] == 9:
        end_vallet = 16
    if temporary_var[1] == 10:
        end_vallet = 17
    if temporary_var[1] == 11:
        end_vallet = 18

    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if count >= minimum:
                if data[type_vallet] >= count:

                    procent = count / 100
                    countprocent = count - (procent * 2)
                    out_bank = data[type_vallet] - count
                    in_bank = int(data[end_vallet] + (exchange[temporary_var[1]] * countprocent))

                    if type_vallet == 16:
                        name_out = 'bank_dollars'
                    if type_vallet == 17:
                        name_out = 'bank_euro'
                    if type_vallet == 18:
                        name_out = 'bank_yen'
                    if type_vallet == 19:
                        name_out = 'bank_pounds'

                    if end_vallet == 16:
                        name_in = 'bank_dollars'
                    if end_vallet == 17:
                        name_in = 'bank_euro'
                    if end_vallet == 18:
                        name_in = 'bank_yen'
                    if end_vallet == 19:
                        name_in = 'bank_pounds'

                    await database.setMultiUserData(message.from_id, f"{name_out} = '{out_bank}'")
                    await database.setMultiUserData(message.from_id, f"{name_in} = '{in_bank}'")
                    await message.answer(
                        message=f"✅ Вы успешно обменяли валюту! (с учетом комиссии 2%)"
                    )
                    await Bankomat(message, bot, api)
                else:
                    await message.answer(
                        message=f"❌ У вас нет столько денег в банке"
                    )
                    await Bankomat(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ Вы должны указать число больше {minimum}",
                )
                await Bankomat(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await Bankomat(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await Bankomat(message, bot, api)






async def ComingSoon(message: Message, bot: Bot, api: API):
    await message.answer(
        message=f"⌛ В данный момент банк не может сделать обмен валют. Попробуйте позже"
    )
    await Bankomat(message, bot, api)



async def transfer(message: Message, bot: Bot, api: API):
    await database.setMultiUserData(message.from_id, "state = 'CentralBank.transfer2', temporary_var = '[]'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 💸 Перевод денег\n\n📝 Укажите ссылку на пользователя",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )





async def transfer2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.transfer2'")
    try:
        link = message.text[15:]
        user_get = await bot.api.users.get(user_ids=link)
        id_user = user_get[0].id
        data = await database.getUserData(id_user)
        user_data = await database.getUserData(message.from_id)
        if data[43] == '❌ Отсутствует':
            await message.answer(
                message=f"❌ У данного человека отсутствует банковская карта. Переводы недоступны"
            )
            await transfer(message, bot, api)
        else:
            if data[1] == user_data[1]:
                await message.answer(
                    message=f"❌ Вы пытаетесь перевести деньги самому себе"
                )
                await transfer(message, bot, api)
            else:
                await database.setUserData(message.from_id, 'temporary_var', f"'{id_user}'")
                await message.answer(
                    message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 💸 Перевод денег\n\n"
                            f"Выберите валюту для перевода",
                    keyboard=(
                        Keyboard(one_time=True, inline=False)
                            .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                            .row()
                            .add(Text("💵 Доллары", {"cmd": "CentralBank.transferDollars"}), color=KeyboardButtonColor.SECONDARY)
                            .add(Text("💶 Евро", {"cmd": "CentralBank.transferEuro"}), color=KeyboardButtonColor.SECONDARY)
                            .row()
                            .add(Text("💴 Иены", {"cmd": "CentralBank.transferYen"}), color=KeyboardButtonColor.SECONDARY)
                            .add(Text("💷 Фунты", {"cmd": "CentralBank.transferPounds"}), color=KeyboardButtonColor.SECONDARY)
                            .get_json()
                    )
                )
    except Exception as ex:
        await message.answer(
            message=f'⚠ Возникла ошибка при поиске игрока\n\n'
                    f'— Убедитесь, что вы ввели правильную ссылку и то, что человек играет на нашем сервере'
        )
        await transfer(message, bot, api)



async def transferPounds(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.transferPoundsCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 💸 » 💷 Фунты\n\n📝 Укажите количество денег для перевода",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )


async def transferPoundsCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[19] >= count:
                data_to_transfer = await database.getUserData(int(data[44]))
                new_balance = int(data_to_transfer[19]) + count
                new_balance2 = int(data[19]) - count
                await database.setMultiUserData(message.from_id, f"bank_pounds = '{new_balance2}'")
                await database.setMultiUserData(int(data[44]), f"bank_pounds = '{new_balance}'")
                await message.answer(
                    message=f"✅ Вы успешно перевели деньги {data_to_transfer[3]} на счет в количестве {count} фунтов (💷)"
                    )
                await Bankomat(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег в банке"
                )
                await transferPounds(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await transferPounds(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await transferPounds(message, bot, api)





async def transferYen(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.transferYenCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 💸 » 💴 Иены\n\n📝 Укажите количество денег для перевода",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )


async def transferYenCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[18] >= count:
                data_to_transfer = await database.getUserData(int(data[44]))
                new_balance = int(data_to_transfer[18]) + count
                new_balance2 = int(data[18]) - count
                await database.setMultiUserData(message.from_id, f"bank_yen = '{new_balance2}'")
                await database.setMultiUserData(int(data[44]), f"bank_yen = '{new_balance}'")
                await message.answer(
                    message=f"✅ Вы успешно перевели деньги {data_to_transfer[3]} на счет в количестве {count} иен (💴)"
                    )
                await Bankomat(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег в банке"
                )
                await transferYen(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await transferYen(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await transferYen(message, bot, api)



async def transferEuro(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.transferEuroCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 💸 » 💶 Евро\n\n📝 Укажите количество денег для перевода",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )


async def transferEuroCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[17] >= count:
                data_to_transfer = await database.getUserData(int(data[44]))
                new_balance = int(data_to_transfer[17]) + count
                new_balance2 = int(data[17]) - count
                await database.setMultiUserData(message.from_id, f"bank_euro = '{new_balance2}'")
                await database.setMultiUserData(int(data[44]), f"bank_euro = '{new_balance}'")
                await message.answer(
                    message=f"✅ Вы успешно перевели деньги {data_to_transfer[3]} на счет в количестве {count} евро (💶)"
                    )
                await Bankomat(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег в банке"
                )
                await transferEuro(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await transferEuro(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await transferEuro(message, bot, api)






async def transferDollars(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.transferDollarsCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 💸 » 💵 Доллары\n\n📝 Укажите количество денег для перевода",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )


async def transferDollarsCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[16] >= count:
                data_to_transfer = await database.getUserData(int(data[44]))
                new_balance = int(data_to_transfer[16]) + count
                new_balance2 = int(data[16]) - count
                await database.setMultiUserData(message.from_id, f"bank_dollars = '{new_balance2}'")
                await database.setMultiUserData(int(data[44]), f"bank_dollars = '{new_balance}'")
                await message.answer(
                    message=f"✅ Вы успешно перевели деньги {data_to_transfer[3]} на счет в количестве {count} долларов (💵)"
                    )
                await Bankomat(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег в банке"
                )
                await transferDollars(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await transferDollars(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await transferDollars(message, bot, api)















async def Balance(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    num1 = await database.pretty(data[16])
    num2 = await database.pretty(data[17])
    num3 = await database.pretty(data[18])
    num4 = await database.pretty(data[19])
    await message.answer(
        message=f"💵 Доллары в банке » {num1}\n"
                f"💶 Евро в банке » {num2}\n"
                f"💴 Иены в банке » {num3}\n"
                f"💷 Фунты в банке » {num4}",
    )
    await Bankomat(message, bot, api)



async def vivodBalance1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.vivodBalance1'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔽 Списать\n\n"
                f"Выберите валюту для списания",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("💵 Доллары", {"cmd": "CentralBank.vivodBalanceDollars"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💶 Евро", {"cmd": "CentralBank.vivodBalanceEuro"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💴 Иены", {"cmd": "CentralBank.vivodBalanceYen"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💷 Фунты", {"cmd": "CentralBank.vivodBalancePounds"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def vivodBalancePounds(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.vivodBalancePoundsCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔽 » 💷 Фунты\n\n"
                f"📝 Введите количество денег, которое вы хотите снять",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.vivodBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def vivodBalancePoundsCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[19] >= count:
                new_balance = int(data[15]) + count
                new_balance2 = int(data[19]) - count
                await database.setMultiUserData(message.from_id, f"pounds = '{new_balance}', bank_pounds = '{new_balance2}'")
                await message.answer(
                    message=f"✅ Вы успешно сняли фунты со своего счета"
                    )
                await Bankomat(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег в банке"
                )
                await Bankomat(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await vivodBalancePounds(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await vivodBalancePounds(message, bot, api)





async def vivodBalanceYen(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.vivodBalanceYenCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔽 » 💴 Иены\n\n"
                f"📝 Введите количество денег, которое вы хотите снять",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.vivodBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def vivodBalanceYenCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[18] >= count:
                new_balance = int(data[14]) + count
                new_balance2 = int(data[18]) - count
                await database.setMultiUserData(message.from_id, f"yen = '{new_balance}', bank_yen = '{new_balance2}'")
                await message.answer(
                    message=f"✅ Вы успешно сняли иены со своего счета"
                    )
                await Bankomat(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег в банке"
                )
                await Bankomat(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await vivodBalanceYen(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await vivodBalanceYen(message, bot, api)





async def vivodBalanceEuro(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.vivodBalanceEuroCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔽 » 💶 Евро\n\n"
                f"📝 Введите количество денег, которое вы хотите снять",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.vivodBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def vivodBalanceEuroCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[17] >= count:
                new_balance = int(data[13]) + count
                new_balance2 = int(data[17]) - count
                await database.setMultiUserData(message.from_id, f"euro = '{new_balance}', bank_euro = '{new_balance2}'")
                await message.answer(
                    message=f"✅ Вы успешно сняли евро со своего счета"
                    )
                await Bankomat(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег в банке"
                )
                await Bankomat(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await vivodBalanceEuro(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await vivodBalanceEuro(message, bot, api)



async def vivodBalanceDollars(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.vivodBalanceDollarsCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔽 » 💵 Доллары\n\n"
                f"📝 Введите количество денег, которое вы хотите снять",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.vivodBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def vivodBalanceDollarsCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[16] >= count:
                new_balance = int(data[12]) + count
                new_balance2 = int(data[16]) - count
                await database.setMultiUserData(message.from_id, f"dollars = '{new_balance}', bank_dollars = '{new_balance2}'")
                await message.answer(
                    message=f"✅ Вы успешно сняли доллары со своего счета"
                    )
                await Bankomat(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег в банке"
                )
                await Bankomat(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await vivodBalanceDollars(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await vivodBalanceDollars(message, bot, api)
















async def addBalance1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.addBalance1'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔼 Пополнить\n\n"
                f"Выберите валюту для пополнения",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("💵 Доллары", {"cmd": "CentralBank.addBalanceDollars"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💶 Евро", {"cmd": "CentralBank.addBalanceEuro"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💴 Иены", {"cmd": "CentralBank.addBalanceYen"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💷 Фунты", {"cmd": "CentralBank.addBalancePounds"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def addBalancePounds(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.addBalancePoundsCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔼 » 💷 Фунты\n\n"
                f"📝 Введите количество денег, которое вы хотите пополнить",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.addBalancePoundsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def addBalancePoundsCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[15] >= count:
                new_balance = int(data[15]) - count
                new_balance2 = int(data[19]) + count
                await database.setMultiUserData(message.from_id, f"pounds = '{new_balance}', bank_pounds = '{new_balance2}'")
                await message.answer(
                    message=f"✅ Вы успешно пополнили фунтовый счет"
                    )
                await Bankomat(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег на руках"
                )
                await Bankomat(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await addBalancePounds(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await addBalancePounds(message, bot, api)





async def addBalanceYen(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.addBalanceYenCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔼 » 💴 Иены\n\n"
                f"📝 Введите количество денег, которое вы хотите пополнить",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.addBalanceYenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def addBalanceYenCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[14] >= count:
                new_balance = int(data[14]) - count
                new_balance2 = int(data[18]) + count
                await database.setMultiUserData(message.from_id, f"yen = '{new_balance}', bank_yen = '{new_balance2}'")
                await message.answer(
                    message=f"✅ Вы успешно пополнили иеновский счет"
                    )
                await Bankomat(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег на руках"
                )
                await Bankomat(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await addBalanceYen(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await addBalanceYen(message, bot, api)





async def addBalanceEuro(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.addBalanceEuroCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔼 » 💶 Евро\n\n"
                f"📝 Введите количество денег, которое вы хотите пополнить",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.addBalanceEuroCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def addBalanceEuroCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[13] >= count:
                new_balance = int(data[13]) - count
                new_balance2 = int(data[17]) + count
                await database.setMultiUserData(message.from_id, f"euro = '{new_balance}', bank_euro = '{new_balance2}'")
                await message.answer(
                    message=f"✅ Вы успешно пополнили евро счет"
                    )
                await Bankomat(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег на руках"
                )
                await Bankomat(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await addBalanceEuro(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await addBalanceEuro(message, bot, api)



async def addBalanceDollars(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.addBalanceDollarsCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 » 🔼 » 💵 Доллары\n\n"
                f"📝 Введите количество денег, которое вы хотите пополнить",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Отмена", {"cmd": "CentralBank.Bankomat"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("25", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("1000", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5000", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("25000", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250000", {"cmd": "CentralBank.addBalanceDollarsCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def addBalanceDollarsCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if data[12] >= count:
                new_balance = int(data[12]) - count
                new_balance2 = int(data[16]) + count
                await database.setMultiUserData(message.from_id, f"dollars = '{new_balance}', bank_dollars = '{new_balance2}'")
                await message.answer(
                    message=f"✅ Вы успешно пополнили долларовый счет"
                    )
                await Bankomat(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег на руках"
                )
                await Bankomat(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await addBalanceDollars(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await addBalanceDollars(message, bot, api)




# --------------------------------------------------------------------------------------------------------------


async def CreateBankCard1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.CreateBankCard1'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 Получение банковской карты\n\n"
                f"👱‍♀ Для того, чтобы оформить банковскую карту, вам необходимо 250 долларов (💵). Они у вас есть?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💬 Нету", {"cmd": "CentralBank.CreateBankCardError"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💵 Заплатить за оформление карты", {"cmd": "CentralBank.CreateBankCard2"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def CreateBankCardError(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.CreateBankCardError'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 Получение банковской карты\n\n"
                f"👱‍♀ Как только у вас будет 250 долларов (💵), то я вам смогу сделать банковскую карту",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💬 Хорошо", {"cmd": "CentralBank.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def CreateBankCard2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.CreateBankCard2'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    if data[12] >= 250:
        await message.answer(
            message="👱‍♀ Отлично."
        )
        new_balance = int(data[12]) - 250
        await database.setUserData(message.from_id, "dollars", f"'{new_balance}'")
        await CreateBankCard3(message, bot, api)
    else:
        await message.answer(
            message=f"❌ У вас нет 250 долларов на руках",
        )
        await CreateBankCard1(message, bot, api)


async def CreateBankCard3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CentralBank.CreateBankCard3'")
    await message.answer(
        message="👱‍♀ Проследуйте за мной, необходима ваша фотография",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶🏻‍♂ Идти за девушкой", {"cmd": "CentralBank.CreateBankCard4"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def CreateBankCard4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚶🏻‍♂ Вы идете за девушкой в специальную комнату"
    )
    await asyncio.sleep(5)
    await database.setUserData(message.from_id, 'state', "'CentralBank.CreateBankCard4'")
    await message.answer(
        message=f"🚶🏻‍♂ Вы пришли в специальную комнату и видите в ней фотокамеру и световые прожекторы"
    )
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 Получение банковской карты\n\n"
                f"👱‍♀ Присаживайтесь на стул, сейчас я вас сфотографирую.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🪑 Сесть на стул", {"cmd": "CentralBank.CreateBankCard5"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def CreateBankCard5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🪑 Вы сели на стул"
    )
    await asyncio.sleep(2)
    await message.answer(
        message=f"📸 *Произошел щелчок в камере*"
    )
    await asyncio.sleep(4)
    await message.answer(
        message=f"👱‍♀ Вы отлично получились на данной фотографии"
    )
    await asyncio.sleep(2)
    await message.answer(
        message=f"👱‍♀  Сейчас прикреплю вашу фотографию к карте и выдам её вам..."
    )
    await asyncio.sleep(15)
    await database.setUserData(message.from_id, 'state', "'CentralBank.CreateBankCard5'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 Получение банковской карты\n\n"
                f"👱‍♀ Отлично, на этом все. Теперь это ваша карта. Спасибо, что выбрали именно наш банк.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Callback("💳 Взять карту", payload={"cmd": "CentralBank.CreateBankCard6"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def CreateBankCard6(from_id, bot: Bot):
    await database.setUserData(from_id, 'state', "'CentralBank.Show'")
    await database.setUserData(from_id, 'bank_card', "'✅ Имеется'")
    await bot.api.messages.send(
        user_id=from_id,
        random_id=random.randint(1, 999999999),
        message=f"🎯 » 🗺 » 🏛 » 🏦 » 💳 Получение банковской карты\n\n"
                f"💳 Вы взяли карту.\n\n"
                f"⭐ ТЕПЕРЬ У ВАС ЕСТЬ ВОЗМОЖНОСТИ:\n"
                f"— Пользоваться услугами банка: пополнять, снимать деньги со счета\n"
                f"— Переводить деньги с карты на карту\n"
                f"— Получать уникальные скидки и кэшбек.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉 Продолжить", {"cmd": "CentralBank.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )