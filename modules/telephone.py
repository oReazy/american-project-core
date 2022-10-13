
# Телефон

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database, mainMenu

# ----------------------------------------------------------------------------------------------------------------------

async def Check(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[5] == '❌ Отсутствует':
        await message.answer(
            message=f"❌ У вас нет мобильного телефона. Купить вы его можете в магазине электроники",
        )
        await mainMenu.Show(message, bot, api)
    else:
        await Show(message, bot, api)



async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"📱 Вы достали телефон из кармана"
    )
    await asyncio.sleep(2)
    await message.answer(
        message=f"📱 Вы включили телефон"
    )
    await asyncio.sleep(2)
    await ShowMenu(message, bot, api)



async def PowerOff(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"📱 Вы выключили телефон"
    )
    await asyncio.sleep(2)
    await message.answer(
        message=f"📱 Вы убрали телефон в карман"
    )
    await asyncio.sleep(2)
    await mainMenu.Show(message, bot, api)




async def ShowMenu(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'telephone.ShowMenu'")
    data = await database.getUserData(message.from_id)
    if data[5] not in ['iPhone 13', 'iPhone 12', 'iPhone 11', 'SAMSUNG Galaxy S21', 'SAMSUNG Galaxy A72', 'SAMSUNG Galaxy S20', 'Xiaomi Mi 11 Lite', 'Xiaomi Redmi Note 10 Pro', 'Xiaomi Redmi Note 8 Pro']:
        await message.answer(
            message=f"🎯 » 📱 Телефон",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("🔴 Выключить телефон", {"cmd": "telephone.PowerOff"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("⏰ Служба точного времени", {"cmd": "telephone.Time"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📌 Заметки", {"cmd": "telephone.notes"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🌎 Forbes", {"cmd": "telephone.Forbes"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📇 Объявления", {"cmd": "telephone.Advert"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    else:
        await message.answer(
            message=f"🎯 » 📱 Телефон",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("🔴 Выключить телефон", {"cmd": "telephone.PowerOff"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("⏰ Служба точного времени", {"cmd": "telephone.Time"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("📌 Заметки", {"cmd": "telephone.notes"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("💱 Курс валют", {"cmd": "telephone.CourceVallet"}), color=KeyboardButtonColor.SECONDARY)
                    .add(Text("🌎 Forbes", {"cmd": "telephone.Forbes"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📇 Объявления", {"cmd": "telephone.Advert"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )



async def Advert(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'telephone.Advert'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    data = ast.literal_eval(server_settings[27])
    data = list(data)
    spisok = ''
    data.reverse()
    if len(data) != 0:
        for row in data:
            data_user = await database.getUserData(row[1])
            data_user2 = await database.getUserData(row[2])
            if row[3] == '📄 Стандартное объявление':
                spisok = f'{spisok}\n{row[0]}.\n💬 Связаться » @id{row[1]}({data_user[3]})\n✏ Объявление отредактировал » @id{row[2]}({data_user2[3]})\n\n'
            if row[3] == '👑 VIP объявление':
                spisok = f'{spisok}\n👑 VIP ОБЪЯВЛЕНИЕ\n{row[0]}.\n💬 Связаться » @id{row[1]}({data_user[3]})\n✏ Объявление отредактировал » @id{row[2]}({data_user2[3]})\n\n'
    else:
        spisok = '❌ Объявления отсутствуют'

    await message.answer(
        message=f"📇 Объявления со всего штата\n\n"
                f"{spisok}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("❌ Закрыть приложение", {"cmd": "telephone.ShowMenu"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("➕ Добавить объявление", {"cmd": "telephone.AdvertEdit"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🔁 Обновить", {"cmd": "telephone.Advert"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def AdvertEdit(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'telephone.AdvertEdit'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    data = ast.literal_eval(server_settings[28])
    data = list(data)
    for row in data:
        if row[1] == message.from_id:
            await message.answer(
                message=f"❌ Ошибка. Вы недавно уже отправляли объявление, дождитесь его публикации",
            )
            await Advert(message, bot, api)
            return

    await message.answer(
        message=f"Вы можете подать объявление двух типов:\n\n"
                f"📄 Стандартное объявление » Стоимость отправки 1 000 долларов (💵)\n"
                f"👑 VIP объявление » Стоимость отправки 25 000 долларов (💵)\n\n"
                f"⤵ Выберите тип объявления",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("❌ Закрыть приложение", {"cmd": "telephone.ShowMenu"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📄 Стандартное объявление", {"cmd": "telephone.AdvertEdit2"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("👑 VIP объявление", {"cmd": "telephone.AdvertEdit2"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def AdvertEdit2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'telephone.AdvertEditCheck'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    data_user = await database.getUserData(message.from_id)

    if message.text == '📄 Стандартное объявление':
        if data_user[12] >= 1000:
            await database.setUserData(message.from_id, 'temporary_var', "'📄 Стандартное объявление'")
            await database.setUserData(message.from_id, 'dollars', f"'{data_user[12] - 1000}'")
        else:
            await message.answer('❌ Ошибка. У вас недостаточно денег на руках, чтобы отправить данное объявление')
            await AdvertEdit(message, bot, api)
            return
    if message.text == '👑 VIP объявление':
        if data_user[12] >= 25000:
            await database.setUserData(message.from_id, 'temporary_var', "'👑 VIP объявление'")
            await database.setUserData(message.from_id, 'dollars', f"'{data_user[12] - 25000}'")
        else:
            await message.answer('❌ Ошибка. У вас недостаточно денег на руках, чтобы отправить данное объявление')
            await AdvertEdit(message, bot, api)
            return

    await message.answer(
        message=f"✏ Напишите объявление, которое хотите отправить (до 120 букв)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("❌ Закрыть приложение", {"cmd": "telephone.ShowMenu"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def AdvertEditCheck(message: Message, bot: Bot, api: API):
    if len(message.text) <= 120:
        server_settings = await database.getBdData('settings', 'id', "'1'")
        text = message.text.replace("\n", "")
        text = text.replace("\r", "")
        data_user = await database.getUserData(message.from_id)
        new_data = [text, message.from_id, 'no edit', data_user[44]]
        data = ast.literal_eval(server_settings[28])
        data = list(data)


        data.append(new_data)
        await database.setBdData('settings', 'id', "'1'", 'advert_edit', f'\"{data}\"')
        await message.answer(
            message=f"✅ Вы успешно отправили свое объявление. Перед публикацией объявления, редакция проверит и откорректирует его. В случае, если объявление будет отклонено, деньги за объявление вернуться.",
        )
        await Advert(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Ошибка. Текст вашей заметки превышает норму на {len(message.text)-120} символов",
        )
        await Advert(message, bot, api)











async def notes(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'telephone.notes'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"📌 Заметки\n\nЭто лучшее приложение для мобильного телефона, которое позволяет оставлять заметки.\n\n"
                f"Твои заметки » {data[51]}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("❌ Закрыть приложение", {"cmd": "telephone.ShowMenu"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("✏ Изменить текст заметки", {"cmd": "telephone.notesEdit"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def notesEdit(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'telephone.notesEditCheck'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"✏ Напишите новый текст для вашей заметки (до 500 букв)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("❌ Закрыть приложение", {"cmd": "telephone.ShowMenu"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def notesEditCheck(message: Message, bot: Bot, api: API):
    if len(message.text) <= 500:
        await database.setUserData(message.from_id, 'notes_telephone', f"'{message.text}'")
        await message.answer(
            message=f"✅ Вы успешно изменили текст заметки",
        )
        await notes(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Ошибка. Текст вашей заметки превышает норму на {len(message.text)-500} символов",
        )
        await notes(message, bot, api)



async def ForbesMoney(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'telephone.ForbesLVL'")
    TOP_MONEY = await database.yourSQL('SELECT * FROM `users` ORDER BY `dollars` DESC LIMIT 20;')
    spisok = ''
    count = 1
    for row in TOP_MONEY:
        spisok = f'{spisok}\n{count}. 👤 @id{row[1]}({row[3]}) — {row[12]} долларов (💵)'
        count = count + 1
    await message.answer(
        message=f"🌎 » 💵 Самые богатые игроки (показаны 20 человек по долларам)\n\n{spisok}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("❌ Закрыть приложение", {"cmd": "telephone.ShowMenu"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("◀ Назад", {"cmd": "telephone.Forbes"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def ForbesLVL(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'telephone.ForbesLVL'")
    TOP_LVL = await database.yourSQL('SELECT * FROM `users` ORDER BY `lvl` DESC LIMIT 20;')
    spisok = ''
    count = 1
    for row in TOP_LVL:
        spisok = f'{spisok}\n{count}. 👤 @id{row[1]}({row[3]}) — {row[6]} уровень'
        count = count + 1
    await message.answer(
        message=f"🌎 » 🧔 Самые старые игроки (показаны 20 человек)\n\n{spisok}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("❌ Закрыть приложение", {"cmd": "telephone.ShowMenu"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("◀ Назад", {"cmd": "telephone.Forbes"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def Forbes(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'telephone.Forbes'")
    await message.answer(
        message=f"🌎 Forbes — главное о миллиардерах, бизнесе и финансах\n\n"
                f"⤵ Выберите рейтинг",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("❌ Закрыть приложение", {"cmd": "telephone.ShowMenu"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🧔 Самые старые игроки", {"cmd": "telephone.ForbesLVL"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💵 Самые богатые игроки", {"cmd": "telephone.ForbesMoney"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def CourceValletDollars(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'telephone.CourceValletDollars'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    data = ast.literal_eval(server_settings[16])
    data = list(data)
    await message.answer(
        message=f"💱 » 💵 Доллары\n\n"
                f"⚠ Вы просматриваете обмен с долларов на другие валюты.\n\n"
                f"1 доллар (💵) = {data[0]} евро (💶)\n"
                f"1 доллар (💵) = {data[1]} иен (💴)\n"
                f"1 доллар (💵) = {data[2]} фунтов (💷)\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("❌ Закрыть приложение", {"cmd": "telephone.ShowMenu"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("◀ Назад", {"cmd": "telephone.CourceVallet"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def CourceValletEuro(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'telephone.CourceValletEuro'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    data = ast.literal_eval(server_settings[16])
    data = list(data)
    await message.answer(
        message=f"💱 » 💶 Евро\n\n"
                f"⚠ Вы просматриваете обмен с евро на другие валюты.\n\n"
                f"1 евро (💶) = {data[3]} доллары (💵)\n"
                f"1 евро (💶) = {data[4]} иен (💴)\n"
                f"1 евро (💶) = {data[5]} фунтов (💷)\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("❌ Закрыть приложение", {"cmd": "telephone.ShowMenu"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("◀ Назад", {"cmd": "telephone.CourceVallet"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def CourceValletYen(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'telephone.CourceValletYen'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    data = ast.literal_eval(server_settings[16])
    data = list(data)
    await message.answer(
        message=f"💱 » 💴 Иены\n\n"
                f"⚠ Вы просматриваете обмен с иены на другие валюты.\n\n"
                f"1 иена (💴) = {data[6]} доллары (💵)\n"
                f"1 иена (💴) = {data[7]} евро (💶)\n"
                f"1 иена (💴) = {data[8]} фунтов (💷)\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("❌ Закрыть приложение", {"cmd": "telephone.ShowMenu"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("◀ Назад", {"cmd": "telephone.CourceVallet"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def CourceValletPounds(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'telephone.CourceValletPounds'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    data = ast.literal_eval(server_settings[16])
    data = list(data)
    await message.answer(
        message=f"💱 » 💷 Фунты\n\n"
                f"⚠ Вы просматриваете обмен с иены на другие валюты.\n\n"
                f"1 фунт (💷) = {data[9]} доллары (💵)\n"
                f"1 фунт (💷) = {data[10]} евро (💶)\n"
                f"1 фунт (💷) = {data[11]} иен (💴)\n",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("❌ Закрыть приложение", {"cmd": "telephone.ShowMenu"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("◀ Назад", {"cmd": "telephone.CourceVallet"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def CourceVallet(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'telephone.CourceVallet'")
    await message.answer(
        message=f"💱 Курс валют\n\n"
                f"⤵ Выберите валюту на которую хотите посмотреть курс",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("❌ Закрыть приложение", {"cmd": "telephone.ShowMenu"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💵 Доллары", {"cmd": "telephone.CourceValletDollars"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💶 Евро", {"cmd": "telephone.CourceValletEuro"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💴 Иены", {"cmd": "telephone.CourceValletYen"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("💷 Фунты", {"cmd": "telephone.CourceValletPounds"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def Time(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'telephone.Time'")
    real_time = datetime.datetime.now()
    if 0 <= real_time.minute < 10:
        minute = f'0{real_time.minute}'
    else:
        minute = real_time.minute
    if 0 <= real_time.second < 10:
        second = f'0{real_time.second}'
    else:
        second = real_time.second
    real_day = datetime.date.today()
    await message.answer(
        message=f"⏰ Служба точного времени — на страже ваших секунд\n\n"
                f"⏰ Точное время: {real_time.hour}:{minute}:{second}\n"
                f"📅 Сегодня: {real_day.day}.{real_day.month}.{real_day.year}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("❌ Закрыть приложение", {"cmd": "telephone.ShowMenu"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🔄 Обновить", {"cmd": "telephone.Time"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )