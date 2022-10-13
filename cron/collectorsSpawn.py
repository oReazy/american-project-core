
# Мероприятие собиратели

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, ast, json, time, datetime, random, traceback
from vkbottle.bot import Bot, Message, MessageEvent
from vkbottle import API, LoopWrapper, GroupEventType

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

bot = Bot('aed307a7c1248aea24454fb0e44d8c6c94c92255e759f701023ab1963501be1683acfd6fea6fe0596a28a')
api = API('25a06c2cbdd3d2788f0af4bc75c6c4b5ede3e807d16143eafe0e03ff286ac2089760a2d7da9ac8b1a9415')
lw = LoopWrapper()

# ----------------------------------------------------------------------------------------------------------------------

async def CollectorsSpawn(bot: Bot, api: API):
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await asyncio.sleep(20)
    await database.setBdData('event', 'id', "'0'", 'playersOnline', "'0'")
    await database.setBdData('event', 'id', "'0'", 'count', "'60'")
    min = 0
    while min < 60:
        await asyncio.sleep(int(random.randint(40, 60)))
        await database.setBdData('event', 'id', "'0'", 'count', "'60'")
        min = min + 1
    await database.setBdData('event', 'id', "'0'", 'count', "'0'")
    await database.setBdData('event', 'id', "'0'", 'playersOnline', "'0'")


bot.loop_wrapper.add_task(CollectorsSpawn(bot, api))