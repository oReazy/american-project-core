
# Склад

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'warehouse.Show'")
    data = await database.getUserData(message.from_id)
    if data[27] == 'Безработный' or data[27] != 'Работник склада':
        await message.answer(
            message=f"📦 Склад\n\n"
                    f"🧑 Здраствуй, нам необходимы грузчики для того, чтобы разгрузить фуры",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.newGuysWorks"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("💼 Устроиться на работу", {"cmd": "warehouse.Getting"}), color=KeyboardButtonColor.POSITIVE)
                    .row()
                    .add(Text("📖 Информация по зарплатам", {"cmd": "warehouse.Info1"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Информация о работе", {"cmd": "warehouse.Info2"}), color=KeyboardButtonColor.SECONDARY)
            )
        )
    else:
        await message.answer(
            message=f"📦 Склад\n\n"
                    f"🧑 Здраствуй, {data[3]}. Приехали новые фуры с грузом. Их необходимо разгрузить.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.newGuysWorks"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("⚒ Работать", {"cmd": "warehouse.rab1_1"}), color=KeyboardButtonColor.POSITIVE)
                    .row()
                    .add(Text("💼 Уволиться", {"cmd": "warehouse.Leave"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Информация по зарплатам", {"cmd": "warehouse.Info1"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Информация о работе", {"cmd": "warehouse.Info2"}), color=KeyboardButtonColor.SECONDARY)
            )
        )


async def Getting(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'work', "'Работник склада'")
    await message.answer(
        message=f"✅ Вы успешно устроились на склад"
        )
    await Show(message, bot, api)


async def Leave(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'work', "'Безработный'")
    await message.answer(
        message=f"✅ Вы успешно уволились с работы"
        )
    await Show(message, bot, api)


async def Info1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'warehouse.Info1'")
    await message.answer(
        message=f"📦 » 📖 Информация по зарплатам\n\n"
                f"📦 За один перенесенный мешок вам заплатят » 25 долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "warehouse.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )



async def Info2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'warehouse.Info2'")
    await message.answer(
        message=f"📦 » 📖 Информация о работе\n\n"
                f"На складе вы будете работать грузчиком. Вашей основной задачей является перенос "
                f"мешков из фур на склад. За каждый перенесенный мешок вам дают зарплату",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "warehouse.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )

# ---------------------------------------------------------------------------------------------------------



async def rab1_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_1'")
    await database.setUserData(message.from_id, 'temporary_var', f"'0'")
    await message.answer(
        message=f"🚶🏼 Зайдите в раздевалку и оденьте рабочую одежду",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶🏼 Зайти в раздевалку", {"cmd": "warehouse.rab1_2"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🚶🏼 Вы заходите в раздевалку...')
    await asyncio.sleep(4)
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_2'")
    await message.answer(
        message=f"🦺 Оденьте рабочую одежду",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🦺 Одеть рабочую одежду", {"cmd": "warehouse.rab1_3"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🦺 Вы одеваете рабочую одежду...')
    await asyncio.sleep(6)
    await message.answer('🦺 Вы одели рабочую одежду')
    await asyncio.sleep(1)
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_3'")
    await message.answer(
        message=f"❓ Готовы ли вы к смене?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Выйти на смену", {"cmd": "warehouse.rab1_4"}), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("❌ Закончить работу", {"cmd": "warehouse.rab1_end1_1"}), color=KeyboardButtonColor.SECONDARY)
            )
        )



async def rab1_4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🚶🏻 Вы выходите на смену...')
    await asyncio.sleep(5)
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_4'")
    await message.answer(
        message=f"🧑 Главный грузчик » Привет. У нас есть множество фур, которые необходимо разгрузить.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💬 Хорошо", {"cmd": "warehouse.rab1_4_1"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💬 Окей", {"cmd": "warehouse.rab1_4_1"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💬 За работу!", {"cmd": "warehouse.rab1_4_2"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💬 Груз тяжелый?", {"cmd": "warehouse.rab1_4_3"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("❌ Закончить работу", {"cmd": "warehouse.rab1_end2_1"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_4_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_4_1'")
    await message.answer(
        message=f"🧑 Главный грузчик » Помни, что твоя зарплата зависит от количество перенесенных мешков!\n\n"
                f"Ладно, не буду отвлекать, иди разгружай фуры.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶🏻 Подойти к фуре", {"cmd": "warehouse.rab1_5"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_4_2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_4_2'")
    await message.answer(
        message=f"🧑 Главный грузчик » Мне нравится твой боевой настрой! Надеюсь, что ты сегодня побьешь рекорд по переносу мешков.\n\n"
                f"Ладно, за работу, так за работу. Не буду отвлекать",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶🏻 Подойти к фуре", {"cmd": "warehouse.rab1_5"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_4_3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_4_3'")
    await message.answer(
        message=f"🧑 Главный грузчик » В целом каждый мешок весит по 20 кг.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💬 Хорошо", {"cmd": "warehouse.rab1_4_1"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💬 Окей", {"cmd": "warehouse.rab1_4_1"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💬 За работу!", {"cmd": "warehouse.rab1_4_2"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("❌ Закончить работу", {"cmd": "warehouse.rab1_end2_1"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🚶🏻 Вы подходите к фуре...')
    await asyncio.sleep(5)
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_5'")
    await message.answer(
        message=f"📦 Вы подошли к фуре. Возьмите мешок и перенесите к складу",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("📦 Взять мешок", {"cmd": "warehouse.rab1_6"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_6(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_6'")
    await message.answer(
        message=f"📦 Вы взяли мешок. Несите его на склад",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("📦 Нести мешок на склад", {"cmd": "warehouse.rab1_7"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_7(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('📦 Вы несете мешок на склад...')
    await asyncio.sleep(5)
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_7'")
    await message.answer(
        message=f"📦 Вы принесли мешок на склад. Положите его.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("📦 Положить мешок", {"cmd": "warehouse.rab1_8"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_8(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"📦 Вы положили мешок",
    )
    await rab1_9(message, bot, api)


async def rab1_9(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    new_data = int(data[44]) + 1
    await database.setMultiUserData(message.from_id, f"temporary_var = '{new_data}'")

    if (new_data % 5) == 0:
        await rab1_10(message, bot, api)
    else:
        await rab1_11(message, bot, api)


async def rab1_10(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_10'")
    await message.answer(
        message=f"❓ Желаете ли вы продолжить работу?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Продолжить", {"cmd": "warehouse.rab1_11"}), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("❌ Закончить работу", {"cmd": "warehouse.rab1_end3_1"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_11(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_11'")
    await message.answer(
        message=f"🚶🏻 Идите обратно к фуре, чтобы получить новый мешок",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶🏻 Подойти к фуре", {"cmd": "warehouse.rab1_5"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_end1_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_end1_1'")
    await message.answer(
        message=f"🦺 Вы решили закончить работу. Для того, чтобы завершить работу, вам необходимо снять с себя рабочую одежду",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🦺 Снять рабочую одежду", {"cmd": "warehouse.rab1_end1_2"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_end1_2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🦺 Вы снимаете рабочую одежду...')
    await asyncio.sleep(8)
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_end1_2'")
    await message.answer(
        message=f"🦺 Вы сняли рабочую одежду и оставили ее в шкафчике"
    )
    await Show(message, bot, api)



async def rab1_end2_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_end2_1'")
    await message.answer(
        message=f"🧑 Главный грузчик » Ты же даже не начал работать! Какие-то более важные дела появились? Ладно, не буду отвлекать. Нужны будут деньги, приходи к нам на склад.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💬 Хорошо", {"cmd": "warehouse.rab1_end1_1"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💬 Учту", {"cmd": "warehouse.rab1_end1_1"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_end3_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_end3_1'")
    await message.answer(
        message=f"🚶🏻 Вы решили закончить работу. Для того, чтобы закончить работу, зайдите в раздевалку и переоденьтесь",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶🏻 Идти в раздевалку", {"cmd": "warehouse.rab1_end3_2"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_end3_2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🚶🏻 Вы идете в раздевалку')
    await asyncio.sleep(7)
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_end3_2'")
    await message.answer(
        message=f"🦺 Снимите с себя рабочую одежду и оденьте ту, в которой вы пришли на работу.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🦺 Снять рабочую одежду", {"cmd": "warehouse.rab1_end3_3"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_end3_3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🦺 Вы сняли рабочую одежду')
    await asyncio.sleep(3)
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_end3_3'")
    await message.answer(
        message=f"👕 Оденьте свою одежду",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👕 Одеть свою одежду", {"cmd": "warehouse.rab1_end3_4"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_end3_4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('👕 Вы одеваете свою одежду...')
    await asyncio.sleep(3)
    await database.setUserData(message.from_id, 'state', "'warehouse.rab1_end3_4'")
    await message.answer(
        message=f"🚶🏻 Подойдите в кабинет главного грузчика, чтобы получить оплату за свой труд",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶🏻 Зайти в кабинет", {"cmd": "warehouse.rab1_end3_5"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_end3_5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🚶🏻 Вы заходите в кабинет главного грузчика')
    await asyncio.sleep(3)
    await database.setUserData(message.from_id, 'state', "'warehouse.Show'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    zarplata = int(data[44]) * 25 * server_settings[26]
    itog = int(data[12]) + zarplata
    await database.setUserData(message.from_id, 'dollars', f"'{itog}'")
    await message.answer(
        message=f"🧑 Главный грузчик » {data[3]} хей! Отлично поработал. Я рад, что у нас работают такие люди как ты.Смотри, ты перенес {data[44]} мешков и получаешь за это {zarplata} долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💵 Забрать деньги", {"cmd": "warehouse.Show"}), color=KeyboardButtonColor.SECONDARY)
        )
    )