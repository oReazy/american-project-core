
# Казино

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'casino.Show'")
    inventory = await database.getUserData(message.from_id)
    inventory = ast.literal_eval(inventory[48])
    inventory = list(inventory)

    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🎰 Казино\n\n"
                f"🧿 У вас » {inventory[0]} фишек\n\n"
                f"🧔🏻 Сотрудник казино » Чем мы можем вам помочь?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🎲 Играть в Dice", {"cmd": "casino.Dice"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🧿 Купить фишки", {"cmd": "casino.BuyChips"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🧿 Продать фишки", {"cmd": "casino.SellChips"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def Dice(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'casino.Dice'")
    inventory = await database.getUserData(message.from_id)
    inventory = ast.literal_eval(inventory[48])
    inventory = list(inventory)

    await message.answer(
        message=f"🎲 Dice\n\n"
                f"🧿 У вас » {inventory[0]} фишек\n\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "casino.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🎲 Поставить ставку", {"cmd": "casino.DiceBet"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("ℹ Правила игры", {"cmd": "casino.DiceBetRules"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def DiceBetRules(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'casino.DiceBetRules'")
    await message.answer(
        message=f"🎲 Dice » ℹ Правила игры\n\n"
                f"В данной игре вам необходимо ставить ставку. С вероятностью 50% вы можете выиграть, однако оставшаяся 50% вы можете проиграть",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "casino.Dice"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )



async def DiceBet(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'casino.DiceBetCheck'")
    inventory = await database.getUserData(message.from_id)
    inventory = ast.literal_eval(inventory[48])
    inventory = list(inventory)
    await message.answer(
        message=f"🎲 » 🎲 Поставить ставку\n\n"
                f"🧿 У вас » {inventory[0]} фишек\n\n"
                f"📝 Выберите или напишите размер ставки",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "casino.Dice"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("1", {"cmd": "casino.DiceBetCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("5", {"cmd": "casino.DiceBetCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10", {"cmd": "casino.DiceBetCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("25", {"cmd": "casino.DiceBetCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50", {"cmd": "casino.DiceBetCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("100", {"cmd": "casino.DiceBetCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("250", {"cmd": "casino.DiceBetCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("500", {"cmd": "casino.DiceBetCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("1000", {"cmd": "casino.DiceBetCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("2500", {"cmd": "casino.DiceBetCheck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("5000", {"cmd": "casino.DiceBetCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("10000", {"cmd": "casino.DiceBetCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("25000", {"cmd": "casino.DiceBetCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("50000", {"cmd": "casino.DiceBetCheck"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("100000", {"cmd": "casino.DiceBetCheck"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def DiceBetCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    inventory = await database.getUserData(message.from_id)
    inventory = ast.literal_eval(inventory[48])
    inventory = list(inventory)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            if int(inventory[0]) >= count:
                rand = int(random.randint(0, 100))
                if rand >= 65:
                    inventory[0] = int(inventory[0]) + count
                    await database.setMultiUserData(message.from_id, f"inventory = '{inventory}'")
                    await message.answer(
                        message=f"✅ Вы выиграли и получили {count} фишек."
                    )
                    await DiceBet(message, bot, api)
                else:
                    inventory[0] = int(inventory[0]) - count
                    await database.setMultiUserData(message.from_id, f"inventory = '{inventory}'")
                    await message.answer(
                        message=f"❌ Вы проиграли {count} фишек."
                    )
                    await DiceBet(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ У вас нет столько фишек"
                )
                await DiceBet(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await DiceBet(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await DiceBet(message, bot, api)





async def BuyChips(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'casino.BuyChipsCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🎰 » 🧿 Купить фишки\n\n"
                f"🧔🏻 Сотрудник казино » Цена покупки одной фишки — 90 долларов (💵)\n\n"
                f"📝 Введите желаемое кол-во фишек",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "casino.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )



async def SellChips(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'casino.SellChipsCheck'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 » 🎰 » 🧿 Продать фишки\n\n"
                f"🧔🏻 Сотрудник казино » Цена продажи одной фишки — 80 долларов (💵)\n\n"
                f"📝 Введите желаемое кол-во фишек",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "casino.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )





async def SellChipsCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    inventory = await database.getUserData(message.from_id)
    inventory = ast.literal_eval(inventory[48])
    inventory = list(inventory)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            final_dollar = count * 80
            if int(inventory[0]) >= count:
                new_balance = int(data[12]) + final_dollar
                inventory[0] = int(inventory[0]) - int(count)
                await database.setMultiUserData(message.from_id, f"dollars = '{new_balance}', inventory = '{inventory}'")
                await message.answer(
                    message=f"✅ Вы успешно обменяли фишки казино на доллары (💵) в кол-ве {count} шт. \n"
                            f"Вы получили {await database.pretty(final_dollar)} долларов (💵)"
                    )
                await Show(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ У вас нет столько фишек"
                )
                await SellChips(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await SellChips(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await SellChips(message, bot, api)


async def BuyChipsCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if message.text.isdigit():
        count = int(message.text)
        if 0 < count:
            final_dollar = count * 90
            if data[12] >= final_dollar:

                inventory = await database.getUserData(message.from_id)
                inventory = ast.literal_eval(inventory[48])
                inventory = list(inventory)


                new_balance = int(data[12]) - final_dollar
                inventory[0] = int(inventory[0]) + int(count)
                await database.setMultiUserData(message.from_id, f"dollars = '{new_balance}', inventory = '{inventory}'")
                await message.answer(
                    message=f"✅ Вы успешно обменяли доллары на фишки казино (🧿) в кол-ве {count} шт.\n"
                            f"Вы потратили {await database.pretty(final_dollar)} долларов (💵)"
                    )
                await Show(message, bot, api)
            else:
                await message.answer(
                    message=f"❌ У вас нет столько денег на руках"
                )
                await BuyChips(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Укажите число больше 0",
            )
            await BuyChips(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Укажите число больше 0",
        )
        await BuyChips(message, bot, api)