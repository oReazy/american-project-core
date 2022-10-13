
# Мероприятие "Собиратели"

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'collectors.Show'")
    await message.answer(
        message=f"🎯 » 🗺 » 🎭 » 🥚 Собиратели\n\n"
                f"👦🏽 Мартин » Добро пожаловать, чем могу быть обязан?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "map.events"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("💸 Купить билет и войти", {"cmd": "collectors.Buy"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("ℹ Когда начнется мероприятие", {"cmd": "collectors.info1"}),
                     color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("ℹ Что надо делать на данном мероприятии?", {"cmd": "collectors.info2"}),
                     color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("ℹ Сколько людей на мероприятии?", {"cmd": "collectors.info3"}),
                     color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("ℹ Сколько стоит участие?", {"cmd": "collectors.info4"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def info1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'collectors.info1'")
    await message.answer(
        message=f"🎯 » 🗺 » 🎭 » 🥚 » ℹ Когда начнется мероприятие\n\n"
                f"👦🏽 Мартин » Мероприятие собиратели проходит каждый день с 20:15 до 21:00 по Московскому времени",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "collectors.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )


async def info2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'collectors.info2'")
    await message.answer(
        message=f"🎯 » 🗺 » 🎭 » 🥚 » ℹ Что надо делать на данном мероприятии?\n\n"
                f"👦🏽 Мартин » На данном мероприятии вам надо будет собирать пасхальные яйца. Они появляются каждую минуту. "
                f"Но будьте внимательны, ведь кроме вас играют другие игроки и они также хотят забрать яйца!\n\n"
                f"После взятия яйца (🥚), они превращаются в подарки (🎁). Подарки можно обменять у Эдварда, либо продать на центральном рынке",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "collectors.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )


async def info3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'collectors.info3'")
    event_data = await database.getBdData('event', 'id', "'0'")
    await message.answer(
        message=f"🎯 » 🗺 » 🎭 » 🥚 » ℹ Сколько людей на мероприятии?\n\n"
                f"👦🏽 Мартин » Сейчас на мероприятии присутствуют {event_data[3]} игроков",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "collectors.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )


async def info4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'collectors.info3'")
    await message.answer(
        message=f"🎯 » 🗺 » 🎭 » 🥚 » ℹ Сколько стоит участие?\n\n"
                f"👦🏽 Мартин » Участие на данном мероприятии стоит 30 000 долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "collectors.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )


# ---------------------------------------------------------------------------------------------


async def Buy(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    real_time = datetime.datetime.now()
    if int(real_time.hour) == 20:
        if int(real_time.minute) < 15 or int(real_time.minute) > 59:
            await message.answer(
                message=f"❌ В данный момент мероприятие не проводится! Приходите позже",
            )
            await Show(message, bot, api)
        else:
            data = await database.getUserData(message.from_id)
            if int(data[50]) <= int(time.time()):
                if int(data[6]) >= 3:
                    if int(data[12]) >= 30000:
                        event_data = await database.getBdData('event', 'id', "'0'")
                        new_online = int(event_data[3]) + 1
                        await database.setBdData('event', 'id', "'0'", 'playersOnline', f"'{new_online}'")
                        new_dollars = int(data[12]) - 30000
                        await database.setUserData(message.from_id, 'dollars', f"'{new_dollars}'")

                        if event_data[3] <= 0:
                            time_event = 300
                            await database.setMultiUserData(message.from_id, f"timeEventCollectors = '{int(time.time()) + time_event}'")
                        if event_data[3] > 0 and event_data[3] <= 15:
                            time_event = 480
                            await database.setMultiUserData(message.from_id, f"timeEventCollectors = '{int(time.time()) + time_event}'")
                        if event_data[3] > 15 and event_data[3] <= 25:
                            time_event = 600
                            await database.setMultiUserData(message.from_id, f"timeEventCollectors = '{int(time.time()) + time_event}'")
                        if event_data[3] > 25 and event_data[3] <= 35:
                            time_event = 900
                            await database.setMultiUserData(message.from_id, f"timeEventCollectors = '{int(time.time()) + time_event}'")
                        if event_data[3] > 35:
                            time_event = 1200
                            await database.setMultiUserData(message.from_id, f"timeEventCollectors = '{int(time.time()) + time_event}'")

                        await Menu(message, bot, api)


                    else:
                        await message.answer(
                            message=f"❌ У вас недостаточно денег для участия в мероприятии",
                        )
                        await Show(message, bot, api)
                else:
                    await message.answer(
                        message=f"❌ Участвовать на мероприятии можно с 3-его уровня",
                    )
                    await Show(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ Вы сегодня уже участвовали на мероприятии!",
                )
                await Show(message, bot, api)
    else:
        await message.answer(
            message=f"❌ В данный момент мероприятие не проводится! Приходите позже",
        )
        await Show(message, bot, api)


async def end1(message: Message, bot: Bot, api: API):
    event_data = await database.getBdData('event', 'id', "'0'")
    await database.setBdData('event', 'id', "'0'", 'playersOnline', f"'{event_data[3] - 1}'")
    await database.setUserData(message.from_id, 'state', "'collectors.Show'")
    await database.setMultiUserData(message.from_id, f"timeEventCollectors = '{int(time.time()) + 7200}'")
    await message.answer(
        message=f"❌ Вы отказались от участия в мероприятии",
    )
    await Show(message, bot, api)


async def end2(message: Message, bot: Bot, api: API):
    event_data = await database.getBdData('event', 'id', "'0'")
    await database.setBdData('event', 'id', "'0'", 'playersOnline', f"'{event_data[3] - 1}'")
    await database.setUserData(message.from_id, 'state', "'collectors.Show'")
    await database.setMultiUserData(message.from_id, f"timeEventCollectors = '{int(time.time()) + 7200}'")
    await message.answer(
        message=f"⌛ Ваше время на мероприятии истекло. Вы покинули мероприятие",
    )
    await Show(message, bot, api)


async def CheckMenu(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[50] <= int(time.time()):
        await end2(message, bot, api)
    else:
        await Menu(message, bot, api)


async def Menu(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[50] <= int(time.time()):
        await end2(message, bot, api)
    else:
        await database.setUserData(message.from_id, 'state', "'collectors.Menu'")
        event_data = await database.getBdData('event', 'id', "'0'")
        await message.answer(
            message=f"🥚 Мероприятие собиратели » ⏰ {data[50] - int(time.time())} сек.\n\n"
                    f"🥚 Доступно » {event_data[2]} яиц для сбора\n"
                    f"👥 На данном мероприятии играет » {event_data[3]} игроков",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("❌ Отказаться от мероприятия", {"cmd": "collectors.end1"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🥚 Собирать яйца", {"cmd": "collectors.collected"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🔄 Обновить информацию", {"cmd": "collectors.Menu"}), color=KeyboardButtonColor.SECONDARY)
            )
        )


async def collected(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[50] <= int(time.time()):
        await end2(message, bot, api)
    else:
        event_data = await database.getBdData('event', 'id', "'0'")
        if event_data[2] <= 0:
            await message.answer(
                message=f"🚷 В данный момент нет яиц для сбора",
            )
            await Menu(message, bot, api)
        else:
            await database.setUserData(message.from_id, 'state', "'block.Show'")
            new_eggs = event_data[2] - 1
            await database.setBdData('event', 'id', "'0'", 'count', f"'{new_eggs}'")
            await message.answer(
                message=f"🥚 Вы собираете яйцо...",
            )
            await asyncio.sleep(random.randint(3, 10))

            data = await database.getUserData(message.from_id)
            if data[50] <= int(time.time()):
                await end2(message, bot, api)
            else:
                # ----------------------------------------------------------------------

                inventory = await database.getUserData(message.from_id)
                inventory = ast.literal_eval(inventory[48])
                inventory = list(inventory)

                inventory[3] = int(inventory[3]) + 1

                await database.setUserData(message.from_id, 'inventory', f"'{inventory}'")

                # ----------------------------------------------------------------------

                await message.answer(
                    message=f"🎁 Вы получили подарок",
                )
                await CheckMenu(message, bot, api)