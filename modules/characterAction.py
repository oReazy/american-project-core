
# Действия персонажа

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

# Действия персонажа
async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'characterAction.Show'")
    await message.answer(
        message=f"🎯 » 👤 Действия персонажа",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("📊 Моя статистика", {"cmd": "characterAction.Statistics"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💼 Инвентарь", {"cmd": "inventory.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🚗 Меню автомобиля", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🏠 Меню дома", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🏪 Меню бизнеса", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🤠 Меню лидера", {"cmd": "liderfraction.Show"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("⏏ Улучшения", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("📕 Мой паспорт", {"cmd": "passport.Show"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("📒 Мои лицензии", {"cmd": "licences.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👕 Моя одежда", {"cmd": "characterAction.Clothes"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🐯 Татуировки", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("👥 Меню семьи", {"cmd": "family.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Одежда персонажа
async def Clothes(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'characterAction.Clothes'")
    data = await database.getUserData(message.from_id)

    data = ast.literal_eval(data[26])
    data = list(data)
    await message.answer(
        message=f"🎯 » 👤 » 👕 Моя одежда\n\n"
                f"🧢 Голова » {data[0]}\n"
                f"👕 Тело » {data[1]}\n"
                f"👖 Ноги » {data[2]}\n"
                f"🥾 Обувь » {data[3]}\n\n"
                f"🤚🏻 Руки » {data[4]}\n"
                f"🧣 Шея » {data[5]}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Статистика игрока
async def Statistics(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'characterAction.Statistics'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    VIP = ast.literal_eval(data[21])
    blacklist = ast.literal_eval(data[25])
    VIP = list(VIP)
    if VIP[0] == 'no vip':
        vipitog= f'❌ Отсутствует'
    else:
        if VIP[1] == 10:
            vipitog = f'{VIP[0]}, навсегда'
        else:
            endvip = datetime.datetime.utcfromtimestamp(VIP[1]).strftime('%d.%m.%Y')
            vipitog = f'{VIP[0]} до {endvip}'
    await message.answer(
        message=f"🎯 » 👤 » 📊 Моя статистика\n\n"
                f"😀 Ник » {data[3]}\n"
                f"🌐 Уровень » {data[6]}\n"
                f"🌐 Очки опыта » {data[7]} / {server_settings[20] * data[6]}\n"
                f"🚻 Пол » {data[8]}\n"
                f"🔢 Возраст » {data[9]} лет\n"
                f"🏳 Национальность » {data[10]}\n\n"
                f"💵 Доллары на руках » {await database.pretty(data[12])}\n"
                f"💶 Евро на руках » {await database.pretty(data[13])}\n"
                f"💴 Иены на руках » {await database.pretty(data[14])}\n"
                f"💷 Фунты на руках » {await database.pretty(data[15])}\n\n"
                f"🛠 Работа » {data[27]}\n"
                f"🏢 Организация » {data[22]}\n\n"
                f"🅰️ Предупреждения » {len(blacklist)}\n"
                f"💳 Банковская карта » {data[43]}\n"
                f"📱 Телефон » {data[5]}\n"
                f"👑 VIP » {vipitog}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )