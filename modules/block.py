import asyncio

import vkbottle.api
import vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
import json, time, os, sys
from modules import database


# ------------------------------------------------------------------------------------------

# Блокирует любое взаимодействие с ботом

# -------------------------------------------------------------------------------------------

async def Show(message, bot, api):
    print(f'\033[38m[\033[34m!\033[38m][\033[33mDEBUG\033[38m] Пользователь пытался что-то сделать, когда находился в блокировке.')