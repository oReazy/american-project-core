
# Главное меню

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

# Стандартное меню
async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'mainMenu.Show'")
    data = await database.getUserData(message.from_id)

    # Проверка, включен ли у игрока компактный режим
    if data[47] == 1:
        await Mini(message, bot, api)
    else:
        server_settings = await database.getBdData('settings', 'id', "'1'")
        num1 = await database.pretty(data[11])
        real_time = datetime.datetime.now()
        real_time_hour = real_time.hour
        real_time_minute = real_time.minute
        TEXT_OBJ = ''
        if int(real_time.hour) == 20:
            if int(5 <= real_time.minute < 10):
                TEXT_OBJ = '🥚 Мероприятие «Собиратели» уже скоро начнется. Найти данное мероприятие можно во вкладке «🗺 Карта», в категории «🎭 Мероприятия»\n\n'
        if data[11] == 0:
            await message.answer(
                message=f"🎯 Главное меню{server_settings[21]}\n\n{TEXT_OBJ}"
                        f"💵 Доллары на руках » {num1}\n",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                    .add(Text("👤 Действия персонажа", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📱 Телефон", {"cmd": "telephone.Check"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🗺 Карта", {"cmd": "map.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🤹 Навыки", {"cmd": "skills.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("💎 Донат", {"cmd": "donate.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("⚙ Настройки персонажа", {"cmd": "settings.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📣 Связь с администрацией", {"cmd": "report.Check"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Помощь по игре", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📖 Правила", {"cmd": "game_rule.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📃 История наказаний", {"cmd": "historyPunish.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📃 История ников", {"cmd": "historyNicks.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
                )
            )
        else:
            await message.answer(
                message=f"🎯 Главное меню{server_settings[21]}\n\n{TEXT_OBJ}"
                        f"💵 Доллары на руках » {num1}\n"
                        f"💶 Евро на руках » {num2}\n"
                        f"💴 Иены на руках » {num3}\n"
                        f"💷 Фунты на руках » {num4}",
                keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("🛠 Админ-панель", {"cmd": "admin.Check"}), color=KeyboardButtonColor.POSITIVE)
                    .row()
                    .add(Text("👤 Действия персонажа", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📱 Телефон", {"cmd": "telephone.Check"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🗺 Карта", {"cmd": "map.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🤹 Навыки", {"cmd": "skills.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("💎 Донат", {"cmd": "donate.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("⚙ Настройки персонажа", {"cmd": "settings.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📣 Связь с администрацией", {"cmd": "report.Check"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Помощь по игре", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📖 Правила", {"cmd": "game_rule.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📃 История наказаний", {"cmd": "historyPunish.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📃 История ников", {"cmd": "historyNicks.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
                )
            )


async def ShowFixFromId(from_id, bot: Bot, api: API):
    await database.setUserData(from_id, 'state', "'mainMenu.Show'")
    data = await database.getUserData(from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    if data[47] == 1:
        await MiniFix(from_id, bot, api)
    else:
        num1 = await database.pretty(data[12])
        num2 = await database.pretty(data[13])
        num3 = await database.pretty(data[14])
        num4 = await database.pretty(data[15])
        real_time = datetime.datetime.now()
        real_time_hour = real_time.hour
        real_time_minute = real_time.minute
        TEXT_OBJ = ''
        if int(real_time.hour) == 20:
            if int(5 <= real_time.minute < 10):
                TEXT_OBJ = '🥚 Мероприятие «Собиратели» уже скоро начнется. Найти данное мероприятие можно во вкладке «🗺 Карта», в категории «🎭 Мероприятия»\n\n'
        if data[11] == 0:
            await bot.api.messages.send(
                user_id=from_id,
                random_id=random.randint(1, 999999999),
                message=f"🎯 Главное меню{server_settings[21]}\n\n{TEXT_OBJ}"
                        f"💵 Доллары на руках » {num1}\n"
                        f"💶 Евро на руках » {num2}\n"
                        f"💴 Иены на руках » {num3}\n"
                        f"💷 Фунты на руках » {num4}",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                    .add(Text("👤 Действия персонажа", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📱 Телефон", {"cmd": "telephone.Check"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🗺 Карта", {"cmd": "map.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🤹 Навыки", {"cmd": "skills.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("💎 Донат", {"cmd": "donate.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("⚙ Настройки персонажа", {"cmd": "settings.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📣 Связь с администрацией", {"cmd": "report.Check"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Помощь по игре", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📖 Правила", {"cmd": "game_rule.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📃 История наказаний", {"cmd": "historyPunish.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📃 История ников", {"cmd": "historyNicks.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
                )
            )
        else:
            await bot.api.messages.send(
                user_id=from_id,
                random_id=random.randint(1, 999999999),
                message=f"🎯 Главное меню{server_settings[21]}\n\n{TEXT_OBJ}"
                        f"💵 Доллары на руках » {num1}\n"
                        f"💶 Евро на руках » {num2}\n"
                        f"💴 Иены на руках » {num3}\n"
                        f"💷 Фунты на руках » {num4}",
                keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("🛠 Админ-панель", {"cmd": "admin.Check"}), color=KeyboardButtonColor.POSITIVE)
                    .row()
                    .add(Text("👤 Действия персонажа", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📱 Телефон", {"cmd": "telephone.Check"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🗺 Карта", {"cmd": "map.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🤹 Навыки", {"cmd": "skills.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("💎 Донат", {"cmd": "donate.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("⚙ Настройки персонажа", {"cmd": "settings.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📣 Связь с администрацией", {"cmd": "report.Check"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Помощь по игре", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📖 Правила", {"cmd": "game_rule.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📃 История наказаний", {"cmd": "historyPunish.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📃 История ников", {"cmd": "historyNicks.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
                )
            )


async def Mini(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'mainMenu.Mini'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    num1 = await database.pretty(data[12])
    num2 = await database.pretty(data[13])
    num3 = await database.pretty(data[14])
    num4 = await database.pretty(data[15])
    real_time = datetime.datetime.now()
    real_time_hour = real_time.hour
    real_time_minute = real_time.minute
    TEXT_OBJ = ''
    if int(real_time.hour) == 20:
        if int(5 <= real_time.minute < 10):
            TEXT_OBJ = '🥚 Мероприятие «Собиратели» уже скоро начнется. Найти данное мероприятие можно во вкладке «🗺 Карта», в категории «🎭 Мероприятия»\n\n'
    if data[11] == 0:
        await message.answer(
            message=f"🎯 Главное меню{server_settings[21]}\n\n{TEXT_OBJ}"
                    f"💵 Доллары на руках » {num1}\n"
                    f"💶 Евро на руках » {num2}\n"
                    f"💴 Иены на руках » {num3}\n"
                    f"💷 Фунты на руках » {num4}",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("👤", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📱", {"cmd": "telephone.Check"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🗺", {"cmd": "map.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🤹", {"cmd": "skills.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("💎", {"cmd": "donate.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("⚙ Настройки", {"cmd": "settings.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📣 Репорт", {"cmd": "report.Check"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Помощь по игре", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📖 Правила", {"cmd": "game_rule.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📃 История наказаний", {"cmd": "historyPunish.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📃 История ников", {"cmd": "historyNicks.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    if data[11] > 0:
        await message.answer(
            message=f"🎯 Главное меню{server_settings[21]}\n\n{TEXT_OBJ}"
                    f"💵 Доллары на руках » {num1}\n"
                    f"💶 Евро на руках » {num2}\n"
                    f"💴 Иены на руках » {num3}\n"
                    f"💷 Фунты на руках » {num4}",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("🛠 Админ-панель", {"cmd": "admin.Check"}), color=KeyboardButtonColor.POSITIVE)
                    .row()
                    .add(Text("👤", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📱", {"cmd": "telephone.Check"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🗺", {"cmd": "map.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🤹", {"cmd": "skills.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("💎", {"cmd": "donate.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("⚙ Настройки", {"cmd": "settings.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📣 Репорт", {"cmd": "report.Check"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Помощь по игре", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📖 Правила", {"cmd": "game_rule.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📃 История наказаний", {"cmd": "historyPunish.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📃 История ников", {"cmd": "historyNicks.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )




async def MiniFix(from_id, bot: Bot, api: API):
    await database.setUserData(from_id, 'state', "'mainMenu.Mini'")
    data = await database.getUserData(from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    num1 = await database.pretty(data[12])
    num2 = await database.pretty(data[13])
    num3 = await database.pretty(data[14])
    num4 = await database.pretty(data[15])
    real_time = datetime.datetime.now()
    real_time_hour = real_time.hour
    real_time_minute = real_time.minute
    TEXT_OBJ = ''
    if int(real_time.hour) == 20:
        if int(5 <= real_time.minute < 10):
            TEXT_OBJ = '🥚 Мероприятие «Собиратели» уже скоро начнется. Найти данное мероприятие можно во вкладке «🗺 Карта», в категории «🎭 Мероприятия»\n\n'
    if data[11] == 0:
        await bot.api.messages.send(
            user_id=from_id,
            random_id=random.randint(1, 999999999),
            message=f"🎯 Главное меню{server_settings[21]}\n\n{TEXT_OBJ}"
                    f"💵 Доллары на руках » {num1}\n"
                    f"💶 Евро на руках » {num2}\n"
                    f"💴 Иены на руках » {num3}\n"
                    f"💷 Фунты на руках » {num4}",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("👤", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📱", {"cmd": "telephone.Check"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🗺", {"cmd": "map.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🤹", {"cmd": "skills.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("💎", {"cmd": "donate.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("⚙ Настройки", {"cmd": "settings.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📣 Репорт", {"cmd": "report.Check"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Помощь по игре", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📖 Правила", {"cmd": "game_rule.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📃 История наказаний", {"cmd": "historyPunish.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📃 История ников", {"cmd": "historyNicks.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    if data[11] > 0:
        await bot.api.messages.send(
            user_id=from_id,
            random_id=random.randint(1, 999999999),
            message=f"🎯 Главное меню{server_settings[21]}\n\n{TEXT_OBJ}"
                    f"💵 Доллары на руках » {num1}\n"
                    f"💶 Евро на руках » {num2}\n"
                    f"💴 Иены на руках » {num3}\n"
                    f"💷 Фунты на руках » {num4}",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("🛠 Админ-панель", {"cmd": "admin.Check"}), color=KeyboardButtonColor.POSITIVE)
                    .row()
                    .add(Text("👤", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📱", {"cmd": "telephone.Check"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🗺", {"cmd": "map.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🤹", {"cmd": "skills.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("💎", {"cmd": "donate.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("⚙ Настройки", {"cmd": "settings.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📣 Репорт", {"cmd": "report.Check"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Помощь по игре", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📖 Правила", {"cmd": "game_rule.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📃 История наказаний", {"cmd": "historyPunish.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📃 История ников", {"cmd": "historyNicks.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )