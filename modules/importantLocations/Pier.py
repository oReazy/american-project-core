
# Пирс

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'Pier.Show'")
    if 0 <= int(datetime.datetime.now().hour) <= 5:
        await message.answer(
            message=f"🎯 » 🗺 » 🏛 » 🌅 Пирс\n\n"
                    f"🌙 Яркая, белая луна. Небо чистое без облаков",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("👨🏻‍🦳 Эдвард (обмен подарков)", {"cmd": "Pier.Obmen"}),
                         color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🔎 Найти семью", {"cmd": "Pier.FindFamily"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    elif 6 <= int(datetime.datetime.now().hour) <= 10:
        await message.answer(
            message=f"🎯 » 🗺 » 🏛 » 🌅 Пирс\n\n"
                    f"🌤 Небольшая облачность, солнце встает",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("👨🏻‍🦳 Эдвард (обмен подарков)", {"cmd": "Pier.Obmen"}),
                         color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🔎 Найти семью", {"cmd": "Pier.FindFamily"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    elif 10 <= int(datetime.datetime.now().hour) <= 15:
        await message.answer(
            message=f"🎯 » 🗺 » 🏛 » 🌅 Пирс\n\n"
                    f"☀ Яркое солнце, ясная погода",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("👨🏻‍🦳 Эдвард (обмен подарков)", {"cmd": "Pier.Obmen"}),
                         color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🔎 Найти семью", {"cmd": "Pier.FindFamily"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    elif 15 <= int(datetime.datetime.now().hour) <= 20:
        await message.answer(
            message=f"🎯 » 🗺 » 🏛 » 🌅 Пирс\n\n"
                    f"🌆 Закат",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("👨🏻‍🦳 Эдвард (обмен подарков)", {"cmd": "Pier.Obmen"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🔎 Найти семью", {"cmd": "Pier.FindFamily"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    elif 20 <= int(datetime.datetime.now().hour) <= 24:
        await message.answer(
            message=f"🎯 » 🗺 » 🏛 » 🌅 Пирс\n\n"
                    f"⛅ Небольшая облачность, солнце потихоньку опускается",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("👨🏻‍🦳 Эдвард (обмен подарков)", {"cmd": "Pier.Obmen"}),
                         color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🔎 Найти семью", {"cmd": "Pier.FindFamily"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )



async def FindFamily(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'Pier.FindFamily'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🌅 » 🔎 Найти семью\n\n"
                f"ℹ Напишите основателю или заместителю семьи о том, что вы готовы принять приглашение в семью.\n\n"
                f"ℹ Для того, чтобы перестать искать семью, нажмите на кнопку\n\n"
                f"⚠ В РАЗРАБОТКЕ",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "Pier.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )


async def Obmen(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'Pier.Obmen'")
    await message.answer(
        message=f"👨🏻‍🦳 Эдвард » Привет, хочешь обменять свои накопленные подарочки?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "Pier.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🎁 Обменять подарки", {"cmd": "Pier.ObmenCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("ℹ Что я могу получить?", {"cmd": "Pier.ObmenInfo1"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def ObmenCheck(message: Message, bot: Bot, api: API):
    inventory = await database.getUserData(message.from_id)
    inventory = ast.literal_eval(inventory[48])
    inventory = list(inventory)

    if int(inventory[3]) >= 20:
        inventory[3] = int(inventory[3]) - 20


        await database.setUserData(message.from_id, 'inventory', f"'{inventory}'")


        prize = [0,0,1,1,1,1,2,2,2,2,2,2,3,3,3,4,4,5,5,5,6,6,7,8,8,8,8,9,9]
        randPrize = random.randint(0, len(prize)-1)
        if prize[randPrize] == 0:
            await message.answer(
                message=f"👨🏻‍🦳 Эдвард » Получить половину подарков приятнее, чем ничего.\n\n"
                        f"🎁 Вы получили 10 подарков",
            )
            inventory = await database.getUserData(message.from_id)
            inventory = ast.literal_eval(inventory[48])
            inventory = list(inventory)

            inventory[3] = int(inventory[3]) + 10
            await database.setUserData(message.from_id, 'inventory', f"'{inventory}'")
            await Obmen(message, bot, api)
        elif prize[randPrize] == 1:
            await message.answer(
                message=f"👨🏻‍🦳 Эдвард » Давай еще раз\n\n"
                        f"🎁 Вы получили 20 подарков",
            )
            inventory = await database.getUserData(message.from_id)
            inventory = ast.literal_eval(inventory[48])
            inventory = list(inventory)

            inventory[3] = int(inventory[3]) + 20

            inventory = str(inventory)
            inventory = inventory.replace("'", "")
            await database.setUserData(message.from_id, 'inventory', f"'{inventory}'")
            await Obmen(message, bot, api)

        elif prize[randPrize] == 2:
            await message.answer(
                message=f"👨🏻‍🦳 Эдвард » Держи свою пятеру\n\n"
                        f"💵 Вы получили 5 000 долларов",
            )
            data = await database.getUserData(message.from_id)
            new_balance = int(data[12]) + 5000
            await database.setUserData(message.from_id, "dollars", f"'{new_balance}'")
            await Obmen(message, bot, api)
        elif prize[randPrize] == 3:
            await message.answer(
                message=f"👨🏻‍🦳 Эдвард » Держи свою десятку\n\n"
                        f"💵 Вы получили 10 000 долларов",
            )
            data = await database.getUserData(message.from_id)
            new_balance = int(data[12]) + 10000
            await database.setUserData(message.from_id, "dollars", f"'{new_balance}'")
            await Obmen(message, bot, api)
        elif prize[randPrize] == 4:
            await message.answer(
                message=f"👨🏻‍🦳 Эдвард » Держи свою двадцатку\n\n"
                        f"💵 Вы получили 20 000 долларов",
            )
            data = await database.getUserData(message.from_id)
            new_balance = int(data[12]) + 20000
            await database.setUserData(message.from_id, "dollars", f"'{new_balance}'")
            await Obmen(message, bot, api)
        elif prize[randPrize] == 5:
            await message.answer(
                message=f"👨🏻‍🦳 Эдвард » Поздравляю ковбой!\n\n"
                        f"🥉 Вы получили 1 бронзовую рулетку",
            )
            inventory = await database.getUserData(message.from_id)
            inventory = ast.literal_eval(inventory[48])
            inventory = list(inventory)

            inventory[4] = int(inventory[4]) + 1
            await database.setUserData(message.from_id, 'inventory', f"'{inventory}'")
            await Obmen(message, bot, api)
        elif prize[randPrize] == 6:
            await message.answer(
                message=f"👨🏻‍🦳 Эдвард » Отличный приз, серебряная рулетка!\n\n"
                        f"🥈 Вы получили 1 серебряную рулетку",
            )
            inventory = await database.getUserData(message.from_id)
            inventory = ast.literal_eval(inventory[48])
            inventory = list(inventory)

            inventory[5] = int(inventory[5]) + 1
            await database.setUserData(message.from_id, 'inventory', f"'{inventory}'")
            await Obmen(message, bot, api)
        elif prize[randPrize] == 7:
            await message.answer(
                message=f"👨🏻‍🦳 Эдвард » Ты нашел золото!\n\n"
                        f"🥇 Вы получили 1 золотую рулетку",
            )
            inventory = await database.getUserData(message.from_id)
            inventory = ast.literal_eval(inventory[48])
            inventory = list(inventory)

            inventory[6] = int(inventory[6]) + 1
            await database.setUserData(message.from_id, 'inventory', f"'{inventory}'")
            await Obmen(message, bot, api)
        elif prize[randPrize] == 8:
            DonateList = [10,10,10,15,15,15,20,25,25,25,25,25,30,30,30,30,30,40,40,40,40,40,50,60,70,80,90,100,125,150,175,200,250,300,350,400,500]
            randDonate = random.randint(0,len(DonateList)-1)
            if 0 <= DonateList[randDonate] <= 99:
                await message.answer(
                    message=f"👨🏻‍🦳 Эдвард » Ты нашел настояющую жилу!\n\n"
                            f"💎 Вы получили {DonateList[randDonate]} доната.\n\n"
                            f"👉 Перекинь это сообщение, чтобы твои друзья завидовали твоей удаче",
                )
            if 100 <= DonateList[randDonate] <= 299:
                await message.answer(
                    message=f"👨🏻‍🦳 Эдвард » Ты нашел клад!\n\n"
                            f"💎 Вы получили {DonateList[randDonate]} доната.\n\n"
                            f"👉 Перекинь это сообщение, чтобы твои друзья завидовали твоей удаче",
                )
            if 300 <= DonateList[randDonate] <= 499:
                await message.answer(
                    message=f"👨🏻‍🦳 Эдвард » Тебе очень повезло!\n\n"
                            f"💎 Вы получили {DonateList[randDonate]} доната.\n\n"
                            f"👉 Перекинь это сообщение, чтобы твои друзья завидовали твоей удаче",
                )
            if 500 <= DonateList[randDonate] <= 5000:
                await message.answer(
                    message=f"👨🏻‍🦳 Эдвард » Ты сорвал куш! Ты выиграл 500 доната!\n\n"
                            f"💎 Вы получили {DonateList[randDonate]} доната.\n\n"
                            f"👉 Перекинь это сообщение, чтобы твои друзья завидовали твоей удаче",
                )
            data = await database.getUserData(message.from_id)
            new_balance = int(data[20]) + DonateList[randDonate]
            await database.setUserData(message.from_id, "donate", f"'{new_balance}'")
            await Obmen(message, bot, api)
        elif prize[randPrize] == 9:
            await message.answer(
                message=f"👨🏻‍🦳 Эдвард » Я хотел подарить тебе улучшение, но у тебя оно уже есть\n\n"
                        f"💵 Вам вернули 20 подарков",
            )
            inventory = await database.getUserData(message.from_id)
            inventory = ast.literal_eval(inventory[48])
            inventory = list(inventory)

            inventory[3] = int(inventory[3]) + 20
            await database.setUserData(message.from_id, 'inventory', f"'{inventory}'")
            await Obmen(message, bot, api)
    else:
        await message.answer(
            message=f"❌ У вас нет 20-ти подарков для обмена",
        )
        await Obmen(message, bot, api)





async def ObmenInfo1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'Pier.Show'")
    await message.answer(
        message=f"👨🏻‍🦳 Эдвард » После обмена 20-ти подарков, ты можешь получить один из этих призов:\n"
                f"— Подарки (5 шт.)\n"
                f"— Подарки (10 шт.)\n"
                f"— Доллары (5 000)\n"
                f"— Доллары (10 000)\n"
                f"— Доллары (20 000)\n"
                f"— Бронзовая рулетка\n"
                f"— Серебряная рулетка\n"
                f"— Золотая рулетка\n"
                f"— Донат (от 10 до 500)\n"
                f"— Прочие улучшения для вашего персонажа",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "Pier.Obmen"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )