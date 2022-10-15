# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# Игровой Role-Play чат-бот для ВКонтакте.
#
# Автор: Reazy, 2022 год.

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import asyncio, ast, json, time, datetime, random, traceback
from vkbottle.bot import Bot, Message, MessageEvent
from vkbottle import API, LoopWrapper, GroupEventType

from modules import database, registration, excursion
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

STATES = {'registration.registration_1': registration.registration_1,
          'registration.registration_1_check': registration.registration_1_check,
          'registration.registration_2': registration.registration_2,
          'registration.registration_2_man': registration.registration_2_man,
          'registration.registration_2_woman': registration.registration_2_woman,
          'registration.registration_3': registration.registration_3,
          'registration.registration_3_check': registration.registration_3_check,
          'registration.registration_4': registration.registration_4,
          'registration.registration_4_check': registration.registration_4_check,
          'registration.registration_5': registration.registration_5,
          'registration.registration_5_friend': registration.registration_5_friend,
          'registration.registration_5_list_chatbot': registration.registration_5_list_chatbot,
          'registration.registration_5_search': registration.registration_5_search,
          'registration.registration_5_youtube': registration.registration_5_youtube,
          'registration.registration_5_other': registration.registration_5_other,
          'registration.registration_6': registration.registration_6,
          'registration.registration_6_accept': registration.registration_6_accept,
          'registration.registration_6_denial': registration.registration_6_denial,
          'registration.registration_7': registration.registration_7,
          'registration.registration_8': registration.registration_8,
          'registration.registration_9': registration.registration_9,
          'registration.registration_9_1': registration.registration_9_1,
          'registration.newAccaunt': registration.newAccaunt,
          'excursion.Show1': excursion.Show1,
          'excursion.Show2': excursion.Show2,
          'excursion.Show3': excursion.Show3,
          'excursion.Show4': excursion.Show4,
          'excursion.Show5': excursion.Show5,
          'excursion.Show6': excursion.Show6,
          'excursion.Show7': excursion.Show7,
          'excursion.Show8': excursion.Show8,
          'excursion.Show9': excursion.Show9,
          'excursion.Show10': excursion.Show10,
          'excursion.Show11': excursion.Show11,
        }