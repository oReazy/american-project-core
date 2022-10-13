
# Спортивный зал

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'SportsHall.Show'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 💪 Спортивный зал\n\n"
                f"🧔 » Здраствуйте. Вы пришли в лучший спортивный зал в этом штате.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🚶 Войти в зал", {"cmd": "SportsHall.ShowEntry"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def ShowEntry(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'SportsHall.ShowEntry'")
    await message.answer(
        message=f"🧔 » Стоимость входа в спортивный зал составляет 750 долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "SportsHall.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("💵 Войти в зал", {"cmd": "SportsHall.ShowEntryCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def ShowEntryCheck(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data = await database.getUserData(message.from_id)
    if data[12] >= 750:
        new_data = int(data[12]) - 750
        await database.setUserData(message.from_id, 'dollars', f"'{new_data}'")
        await ShowSportsHall(message, bot, api)
    else:
        await message.answer(
            message=f"❌ У вас недостаточно денег на руках, чтобы заплатить за вход в спортзал"
        )
        await ShowEntry(message, bot, api)