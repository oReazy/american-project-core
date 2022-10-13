
# История ников

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'historyNicks.Show'")
    data = await database.getUserData(message.from_id)
    if data[33] == '[]':
        await message.answer(
            message=f"🎯 » 📃 История ников\n\n❌ История ников пуста.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .get_json()
            )
        )
    else:
        list_nicks = ast.literal_eval(data[33])
        nicks_end = ''
        count = 0
        while count < len(list_nicks) or count >= 20:
            nicks_end = nicks_end + f'{list_nicks[count]}\n'
            count = count + 1
        await message.answer(
            message=f"🎯 » 📃 История ников\n\n{nicks_end}",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .get_json()
            )
        )