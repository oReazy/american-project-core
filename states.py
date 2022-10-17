# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# Игровой Role-Play чат-бот для ВКонтакте.
#
# Автор: Reazy, 2022 год.

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import asyncio, ast, json, time, datetime, random, traceback
from vkbottle.bot import Bot, Message, MessageEvent
from vkbottle import API, LoopWrapper, GroupEventType

from modules import database
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

STATES = {'registration.registration_1': registration.registration_1,
        }