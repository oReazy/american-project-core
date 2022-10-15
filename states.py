# ----------------------------------------------------------------------------------------------------------------------

# Игровой Role-Play чат-бот для ВКонтакте.
#
# Автор: Reazy, 2022 год.

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, ast, states, json, time, datetime, random, traceback
from vkbottle.bot import Bot, Message, MessageEvent
from vkbottle import API, LoopWrapper, GroupEventType

from modules import database, registration
# ----------------------------------------------------------------------------------------------------------------------

STATES = {'registration.registration_1': registration.registration_1,
          'registration.registration_1_check': registration.registration_1_check,
          'registration.registration_2': registration.registration_2,
          'registration.registration_2_man': registration.registration_2_man,
          'registration.registration_2_woman': registration.registration_2_woman,
          'registration.registration_3': registration.registration_3,
        }