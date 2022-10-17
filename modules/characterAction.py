
# Действия персонажа

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# Действия персонажа
async def Show(message: Message, bot: Bot, api: API, DATA_USER, DATA_SETTINGS):
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
async def Clothes(message: Message, bot: Bot, api: API, DATA_USER, DATA_SETTINGS):
    await database.setUserData(message.from_id, 'state', "'characterAction.Clothes'")

    data = ast.literal_eval(DATA_USER[26])
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
async def Statistics(message: Message, bot: Bot, api: API, DATA_USER, DATA_SETTINGS):
    await database.setUserData(message.from_id, 'state', "'characterAction.Statistics'")
    VIP = ast.literal_eval(DATA_USER[15])
    blacklist = ast.literal_eval(DATA_USER[25])
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
                f"😀 Ник » {DATA_USER[3]}\n"
                f"🌐 Уровень » {DATA_USER[6]}\n"
                f"🌐 Очки опыта » {DATA_USER[7]} / {DATA_SETTINGS[20] * DATA_USER[6]}\n"
                f"🚻 Пол » {DATA_USER[8]}\n"
                f"🔢 Возраст » {DATA_USER[9]} лет\n"
                f"🏳 Национальность » {DATA_USER[10]}\n\n"
                f"💵 Доллары на руках » {await database.pretty(DATA_USER[12])}\n\n"
                f"🛠 Работа » {DATA_USER[21]}\n"
                f"🏢 Организация » {DATA_USER[16]}\n\n"
                f"🅰️ Предупреждения » {len(blacklist)}\n"
                f"💳 Банковская карта » {DATA_USER[37]}\n"
                f"📱 Телефон » {DATA_USER[5]}\n"
                f"👑 VIP » {vipitog}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )