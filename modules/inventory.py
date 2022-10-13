
# История ников

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'inventory.Show'")
    inventory = await database.getUserData(message.from_id)

    inventory = ast.literal_eval(inventory[48])
    inventory = list(inventory)

    # massive = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # print(len(massive))
    #
    # inventory = str(inventory)
    # inventory = inventory.replace("'", "")
    # print(inventory)

    await database.setUserData(message.from_id, 'state', "'inventory.Show'")
    count = 0 + len(inventory)
    while count < 7:
        inventory.append(0)
        count = count + 1
    await database.setUserData(message.from_id, 'inventory', f"'{inventory}'")
    await message.answer(
        message=f"🎯 » 👤 » 💼 Инвентарь\n\n"
                f"🧿 Фишки казино » {inventory[0]} шт.\n"
                f"🌲 Дерево » {inventory[1]} шт.\n"
                f"📦 Металл » {inventory[2]} шт.\n"
                f"🎁 Подарок » {inventory[3]} шт.\n"
                f"🥉 Бронзовая рулетка » {inventory[4]} шт.\n"
                f"🥈 Серебряная рулетка » {inventory[5]} шт.\n"
                f"🥇 Золотая рулетка » {inventory[6]} шт.\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "characterAction.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )