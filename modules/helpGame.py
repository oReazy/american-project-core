
# Раздел с помощью игры

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

# Главное меню помощи
async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'helpGame.Show'")
    setting_server = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 📖 Помощь по игре\n\n"
                f"ℹ {setting_server[1]} — игровой чат-бот, где вы можете зарабатывать игровые деньги, вступать в организации и семьи, "
                f"участвовать в мероприятиях и многое другое. Так как в нашем чат-боте очень много систем, у многих игроков возникают "
                f"вопросы, ответы на которые можно получить тут.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🔰 Часто задаваемые вопросы", {"cmd": "helpGame.List1"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🔰 Экскурсия по серверу", {"cmd": "excursion.Show1"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌐 Как заработать первые деньги?", {"cmd": "helpGame.List2"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌐 Виды лицензий", {"cmd": "helpGame.List3"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌐 Банковская карта", {"cmd": "helpGame.List4"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌐 Уровни для работ", {"cmd": "helpGame.List5"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

async def List5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'helpGame.List4'")
    await message.answer(
        message=f"🎯 » 📖 » 🌐 Уровни для работ\n\n"
                f"Каждый новый уровень игрока — это новые возможности, которые ему открываются по мере своей игры.\n\n"
                f"🚕 Таксист » 1 уровень\n"
                f"🚌 Водитель автобуса » 2 уровень\n"
                f"🌭 Продавец хотдогов » 2 уровень\n"
                f"🧰 Механик » 3 уровень\n"
                f"🚛 Водитель мусоровоза » 4 уровень\n"
                f"🚚 Дальнобойщик » 5 уровень\n"
                f"🧯 Пожарный » 6 уровень\n"
                f"🚋 Водитель трамвая » 7 уровень\n"
                f"🚈 Машинист электропоезда » 7 уровень\n"
                f"💵 Инкассатор » 8 уровень\n"
                f"✈ Пилот » 9 уровень\n"
                f"💰 Налоговая служба » 10 уровень\n"
                f"🧰 Дорожная служба » 11 уровень",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )


async def List4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'helpGame.List4'")
    await message.answer(
        message=f"🎯 » 📖 » 🌐 Банковская карта\n\n"
                f"Получить банковскую карту можно в центральном отделении банка. Найти его можно на карте -> важные места -> центральный банк. "
                f"После получения банковской карты, вы можете положить на ее счет деньги, открывать вклады, сбережения, цели и много другое.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )


async def List3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'helpGame.List3'")
    await message.answer(
        message=f"🎯 » 📖 » 🌐 Виды лицензий\n\n"
                f"В данный момент на проекте существует 8 видов лицензий.\n\n"
                f"🚗 Лицензия на автомобили » Вы сможете водить легковыми автомобилями, тем самым вы сможете управлять своим личным автомобилем\n"
                f"🏍 Лицензия на мотоциклы » Вы сможете брать в аренду мотоциклы, либо сможете управлять своим мотоциклом\n"
                f"🚚 Лицензия на грузовой транспорт » Вы сможете работать на грузовом транспорте (например на дальнобое)\n"
                f"🔫 Лицензия на оружие » Вы сможете покупать оружие в аммунации\n"
                f"🐠 Лицензия на ловлю рыбы » Вы сможете ловить рыбу в море легально\n"
                f"🛩 Лицензия на воздушный транспорт » Вы сможете управлять летательными средствами (вертолеты, самолеты). Также у вас появится возможность работать пилотом\n"
                f"🛥 Лицензия на водный транспорт » Вы сможете управлять водными средствами (лодки, яхты, катера). Также у вас появится возможность рыбачить.\n"
                f"🐅 Лицензия на охоту » Вы сможете легально вести охоту на животных в лесу\n\n"
                f"💬 Некоторые лицензии можно получить в центре лицензирования, но некоторые можно только в полиции.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )


async def List2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'helpGame.List2'")
    await message.answer(
        message=f"🎯 » 📖 » 🌐 Как заработать первые деньги?\n\n"
                f"Для того, чтобы заработать первые деньги, вам необходимо зайти в карту -> Работы для новичков -> Выберите более подходящую работу для вас. "
                f"Как только вы заработаете деньги, купите лицензии и накопите уровень, то вы сможете остроится на основные работы, либо во фракцию!",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )



async def List1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'helpGame.List1'")
    await message.answer(
        message=f"🎯 » 📖 » 🔰 Часто задаваемые вопросы\n\n"
                f"Как можно получить паспорт? — Паспорт можно получить в мэрии\n"
                f"Где можно получить лицензию на авто? — Лицензию на легковые автомобили можно получить в центре лицензирования\n"
                f"Где можно получить какую-либо лицензию? — Любые лицензии можно получить в центре лицензирования\n"
                f"Как заработать первые деньги? — Откройте карту -> работы для новичков\n"
                f"Как можно вступить во фракцию? — Следите за новостями сервера. Как только начнется набор, вам необходимо прийти во фракцию, далее на собеседование\n"
                f"Как можно стать лидером? — Через обзвон.\n"
                f"Можно ли купить админку или как стать им? — Админку купить нельзя! Стать администратором вы можете через пост лидера или через обзвон.\n"
                f"Как можно отписаться/подписаться на рассылки? — Откройте настройки персонажа -> рассылки\n"
                f"Где можно купить дом? — В риэлторском агентстве\n"
                f"Где можно купить машину? — Откройте карту -> Автосалоны",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "helpGame.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )