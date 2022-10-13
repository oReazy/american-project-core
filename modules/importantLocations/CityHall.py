
# Мэрия

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CityHall.Show'")
    data = await database.getUserData(message.from_id)
    if data[35] == '❌ Отсутствует':
        await message.answer(
            message=f"🎯 » 🗺 » 🏛 » 🏛 Мэрия\n\n"
                    f"👱‍♀ Добро пожаловать в мэрию, чем могу быть обязана?",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("📕 Получить паспорт", {"cmd": "CityHall.getPassport1"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("👨‍💼 Кто является губернатором", {"cmd": "CityHall.president"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    else:
        await message.answer(
            message=f"🎯 » 🗺 » 🏛 » 🏛 Мэрия\n\n"
                    f"👱‍♀ Добро пожаловать в мэрию, чем могу быть обязана?",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("👨‍💼 Кто является губернатором", {"cmd": "CityHall.president"}),
                         color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )



async def getPassport1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CityHall.getPassport1'")
    await message.answer(
        message=f"👱‍♀ Если вам нужен паспорт, то пожалуйста возьмите анкету и карандаш",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("📝 Взять анкету и карандаш", {"cmd": "CityHall.getPassport2"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def getPassport2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'CityHall.getPassport2'")
    await message.answer(
        message=f"👱‍♀ Отлично, на этой анкете напишите как вас зовут, какого вы года рождения, а также всю остальную важную информацию",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("✏ Записать данные на листочек", {"cmd": "CityHall.getPassport3"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def getPassport3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer("✏ Вы заполняете анкету...")
    await asyncio.sleep(10)
    await database.setUserData(message.from_id, 'state', "'CityHall.getPassport3'")
    await message.answer("✏ Вы закончили заполнять анкету и отдали ее сотруднице")
    await asyncio.sleep(5)
    await message.answer("👱‍♀ Так, дайте мне немного времени для того, чтобы я могла выдать вам паспорт")
    await asyncio.sleep(25)
    await message.answer(
        message=f"👱‍♀ Все готово, держите ваш паспорт.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Callback("📕 Взять паспорт", payload={"cmd": "CityHall.getPassport"}), color=KeyboardButtonColor.SECONDARY)
        )
    )

async def GetPassport(from_id, bot: Bot):
    await database.setUserData(from_id, 'state', "'CityHall.Show'")
    await database.setUserData(from_id, 'passport', "'✅ Имеется'")
    await database.setUserData(from_id, 'passport_serial', f"'{random.randint(1000, 9999)}'")
    await database.setUserData(from_id, 'passport_number', f"'{random.randint(100000, 999999)}'")
    await bot.api.messages.send(
        user_id=from_id,
        random_id=random.randint(1, 999999999),
        message=f"📕 Вы получили паспорт\n\n"
                f"⭐ ТЕПЕРЬ У ВАС ЕСТЬ ВОЗМОЖНОСТИ:\n"
                f"— Покупать имущество (автомобили, дома, бизнесы)\n"
                f"— Вступать в государственные организации\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉 Продолжить", {"cmd": "CityHall.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def president(message: Message, bot: Bot, api: API):
    fraction_info = await database.getBdData('fractions', 'id', "'1'")
    if fraction_info[2] == 'Не назначен!':
        await message.answer(
            message=f"👱‍♀ В данный момент в нашем штате нет губернатора"
        )
        await asyncio.sleep(3)
        await Show(message, bot, api)
    else:
        await asyncio.sleep(3)
        await message.answer(
            message=f"👱‍♀ В данный момент пост губернатора занимает {fraction_info[2]}"
        )
        await Show(message, bot, api)