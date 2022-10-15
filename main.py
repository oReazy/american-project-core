# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#
# American Project — игровой чат-бот для ВКонтакте, в котором вам необходимо играть за персонажа. Зарабатывайте деньги,
# становитесь богаче и покупайте себе имущество. Как только вы всего достигните, вы можете выбрать направление,
# куда пойти.
#
# Автор: Вова Батенков, 2022 год.
#
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import asyncio, ast, states, json, time, datetime, random, traceback, loguru
from vkbottle.bot import Bot, Message, MessageEvent
from vkbottle import API, LoopWrapper, GroupEventType

from modules import database, registration, mainMenu

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

bot = Bot('aed307a7c1248aea24454fb0e44d8c6c94c92255e759f701023ab1963501be1683acfd6fea6fe0596a28a')
api = API('25a06c2cbdd3d2788f0af4bc75c6c4b5ede3e807d16143eafe0e03ff286ac2089760a2d7da9ac8b1a9415')
lw = LoopWrapper()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# Стейты и их переходы
functions = states.STATES

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# Обработка сообщений из бесед.
@bot.on.chat_message()
async def besidy(message: Message):
    await message.answer(
        message=f'❌ В данный момент нельзя запустить чат-бот в беседе!'
    )

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# Обработка сообщений из личных сообщений сообщества.
@bot.on.private_message()
async def main(message: Message):
    DATA_SETTINGS = await database.getBdData('settings', 'id', "'1'")
    # Проверяем, есть ли игрок в базе данных, если нет, то переходим этап регистрации.
    if await database.findBaseData("vk_id", f"{message.from_id}") == 0:
        await registration.registration_1(message, bot, api, None, DATA_SETTINGS)
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
                await functions[state](message, bot, api, DATA_USER, DATA_SETTINGS)
            except Exception as ex:
                print(
                    f'\033[38m[\033[31m!\033[38m][\033[33mDEBUG\033[38m] Произошла ошибка: {ex}\n| {traceback.format_exc()}')
                state = f"{DATA_USER[2]}"
                await functions[state](message, bot, api, DATA_USER, DATA_SETTINGS)
        else:
            try:
                state = f"{DATA_USER[2]}"
                # print(f'\033[38m[\033[34m!\033[38m][\033[33mDEBUG\033[38m] Перемещение пользователя: {state}')
                await functions[state](message, bot, api, DATA_USER, DATA_SETTINGS)
            except Exception as ex:
                await message.answer(
                    message=f"😬 Как-то не удобно получилось. У нас возникла ошибка. Сейчас вас отправим в главное меню.")
                print(
                    f'\033[38m[\033[31m!\033[38m][\033[33mDEBUG\033[38m] Произошла ошибка: {ex}\n| {traceback.format_exc()}')
                await mainMenu.Show(message, bot, api, DATA_USER, DATA_SETTINGS)

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

async def Blocked():
    users = await database.getMultiProgramBdData('users', f"state = 'block.Show'")
    DATA_SETTINGS = await database.getBdData('settings', 'id', "'1'")
    for selected in users:
        DATA_USER = await database.getUserData(selected[1])
        await bot.api.messages.send(
            user_id=selected[1],
            random_id=random.randint(100000, 999999999),
            peer_id=selected[1],
            message=f'🔄 Был перезагружен сервер\n\n'
                    f'💬 Мы перенесем вас в главное меню, так-как до этого ваши действия были заблокированы.'
        )
        await mainMenu.ShowFixFromId(selected[1], bot, api, DATA_USER, DATA_SETTINGS)

# ----------------------------------------------------------------------------------------------------------------------

bot.loop_wrapper.add_task(Blocked())

# ----------------------------------------------------------------------------------------------------------------------

bot.run_forever()