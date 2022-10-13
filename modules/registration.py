
# Регистрация игрока на проекте

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

# Первый этап регистрации. Тут происходит проверка на открыта ли регистрация на сервере или нет.
# Выводится информация о просьбе ввести ник

async def registration_1(message: Message, bot: Bot, api: API):
    DATA_SETTINGS = await database.getBdData('settings', 'id', "'1'")
    if DATA_SETTINGS[5] == 1:
        if await database.findBaseData("vk_id", f"{message.from_id}") == 0:
            await database.registerNewAccaunt(message.from_id)
        await database.setUserData(message.from_id, 'state', "'registration.registration_1_check'")
        await message.answer(
            message=f"👋🏻 Добро пожаловать на проект @{DATA_SETTINGS[3]}({DATA_SETTINGS[1]}) на сервер @{DATA_SETTINGS[4]}({DATA_SETTINGS[2]})\n\n"
                    f"❌ Ваш аккаунт не зарегистрирован на данном сервере.\n"
                    f"📝 Придумайте ник вашего персонажа (от 3 до 15 символов)"
        )
    else:
        await message.answer(
            message=f"❌ Регистрация на данном сервере закрыта",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("🔄 Обновить", {"cmd": "registration.registration_1"}),
                         color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )

# ----------------------------------------------------------------------------------------------------------------------

