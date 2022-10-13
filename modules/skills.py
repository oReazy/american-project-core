
# Скиллы персонажа

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

# Главное меню выбора навыков
async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'skills.Show'")
    await message.answer(
        message=f"🎯 » 🤹 Навыки",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🔫 Скилл оружия", {"cmd": "skills.Gun"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💪 Скилл боя", {"cmd": "skills.Fighting"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌽 Навык фермера", {"cmd": "skills.Farm"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🚚 Навык дальнобойщика", {"cmd": "skills.Trucker"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🚕 Навык таксиста", {"cmd": "skills.Taxi"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🛩 Навык пилота", {"cmd": "skills.Air"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Навык владения оружием
async def Gun(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'skills.Gun'")
    data = await database.getUserData(message.from_id)
    data = ast.literal_eval(data[29])
    data = list(data)
    await message.answer(
        message=f"🎯 » 🤹 » 🔫 Скилл оружия\n\n"
                f"🔫 Пистолет » {data[0]} / 100\n"
                f"🔫 Автомат » {data[1]} / 100\n"
                f"🔫 Дробовик » {data[2]} / 100\n"
                f"🔫 Снайперская винтовка » {data[3]} / 100\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "skills.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Навык владения боями
async def Fighting(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'skills.Fighting'")
    data = await database.getUserData(message.from_id)
    data = ast.literal_eval(data[28])
    data = list(data)
    await message.answer(
        message=f"🎯 » 🤹 » 💪 Скилл боя\n\n"
                f"Выбранный стиль боя » {data[0]}\n\n"
                f"💪 Кунг-фу » {data[1]}\n"
                f"💪 Книхед » {data[2]}\n"
                f"💪 Бокс » {data[3]}\n"
                f"💪 Элбоу » {data[4]}\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "skills.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Навык фермера
async def Farm(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'skills.Farm'")
    data = await database.getUserData(message.from_id)
    data = ast.literal_eval(data[30])
    data = list(data)
    await message.answer(
        message=f"🎯 » 🤹 » 🌽 Навык фермера\n\n"
                f"👨‍🌾 Ваш навык фермера » {data[0]}\n\n"
                f"— Для работы трактористом необходимо » 500 очков фермера\n"
                f"— Для работы комбайнером необходимо » 3000 очков фермера\n"
                f"— Для работы на кукурузнике необходимо » 7500 очков фермера\n\n"
                f"🗺 Ферму можно найти на карте в разделе «Работы для новичков»\n"
                f"👍🏻 Удачной работы",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "skills.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Навык дальнобойщика
async def Trucker(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'skills.Trucker'")
    data = await database.getUserData(message.from_id)
    data = ast.literal_eval(data[30])
    data = list(data)
    await message.answer(
        message=f"🎯 » 🤹 » 🚚 Навык дальнобойщика\n\n"
                f"🚚 Ваш навык дальнобойщика » {data[2]}\n\n"
                f"💬 Чем больше вы перевезете груза, тем больше у вас будет навык."
                f"Чем больше навык, тем больше будет прибавляться денег при получении зарплаты.\n\n"
                f"30 очков — Прибавляется 50 долларов (💵)\n"
                f"50 очков — Прибавляется 70 долларов (💵)\n"
                f"100 очков — Прибавляется 120 долларов (💵)\n"
                f"300 очков — Прибавляется 175 долларов (💵)\n"
                f"500 очков — Прибавляется 225 долларов (💵)\n"
                f"1000 очков — Прибавляется 300 долларов (💵)\n"
                f"3000 очков — Прибавляется 500 долларов (💵)\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "skills.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Навык таксиста
async def Taxi(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'skills.Taxi'")
    data = await database.getUserData(message.from_id)
    data = ast.literal_eval(data[30])
    data = list(data)
    await message.answer(
        message=f"🎯 » 🤹 » 🚕 Навык таксиста\n\n"
                f"🚕 Ваш навык таксиста » {data[3]}\n\n"
                f"💬 Чем больше ваш навык таксиста, тем больше вы сможете зарабатывать. Также "
                f"у вас появится выбор более лучшего транспорта",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "skills.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Навык пилота
async def Air(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'skills.Air'")
    data = await database.getUserData(message.from_id)
    data = ast.literal_eval(data[30])
    data = list(data)
    await message.answer(
        message=f"🎯 » 🤹 » 🛩 Навык пилота\n\n"
                f"🛩 Ваш навык пилота » {data[4]}\n\n"
                f"💬 Навык пилота складывается из количества сделанных вами перелетов из пункта А в пункт Б. "
                f"Чем больше ваш навык, тем больше у вас будет выбор, на каком из самолетов работать. "
                f"Так-как вы сможете работать на больших авиалайнерах, у вас увеличивается зарплата в несколько "
                f"раз за сложность.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "skills.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )