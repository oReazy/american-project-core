
# Паспорт

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database, characterAction


# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[35] == '❌ Отсутствует':
        await message.answer(
            message=f"❌ У вас нет паспорта. Сделать вы его можете в мэрии")
        await characterAction.Show(message, bot, api)
    else:
        await database.setUserData(message.from_id, 'state', "'passport.Show'")
        temporary = ast.literal_eval(data[31])
        blacklist_end = ''
        count = 0
        while count < len(temporary):
            blacklist_end = blacklist_end + f'{temporary[count]}\n'
            count = count + 1
        if count == 0:
            await message.answer(
                message=f"🎯 » 👤 » 📕 Мой паспорт\n\n"
                        f"😀 Имя » {data[3]}\n"
                        f"🌐 Лет в штате » {data[6]}\n"
                        f"📕 Серия » {data[36]}\n"
                        f"📕 Номер » {data[37]}\n"
                        f"🚻 Семейное положение » {data[38]}\n"
                        f"🏠 Прописка » \n\n"
                        f"🛠 Работа » {data[27]}\n"
                        f"📓 Военный билет » {data[39]}\n\n"
                        f"{blacklist_end}",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("◀ Назад", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.PRIMARY)
                        .get_json()
                )
            )
        else:
            await message.answer(
                message=f"🎯 » 👤 » 📕 Мой паспорт\n\n"
                        f"😀 Имя » {data[3]}\n"
                        f"🌐 Лет в штате » {data[6]}\n"
                        f"📕 Серия » {data[36]}\n"
                        f"📕 Номер » {data[37]}\n"
                        f"🚻 Семейное положение » {data[38]}\n"
                        f"🏠 Прописка » \n\n"
                        f"🛠 Работа » {data[27]}\n"
                        f"📓 Военный билет » {data[39]}\n\n"
                        f"⛔ Вы находитесь в черных списках фракций:\n"
                        f"{blacklist_end}",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("◀ Назад", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.PRIMARY)
                        .get_json()
                )
            )