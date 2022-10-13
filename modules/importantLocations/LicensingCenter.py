
# Центр лицензирования

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.Show'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 📒 Центр лицензирования\n\n"
                f"👨 Доброго времени суток, добро пожаловать в центр лицензирования. Чем я могу вам помочь?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("📒 Получение прав", {"cmd": "LicensingCenter.GetLicences"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📃 Узнать стоимость", {"cmd": "LicensingCenter.PricesLicences"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def GetLicences(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.GetLicences'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 📒 » 📒 Получение прав\n\n"
                f"👨 Какие права вы желаете получить. Как только вы выберите права, не забудьте их оплатить",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "LicensingCenter.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🚗 Автомобильные права", {"cmd": "LicensingCenter.AutoCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🏍 Лицензия на мотоциклы", {"cmd": "LicensingCenter.BikeCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def BikeCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    dataprava = ast.literal_eval(data[24])
    dataprava = list(dataprava)
    if dataprava[1] == '✅ Имеется':
        await message.answer(
            message=f"❌ У вас уже имеются данные права"
        )
        await GetLicences(message, bot, api)
    else:
        if int(data[12]) >= 250:
            new_balance = int(data[12]) - 250
            await database.setUserData(message.from_id, 'dollars', f"'{new_balance}'")
            await message.answer(
                message=f"✅ Вы заплатили 250 долларов (💵) за права"
            )
            await BikeQuestion1(message, bot, api)
        else:
            await message.answer(
                message=f"❌ У вас недостаточно денег (нужно 250 долларов (💵)) "
            )
            await GetLicences(message, bot, api)



async def BikeQuestion1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.BikeQuestion1'")
    await message.answer(
        message=f"👨 Инструктор » С какой скоростью можно ездить вне города?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("70", {"cmd": "LicensingCenter.BikeQuestion2"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("120", {"cmd": "LicensingCenter.BikeQuestion2"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("180", {"cmd": "LicensingCenter.BikeQuestion2"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def BikeQuestion2(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text == '120':
        await database.setUserData(message.from_id, 'temporary_var', "'1'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.BikeQuestion2'")
    await message.answer(
        message=f"👨 Инструктор » Разрешена ли парковка на тратуаре?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Разрешена", {"cmd": "LicensingCenter.BikeQuestion3"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Только в экстренных ситуациях", {"cmd": "LicensingCenter.BikeQuestion3"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Запрещена", {"cmd": "LicensingCenter.BikeQuestion3"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def BikeQuestion3(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text == 'Только в экстренных ситуациях':
        new_ball = int(data[44]) + 1
        await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.BikeQuestion3'")
    await message.answer(
        message=f"👨 Инструктор » На каком расстоянии должен стоять знак аварийной остановки?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("5 метров", {"cmd": "LicensingCenter.BikeQuestion4"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("10 метров", {"cmd": "LicensingCenter.BikeQuestion4"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("15 метров", {"cmd": "LicensingCenter.BikeQuestion4"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("20 метров", {"cmd": "LicensingCenter.BikeQuestion4"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def BikeQuestion4(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text == '15 метров':
        new_ball = int(data[44]) + 1
        await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.BikeQuestion4'")
    await message.answer(
        message=f"👨 Инструктор » В дождливую погоду тормозной путь транспортного средства?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Увеличивается", {"cmd": "LicensingCenter.BikeQuestion5"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Не изменяется", {"cmd": "LicensingCenter.BikeQuestion5"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Уменьшается", {"cmd": "LicensingCenter.BikeQuestion5"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def BikeQuestion5(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text == 'Увеличивается':
        new_ball = int(data[44]) + 1
        await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.BikeQuestion5'")
    await message.answer(
        message=f"👨 Инструктор » Выезд со двора или другой прилегающей территории?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Считается перекрестком", {"cmd": "LicensingCenter.BikeQuestion6"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Не считается перекрестком", {"cmd": "LicensingCenter.BikeQuestion6"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def BikeQuestion6(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text == 'Не считается перекрестком':
        new_ball = int(data[44]) + 1
        await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.BikeQuestion6'")
    await message.answer(
        message=f"👨 Инструктор » Какова максимальная скорость мототранспорта по городу?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("60 км/ч", {"cmd": "LicensingCenter.BikeQuestion7"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("80 км/ч", {"cmd": "LicensingCenter.BikeQuestion7"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("100 км/ч", {"cmd": "LicensingCenter.BikeQuestion7"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("120 км/ч", {"cmd": "LicensingCenter.BikeQuestion7"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def BikeQuestion7(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text == '60 км/ч':
        new_ball = int(data[44]) + 1
        await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion7'")
    data = await database.getUserData(message.from_id)
    new_ball = int(data[44])
    if new_ball >= 3:
        await message.answer(
            message=f"👨 Инструктор » Вы успешно сдали экзамен на {new_ball} из 6 баллов.\nПолучите свои права, ждем вас снова в центре лицензирования",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Callback("📒 Получить права", payload={"cmd": "LicensingCenter.ShowBikes"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    else:
        await message.answer(
            message=f"👨 Инструктор »  Увы, вы не сдали на права. Вы набрали {new_ball} из 6 баллов. Попробуйте еще раз",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("👉 Продолжить", {"cmd": "LicensingCenter.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )

async def BikeOpen(from_id, bot: Bot):
    await database.setUserData(from_id, 'state', "'LicensingCenter.Show'")
    data = await database.getUserData(from_id)
    data = ast.literal_eval(data[24])
    data = list(data)
    data[1] = '✅ Имеется'
    await database.setUserData(from_id, 'license', f"\"{data}\"")
    await bot.api.messages.send(
        user_id=from_id,
        random_id=random.randint(1, 999999999),
        message=f"📒 Вы взяли права на вождение мотоциклов.\n\n"
                f"⭐ ТЕПЕРЬ У ВАС ЕСТЬ ВОЗМОЖНОСТИ:\n"
                f"— Работать на доставке с помощью мопеда\n"
                f"— Покупать мотоциклы и управлять ими",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉 Продолжить", {"cmd": "LicensingCenter.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )












async def AutoCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    dataprava = ast.literal_eval(data[24])
    dataprava = list(dataprava)
    if dataprava[0] == '✅ Имеется':
        await message.answer(
            message=f"❌ У вас уже имеются данные права"
        )
        await GetLicences(message, bot, api)
    else:
        if int(data[12]) >= 1500:
            new_balance = int(data[12]) - 1500
            await database.setUserData(message.from_id, 'dollars', f"'{new_balance}'")
            await message.answer(
                message=f"✅ Вы заплатили 1 500 долларов (💵) за права"
            )
            await AutoQuestion1(message, bot, api)
        else:
            await message.answer(
                message=f"❌ У вас недостаточно денег (нужно 1 500 долларов (💵)) "
            )
            await GetLicences(message, bot, api)




async def AutoQuestion1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion1'")
    await message.answer(
        message=f"👨 Инструктор » С какой скоростью можно ездить по городу?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("40", {"cmd": "LicensingCenter.AutoQuestion2"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("60", {"cmd": "LicensingCenter.AutoQuestion2"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("90", {"cmd": "LicensingCenter.AutoQuestion2"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def AutoQuestion2(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text == '60':
        await database.setUserData(message.from_id, 'temporary_var', "'1'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion2'")
    await message.answer(
        message=f"👨 Инструктор » Что нужно сделать при тумане?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Увеличить скорость и включить фары", {"cmd": "LicensingCenter.AutoQuestion3"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Снизить скорость и включить фары", {"cmd": "LicensingCenter.AutoQuestion3"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Остановиться и выключить фары", {"cmd": "LicensingCenter.AutoQuestion2"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def AutoQuestion3(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text == 'Снизить скорость и включить фары':
        new_ball = int(data[44]) + 1
        await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion3'")
    await message.answer(
        message=f"👨 Инструктор » На какой стороне дороги разрешена остановка?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("На правой стороне", {"cmd": "LicensingCenter.AutoQuestion4"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("На левой стороне", {"cmd": "LicensingCenter.AutoQuestion4"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def AutoQuestion4(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text == 'На правой стороне':
        new_ball = int(data[44]) + 1
        await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion4'")
    await message.answer(
        message=f"👨 Инструктор » Что необходимо сделать при повороте на нерегулируемом перекрестке?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Уступить дорогу проезжающим машинам", {"cmd": "LicensingCenter.AutoQuestion5"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Дождаться разрешающего сигнала", {"cmd": "LicensingCenter.AutoQuestion5"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Пропустить пешеходов", {"cmd": "LicensingCenter.AutoQuestion5"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def AutoQuestion5(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text == 'Пропустить пешеходов':
        new_ball = int(data[44]) + 1
        await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion5'")
    await message.answer(
        message=f"👨 Инструктор » Разрешена ли парковка на тротуаре?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Только в экстренных случаях", {"cmd": "LicensingCenter.AutoQuestion6"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Да", {"cmd": "LicensingCenter.AutoQuestion6"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Иногда", {"cmd": "LicensingCenter.AutoQuestion6"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Нет", {"cmd": "LicensingCenter.AutoQuestion6"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )




async def AutoQuestion6(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text == 'Только в экстренных случаях':
        new_ball = int(data[44]) + 1
        await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion6'")
    await message.answer(
        message=f"👨 Инструктор » В каком случае стоит пристегивать ремень безопасности?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("В любом случае", {"cmd": "LicensingCenter.AutoQuestion7"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Когда необходимо", {"cmd": "LicensingCenter.AutoQuestion7"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("При полицейских", {"cmd": "LicensingCenter.AutoQuestion7"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def AutoQuestion7(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text == 'В любом случае':
        new_ball = int(data[44]) + 1
        await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion7'")
    await message.answer(
        message=f"👨 Инструктор » Разрешено ли движение задним ходом на магистрали?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Запрещено", {"cmd": "LicensingCenter.AutoQuestion8"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Разрешено", {"cmd": "LicensingCenter.AutoQuestion8"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("Только в экстренных ситуациях", {"cmd": "LicensingCenter.AutoQuestion8"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def AutoQuestion8(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text == 'В любом случае':
        new_ball = int(data[44]) + 1
        await database.setUserData(message.from_id, 'temporary_var', f"'{new_ball}'")
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.AutoQuestion8'")
    data = await database.getUserData(message.from_id)
    new_ball = int(data[44])
    if new_ball >= 4:
        await message.answer(
            message=f"👨 Инструктор » Вы успешно сдали экзамен на {new_ball} из 7 баллов.\nПолучите свои права, ждем вас снова в центре лицензирования",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Callback("📒 Получить права", payload={"cmd": "LicensingCenter.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    else:
        await message.answer(
            message=f"👨 Инструктор »  Увы, вы не сдали на права. Вы набрали {new_ball} из 7 баллов. Попробуйте еще раз",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("👉 Продолжить", {"cmd": "LicensingCenter.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )


async def AutoOpen(from_id, bot: Bot):
    await database.setUserData(from_id, 'state', "'LicensingCenter.Show'")
    data = await database.getUserData(from_id)
    data = ast.literal_eval(data[24])
    data = list(data)
    data[0] = '✅ Имеется'
    await database.setUserData(from_id, 'license', f"\"{data}\"")
    await bot.api.messages.send(
        user_id=from_id,
        random_id=random.randint(1, 999999999),
        message=f"📒 Вы взяли права на вождение автомобилей.\n\n"
                f"⭐ ТЕПЕРЬ У ВАС ЕСТЬ ВОЗМОЖНОСТИ:\n"
                f"— Покупать автомобили в автосалонах и управлять ими\n"
                f"— Работать на работах: таксист, механик\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉 Продолжить", {"cmd": "LicensingCenter.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def PricesLicences(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'LicensingCenter.PricesLicences'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 📒 Центр лицензирования\n\n"
                f"👨 Мы являемся единственным местом лицензирования всех жителей штата. Здесь вы можете получить большинство лицензий. "
                f"Вот наш прайс-лист:\n\n"
                f"🚗 Лицензия на автомобили » 1 500 долларов (💵)\n"
                f"🏍 Лицензия на мотоциклы » 250 долларов (💵)\n"
                f"🚚 Лицензия на грузовой транспорт » 5 000 долларов (💵)\n"
                f"🔫 Лицензия на оружие » приобретается в полиции\n"
                f"🐠 Лицензия на ловлю рыбы » 500 долларов (💵)\n"
                f"🛩 Лицензия на воздушный транспорт » 50 000 (💵)\n"
                f"🛥 Лицензия на водный транспорт » 15 000 (💵)\n"
                f"🐅 Лицензия на охоту » приобретается в полиции",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "LicensingCenter.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )