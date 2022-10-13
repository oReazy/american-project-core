
# История наказаний

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'historyPunish.Show'")
    data = await database.getUserData(message.from_id)
    if data[32] == '[]':
        await message.answer(
            message=f"🎯 » 📃 История наказаний\n\n❌ История наказаний пуста.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .get_json()
            )
        )
    else:
        list_punish = ast.literal_eval(data[32])
        punish_end = ''
        count = 0
        while count < len(list_punish) or count >= 20:
            punish_end = punish_end + f'{list_punish[count]}\n'
            count = count + 1
        await message.answer(
            message=f"🎯 » 📃 История наказаний\n\n{punish_end}",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .get_json()
            )
        )