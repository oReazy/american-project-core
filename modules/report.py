
# Репорт

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database, mainMenu

# ----------------------------------------------------------------------------------------------------------------------

async def Check(message: Message, bot: Bot, api: API):
    await Show(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'report.Show'")
    data = await database.getUserData(message.from_id)
    if int(data[46]) <= int(time.time()):
        await message.answer(
            message=f"🎯 » 📣 Связь с администрацией\n\n"
                    f"💬 Вы собираетесь отправить сообщение для администрации. Будьте внимательны, чтобы ваш репорт не нарушал правила, "
                    f"которые написаны ниже.\n\n"
                    f"⛔ Запрещено:\n"
                    f"— Флудить, оскорблять, оффтопить\n"
                    f"— Просить что-либо (дайте денег, дайте лидеру, дайте что-то)\n"
                    f"— Ложные сообщения\n\n"
                    f"⚠ За нарушение данных правил, администрация в праве:\n"
                    f"— Предупредить (Warn)\n"
                    f"— Выдать вам мут или выдать только мут репорта (Mute)\n"
                    f"— Заблокировать аккаунт (Ban)\n"
                    f"— Удалить аккаунт (Delite)\n\n"
                    f"Если вам долго не отвечают, подождите пару минут.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("📣 Отправить репорт", {"cmd": "report.Send"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    else:
        await message.answer(
            message=f"❌ Писать сообщения в репорт можно раз в 3 минуты",
        )
        await database.setUserData(message.from_id, 'state', "'mainMenu.Show'")
        await mainMenu.Show(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

async def Send(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'report.SendCheck'")
    await message.answer(
        message=f"🎯 » 📣 » 📣 Отправить репорт\n\n"
                f"📝 Напишите ваш репорт",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отмена", {"cmd": "report.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )


async def SendCheck(message: Message, bot: Bot, api: API):
    if len(message.text) < 300:
        new_time = int(time.time()) + 180
        await database.setUserData(message.from_id, 'limit_report', f"'{new_time}'")
        data = await database.getUserData(message.from_id)
        data_now = datetime.date.today()
        time_now = datetime.datetime.now()
        await database.addMultiBdData('report', "vk_id_user, nick_user, vk_id_admin, nick_admin, text, answer, data", f"'{message.from_id}', '{data[3]}','0', '','{message.text}', '', '{data_now.day}.{data_now.month}.{data_now.year} {time_now.hour}:{time_now.minute}:{time_now.second}'")
        await message.answer(
            message=f"✅ Ваш репорт был отправлен администрации",
        )
        await database.setUserData(message.from_id, 'state', "'mainMenu.Show'")
        await mainMenu.Show(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Вы написали слишком длинный репорт",
        )
        await database.setUserData(message.from_id, 'state', "'report.Send'")
        await Send(message, bot, api)