# Проверка ника на наличие в базе данных и по условиям
async def registration_1_check(message: Message, bot: Bot, api: API):
    if 3 <= len(message.text) <= 15:
        text = message.text.replace("\n", "")
        text = text.replace("\r", "")
        if await database.findBaseData('nick', f"'{message.text}'") == 0:
            await database.setUserData(message.from_id, 'state', "'registration.registration_2'")
            await database.setUserData(message.from_id, 'nick', f"'{text}'")
            await registration_2(message, bot, api)
        else:
            await message.answer(
                message='❌ Ошибка. Данный ник уже занят. Попробуйте другой'
            )
            await registration_1(message, bot, api)
    else:
        await message.answer(
            message=f'❌ Ошибка. Вы ввели либо короткий ник, либо слишком длинный.'
        )
        await registration_1(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Выбор пола персонажа
async def registration_2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'registration.registration_2'")
    await message.answer(
        message=f"🚻 Выберите пол вашего персонажа\n\n"
                f"⤵ Для выбора нажмите на одну из кнопок ниже",
        keyboard=(
            Keyboard(one_time=True, inline=False)
            .add(Text("👨 Мужчина", {"cmd": "registration.registration_2_man"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("👩 Девушка", {"cmd": "registration.registration_2_woman"}), color=KeyboardButtonColor.SECONDARY)
            .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Выбор пола персонажа
async def registration_2_man(message: Message, bot: Bot, api: API):
    await database.setMultiUserData(message.from_id, "sex = 'Мужчина', state = 'registration.registration_3'")
    await registration_3(message, bot, api)

# Выбор пола персонажа
async def registration_2_woman(message: Message, bot: Bot, api: API):
    await database.setMultiUserData(message.from_id, "sex = 'Женщина', state = 'registration.registration_3'")
    await registration_3(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Выбор национальности персонажа
async def registration_3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'registration.registration_3'")
    await message.answer(
        message=f"⤵️ Выберите национальность вашему персонажу",
        keyboard=(
            Keyboard(one_time=True, inline=False)
            .add(Text("Американец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Канадец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Итальянец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text("Ирландец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Китаец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Японец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text("Русский", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Украинец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Серб", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text("Вьетнамец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Гаитянин", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Араб", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text("Еврей", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .add(Text("Афроамериканец", {"cmd": "registration.registration_3_check"}), color=KeyboardButtonColor.SECONDARY)
            .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Запись национальности в базу данных
async def registration_3_check(message: Message, bot: Bot, api: API):
    await database.setMultiUserData(message.from_id, f"nationality = '{message.text}', state = 'registration.registration_4'")
    await registration_4(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Просьба ввести возраст персонажа
async def registration_4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'registration.registration_4_check'")
    await message.answer(
        message=f"📝 Введите возраст персонажа (от 18 до 70 лет)"
    )

# ----------------------------------------------------------------------------------------------------------------------

# Проверка вводимых данных от пользователя
async def registration_4_check(message: Message, bot: Bot, api: API):
    if message.text.isdigit():
        age = int(message.text)
        if 18 <= age <= 70:
            await database.setMultiUserData(message.from_id, f"age = '{age}', state = 'registration.registration_5'")
            await registration_5(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Введите возраст в пределах от 18 до 70"
            )
            await registration_4(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Введите возраст цифрами"
        )
        await registration_4(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Выбор откуда вы узнали о нашем проекте
async def registration_5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'registration.registration_5'")
    await message.answer(
        message=f"🏃 Откуда вы узнали о нашем сервере?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
            .add(Text("👥 Узнал от друзей", {"cmd": "registration.registration_5_friend"}), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text("📄 Узнал из списка чат-ботов", {"cmd": "registration.registration_5_list_chatbot"}), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text("🔎 Узнал из поисковой системы", {"cmd": "registration.registration_5_search"}), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text("📺 Узнал от ютубера", {"cmd": "registration.registration_5_youtube"}), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text("🔘 Другое", {"cmd": "registration.registration_5_other"}), color=KeyboardButtonColor.SECONDARY)
            .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Варианты ответов на вопрос
async def registration_5_friend(message: Message, bot: Bot, api: API):
    DATA_SETTINGS = await database.getBdData('settings', 'id', '1')
    update = DATA_SETTINGS[9] + 1
    await database.setBdData('settings', 'id', "'1'", 'statistics_friend', f"'{update}'")
    await registration_6(message, bot, api)



async def registration_5_list_chatbot(message: Message, bot: Bot, api: API):
    DATA_SETTINGS = await database.getBdData('settings', 'id', '1')
    update = DATA_SETTINGS[10] + 1
    await database.setBdData('settings', 'id', "'1'", 'statistics_list_chatbot', f"'{update}'")
    await registration_6(message, bot, api)



async def registration_5_search(message: Message, bot: Bot, api: API):
    DATA_SETTINGS = await database.getBdData('settings', 'id', '1')
    update = DATA_SETTINGS[11] + 1
    await database.setBdData('settings', 'id', "'1'", 'statistics_search', f"'{update}'")
    await registration_6(message, bot, api)



async def registration_5_youtube(message: Message, bot: Bot, api: API):
    DATA_SETTINGS = await database.getBdData('settings', 'id', '1')
    update = DATA_SETTINGS[12] + 1
    await database.setBdData('settings', 'id', "'1'", 'statistics_youtube', f"'{update}'")
    await registration_6(message, bot, api)



async def registration_5_other(message: Message, bot: Bot, api: API):
    DATA_SETTINGS = await database.getBdData('settings', 'id', '1')
    update = DATA_SETTINGS[13] + 1
    await database.setBdData('settings', 'id', "'1'", 'statistics_other', f"'{update}'")
    await registration_6(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Предложение о рассылке
async def registration_6(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'registration.registration_6'")
    DATA_SETTINGS = await database.getBdData('settings', 'id', '1')
    await message.answer(
        message=f"📬 Желаете подписаться на новостную рассылку проекта?\n\n"
                f"Если вы согласитесь, то при каждой рассылке вы будете получать {await database.pretty(DATA_SETTINGS[14])} долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
            .add(Text("Подписаться", {"cmd": "registration.registration_6_accept"}), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("❌ Отказаться", {"cmd": "registration.registration_6_denial"}), color=KeyboardButtonColor.SECONDARY)
            .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Варианты ответа на подписку на рассылку
async def registration_6_accept(message: Message, bot: Bot, api: API):
    await database.setMultiUserData(message.from_id, "mailing_project = '✅ Подписан', mailing_server = '❌ Не подписан'")
    await message.answer(
        message=f"✅ Вы успешно подписались на рассылку о новостях проекта.\n"
                f"⚠ Чтобы отписаться от данной рассылки, вам необходимо перейти в настройки вашего персонажа."
    )
    await registration_7(message, bot, api)



async def registration_6_denial(message: Message, bot: Bot, api: API):
    await database.setMultiUserData(message.from_id, "mailing_project = '❌ Не подписан', mailing_server = '❌ Не подписан', state = 'registration.registration_7'")
    await message.answer(
        message=f"❌ Вы отказались от рассылки.\n"
                f"⚠ Вы всегда можете подписаться от отписаться от рассылки в настройках персонажа."
    )
    await registration_7(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Установка начальных значений у пользователя
async def registration_7(message: Message, bot: Bot, api: API):
    DATA_SETTINGS = await database.getBdData('settings', 'id', "'1'")
    await database.setMultiUserData(message.from_id, f"lvl = '{DATA_SETTINGS[18]}', dollars = '{DATA_SETTINGS[17]}', donate = '{DATA_SETTINGS[19]}'")
    await registration_8(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Забрать пособие и начать игру
async def registration_8(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'registration.registration_8'")
    DATA_SETTINGS = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"✈ Каждый человек, который прилетает в штат @{DATA_SETTINGS[4]}({DATA_SETTINGS[2]}) получает начальное пособие:\n\n"
                f"— 💵 Доллары » {await database.pretty(DATA_SETTINGS[17])}\n\n"
                f"ℹ Данного пособия будет достаточно до того момента, пока вы не найдете себе работу.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Callback("💵 Забрать пособие", payload={"cmd": "mainMenu.ShowFixFromId"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Сообщение выводится в том случае, если был передан Message
async def registration_9(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'registration.registration_9'")
    DATA_SETTINGS = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🔰 Желаете ли вы просмотреть дополнительную информацию о нашем сервере?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Да", {"cmd": "excursion.Show1"}), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("❌ Отказаться", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# Сообщение выводится, если был передан from_id (т.е. от Callback)
async def registration_9_1(from_id, bot: Bot, api: API):
    await database.setUserData(from_id.object.user_id, 'state', "'registration.registration_9'")
    DATA_SETTINGS = await database.getBdData('settings', 'id', "'1'")
    await bot.api.messages.send(
        user_id=from_id.object.user_id,
        random_id=random.randint(1, 999999999),
        message=f"🔰 Желаете ли вы просмотреть дополнительную информацию о нашем сервере?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Да", {"cmd": "excursion.Show1"}), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("❌ Отказаться", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Быстрое удаление аккаунта и создание нового
async def newAccaunt(message: Message, bot: Bot, api: API):
    await database.deleteUserData(message.from_id)
    await registration_1(message, bot, api)