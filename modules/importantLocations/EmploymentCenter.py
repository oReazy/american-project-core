
# Центр трудоустройства

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'EmploymentCenter.Show'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » ⚒ Центр занятости\n\n🧑 » Здраствуйте, мы в данный момент закрыты.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🛠 Найти работу", {"cmd": "EmploymentCenter.none"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )