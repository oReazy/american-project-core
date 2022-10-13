
# Система семей

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'family.Show'")
    data = await database.getUserData(message.from_id)
    if int(data[49]) == -1:
        await message.answer(
            message=f"❌ Вы не состоите в семье",
        )
        await characterAction.Show(message, bot, api)
    else:
        await message.answer(
            message=f"❌ В разработке",
        )
        await characterAction.Show(message, bot, api)