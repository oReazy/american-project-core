
# Раздел с лицензиями

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    data = ast.literal_eval(data[24])
    data = list(data)
    await database.setUserData(message.from_id, 'state', "'licences.Show'")
    await message.answer(
        message=f"🎯 » 👤 » 📒 Мои лицензии\n\n"
                f"🚗 Лицензия на автомобили » {data[0]}\n"
                f"🏍 Лицензия на мотоциклы » {data[1]}\n"
                f"🚚 Лицензия на грузовой транспорт » {data[2]}\n"
                f"🔫 Лицензия на оружие » {data[3]}\n"
                f"🐠 Лицензия на ловлю рыбы » {data[4]}\n"
                f"🛩 Лицензия на воздушный транспорт » {data[5]}\n"
                f"🛥 Лицензия на водный транспорт » {data[6]}\n"
                f"🐅 Лицензия на охоту » {data[7]}\n\n"
                f"💬 Некоторые лицензии можно получить в центре лицензирования, но некоторые можно только "
                f"в полиции.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )