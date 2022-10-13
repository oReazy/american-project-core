# ----------------------------------------------------------------------------------------------------------------------

# Игровой Role-Play чат-бот для ВКонтакте.
#
# Автор: Reazy, 2022 год.

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, ast, states, json, time, datetime, random, traceback, loguru
from vkbottle.bot import Bot, Message, MessageEvent
from vkbottle import API, LoopWrapper, GroupEventType

from modules import database, registration, mainMenu
from modules.importantLocations import CentralBank, LicensingCenter, CityHall

# ----------------------------------------------------------------------------------------------------------------------

bot = Bot('aed307a7c1248aea24454fb0e44d8c6c94c92255e759f701023ab1963501be1683acfd6fea6fe0596a28a')
api = API('25a06c2cbdd3d2788f0af4bc75c6c4b5ede3e807d16143eafe0e03ff286ac2089760a2d7da9ac8b1a9415')
lw = LoopWrapper()

# ----------------------------------------------------------------------------------------------------------------------

# Стейты и их переходы.
functions = states.STATES

# ----------------------------------------------------------------------------------------------------------------------

# Обработка сообщений из бесед.
@bot.on.chat_message()
async def besidy(message: Message):
    await message.answer(
        message=f'❌ В данный момент нельзя запустить чат-бот в беседе!'
    )

# ----------------------------------------------------------------------------------------------------------------------

# Обработка сообщений из личных сообщений сообщества.
@bot.on.private_message()
async def main(message: Message):
    # Проверяем, есть ли игрок в базе данных, если нет, то переходим этап регистрации.
    if await database.findBaseData("vk_id", f"{message.from_id}") == 0:
        await registration.registration_1(message, bot, api)
    else:
        # Если игрок зарегистрирован в чат-боте, то обновляем переменную последнего написанного сообщения.
        await database.setMultiUserData(message.from_id, f"last_message = '{int(time.time())}'")

        # Получаем данные игрока, чтобы работать с ними в дальнейшем.
        DATA_USER = await database.getUserData(message.from_id)

        # Переход к активному стейту.
        if message.payload:
            payload = message.payload
            payload = payload.replace("{", "")
            payload = payload.replace("}", "")
            payload = payload.replace('"', "")
            payload = payload.replace(':', "")
            state = f"{payload[3:]}"
            try:
                await functions[state](message, bot, api)
            except Exception as ex:
                print(
                    f'\033[38m[\033[31m!\033[38m][\033[33mDEBUG\033[38m] Произошла ошибка: {ex}\n| {traceback.format_exc()}')
                state = f"{DATA_USER[2]}"
                await functions[state](message, bot, api)
        else:
            try:
                state = f"{DATA_USER[2]}"
                # print(f'\033[38m[\033[34m!\033[38m][\033[33mDEBUG\033[38m] Перемещение пользователя: {state}')
                await functions[state](message, bot, api)
            except Exception as ex:
                await message.answer(
                    message=f"😬 Как-то не удобно получилось. У нас возникла ошибка. Сейчас вас отправим в главное меню.")
                print(
                    f'\033[38m[\033[31m!\033[38m][\033[33mDEBUG\033[38m] Произошла ошибка: {ex}\n| {traceback.format_exc()}')
                await mainMenu.Show(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Обработка RAW эвентов от Callback-кнопок.
@bot.on.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=MessageEvent)
async def handle_message_event(event: MessageEvent):

    # Обновляем переменную last_message, добавляя время последнего сообщения от пользователя.
    await database.setUserData(event.object.user_id, "last_message", f"'{int(time.time())}'")

    # Вынимаем объект payload.
    payload = event.object.payload
    payloadcmd = payload['cmd']

    if payloadcmd == 'mainMenu.ShowFixFromId':
        await event.show_snackbar("✅ Вы успешно зарегистрировались")
        from_id = event.object.user_id
        await bot.api.messages.send(
            user_id=event.object.user_id,
            random_id=random.randint(1, 999999999),
            sticker_id=8441
        )
        await registration.registration_9_1(event, bot, api)

    if payloadcmd == 'CentralBank.CreateBankCard6':
        from_id = event.object.user_id
        await event.show_snackbar("⭐ Открыты новые возможности")
        await CentralBank.CreateBankCard6(from_id, bot)

    if payloadcmd == 'LicensingCenter.ShowBikes':
        from_id = event.object.user_id
        await event.show_snackbar("⭐ Открыты новые возможности")
        await LicensingCenter.BikeOpen(from_id, bot)

    if payloadcmd == 'LicensingCenter.Show':
        from_id = event.object.user_id
        await event.show_snackbar("⭐ Открыты новые возможности")
        await LicensingCenter.AutoOpen(from_id, bot)

    if payloadcmd == 'CityHall.getPassport':
        from_id = event.object.user_id
        await event.show_snackbar("⭐ Открыты новые возможности")
        await CityHall.GetPassport(from_id, bot)

    if payloadcmd == 'mainMenu.ShowFix':
        from_id = event.object.user_id
        await mainMenu.ShowFixFromId(from_id, bot, api)

    if payloadcmd == 'mainMenu.toLink':
        payloadlink = payload['link']
        await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=json.dumps({"type": "open_link", "link": payloadlink}),
        )

# ----------------------------------------------------------------------------------------------------------------------

async def Blocked():
    users = await database.getMultiProgramBdData('users', f"state = 'block.Show'")
    for selected in users:
        await bot.api.messages.send(
            user_id=selected[1],
            random_id=random.randint(100000, 999999999),
            peer_id=selected[1],
            message=f'🔄 Был перезагружен сервер\n\n'
                    f'💬 Мы перенесем вас в главное меню, так-как до этого ваши действия были заблокированы.'
        )
        await mainMenu.ShowFixFromId(selected[1], bot, api)

# ----------------------------------------------------------------------------------------------------------------------

bot.loop_wrapper.add_task(Blocked())

# ----------------------------------------------------------------------------------------------------------------------

bot.run_forever()