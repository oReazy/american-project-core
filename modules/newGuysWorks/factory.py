
# Завод

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'factory.Show'")
    data = await database.getUserData(message.from_id)
    if data[27] == 'Безработный' or data[27] != 'Работник завода':
        await message.answer(
            message=f"🏭 Завод\n\n"
                    f"👷 Привет, нам на завод срочно нужны работники",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.newGuysWorks"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("💼 Устроиться на работу", {"cmd": "factory.Getting"}), color=KeyboardButtonColor.POSITIVE)
                    .row()
                    .add(Text("📖 Информация по зарплатам", {"cmd": "factory.Info1"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Информация о работе", {"cmd": "factory.Info2"}), color=KeyboardButtonColor.SECONDARY)
            )
        )
    else:
        await message.answer(
            message=f"🏭 Завод\n\n"
                    f"👷 Здравствуй, {data[3]}.\n\nУ нас на заводе есть множество свободных рабочих мест.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.newGuysWorks"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("⚒ Работать", {"cmd": "factory.rab1_1"}), color=KeyboardButtonColor.POSITIVE)
                    .row()
                    .add(Text("💼 Уволиться", {"cmd": "factory.Leave"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Информация по зарплатам", {"cmd": "factory.Info1"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Информация о работе", {"cmd": "factory.Info2"}), color=KeyboardButtonColor.SECONDARY)
            )
        )


async def Getting(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'work', "'Работник завода'")
    await message.answer(
        message=f"✅ Вы успешно устроились на завод"
        )
    await Show(message, bot, api)


async def Leave(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'work', "'Безработный'")
    await message.answer(
        message=f"✅ Вы успешно уволились с работы"
        )
    await Show(message, bot, api)


async def Info1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'factory.Info1'")
    await message.answer(
        message=f"🏭 » 📖 Информация по зарплатам\n\n"
                f"На данной работе вы можете работать лишь мастером\n\n"
                f"📦 Оплата за одно изделение » 80 долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "factory.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )



async def Info2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'factory.Info2'")
    await message.answer(
        message=f"🏭 » 📖 Информация о работе\n\n"
                f"Ваша основная задача на заводе — создание изделий. Для того, чтобы сделать изделие, вам необходимо "
                f"взять рабочие инструменты и дощечку. Затем вы подходите к рабочему месту и производите изделие. После "
                f"того, как вы сделали изделие, вам необходимо его сдать и вы получите зарплату.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "factory.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )

# ---------------------------------------------------------------------------------------------------------


async def rab1_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'factory.rab1_1'")
    await database.setUserData(message.from_id, 'temporary_var', f"'0'")
    await message.answer(
        message=f"🦺 Переоденьтесь перед выходом на смену",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🦺 Переодеться", {"cmd": "factory.rab1_2"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🦺 Вы переодеваетесь')
    await asyncio.sleep(4)
    await database.setUserData(message.from_id, 'state', "'factory.rab1_2'")
    await message.answer(
        message=f"🚪 Вы надели рабочую одежду, выходите на смену",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚪 Выйти на смену", {"cmd": "factory.rab1_3"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🚪 Вы вышли из раздевалки и идете на свое рабочее место')
    await asyncio.sleep(10)
    await database.setUserData(message.from_id, 'state', "'factory.rab1_3'")
    await message.answer(
        message=f"🏭 Вы на рабочем месте. Готовы начать работу?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Готов", {"cmd": "factory.rab1_4"}), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("❌ Не готов", {"cmd": "factory.rab1_end1"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'factory.rab1_4'")
    await message.answer(
        message=f"🧰 Подойдите к столу и возьмите рабочие инструменты",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶🏼 Подойти к столу", {"cmd": "factory.rab1_5"}), color=KeyboardButtonColor.SECONDARY)
        )
    )

async def rab1_5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🚶🏼 Вы подходите к столу')
    await asyncio.sleep(4)
    await database.setUserData(message.from_id, 'state', "'factory.rab1_5'")
    await message.answer(
        message=f"🧰 Возьмите инструменты",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🧰 Взять инструменты", {"cmd": "factory.rab1_6"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_6(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'factory.rab1_6'")
    await message.answer(
        message=f"🌲 Возьмите брусок дерева",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🌲 Взять брусок дерева", {"cmd": "factory.rab1_7"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_7(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🌲 Вы взяли брусок дерева')
    await database.setUserData(message.from_id, 'state', "'factory.rab1_7'")
    await message.answer(
        message=f"🚶🏼 Возвращайтесь на свое рабочее место",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶🏼 Вернуться на рабочее место", {"cmd": "factory.rab1_8"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_8(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🚶🏼 Вы идете обратно к своему рабочему месту')
    await asyncio.sleep(4)
    await database.setUserData(message.from_id, 'state', "'factory.rab1_8'")
    await message.answer(
        message=f"🧰 Разложите все инструменты на своем рабочем месте",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🧰 Разложить инструменты и материалы", {"cmd": "factory.rab1_9"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_9(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🧰 Вы раскладываете инструменты и материалы...')
    await asyncio.sleep(4)
    await database.setUserData(message.from_id, 'state', "'factory.rab1_9'")
    await message.answer(
        message=f"🛠 Начните мастерить изделие",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🛠 Начать мастерить", {"cmd": "factory.rab1_10"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_10(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🛠 Вы мастерите изделие...')
    await asyncio.sleep(8)
    await message.answer('🛠 Вы красите изделие...')
    await asyncio.sleep(5)
    await message.answer('📦 Вы упаковываете изделие...')
    await asyncio.sleep(3)
    await database.setUserData(message.from_id, 'state', "'factory.rab1_10'")
    await message.answer(
        message=f"📦 Ваше изделие готово, положите его на общий стол",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("📦 Положить изделие на общий стол", {"cmd": "factory.rab1_11"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_11(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('📦 Вы положили изделие на общий стол.')
    await asyncio.sleep(3)
    await database.setUserData(message.from_id, 'state', "'factory.rab1_11'")
    await message.answer(
        message=f"🧰 Теперь вам необходимо сдать инструменты.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🧰 Сдать инструменты", {"cmd": "factory.rab1_12"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_12(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🧰 Вы сдаете инструменты...')
    await asyncio.sleep(3)
    await message.answer('🧰 Вы сдали инструменты')
    await rab1_13(message, bot, api)


async def rab1_13(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data = await database.getUserData(message.from_id)
    new_data = int(data[44]) + 1
    await database.setMultiUserData(message.from_id, f"temporary_var = '{new_data}'")
    await rab1_14(message, bot, api)


async def rab1_14(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'rab1_14'")
    await message.answer(
        message=f"🛠 Готовы ли вы еще смастерить изделие?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Готов", {"cmd": "factory.rab1_4"}), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("🚶🏻 Закончить смену", {"cmd": "factory.rab1_end2"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_end2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'factory.Show'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    zarplata = int(data[44]) * 80 * server_settings[26]
    itog = int(data[12]) + zarplata
    await database.setUserData(message.from_id, 'dollars', f"'{itog}'")
    await message.answer(
        message=f"👷 » Спасибо за смену. Вы сделали {int(data[44])} изделий. Ты заработал {zarplata} долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💵 Забрать деньги", {"cmd": "factory.Show"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_end1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🚪 Вы отказались работать, вы идете обратно в раздевалку сдавать рабочую одежду')
    await asyncio.sleep(10)
    await database.setUserData(message.from_id, 'state', "'factory.Show'")
    await message.answer(
        message=f"✅ Вы сдали рабочую одежду. Так-как вы ушли со смены, вы ничего не заработали."
    )
    await Show(message, bot, api)