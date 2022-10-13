
# Ферма

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.Show'")
    data = await database.getUserData(message.from_id)
    if data[27] == 'Безработный' or data[27] != 'Фермер':
        await message.answer(
            message=f"🥔 Ферма\n\n"
                    f"👨‍🌾 Здраствуй, меня зовут Том и добро пожаловать на мою ферму. Вы что-то хотите?",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.newGuysWorks"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("💼 Устроиться на работу", {"cmd": "farm.Getting"}), color=KeyboardButtonColor.POSITIVE)
                    .row()
                    .add(Text("📖 Информация по зарплатам", {"cmd": "farm.Info1"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Виды работ", {"cmd": "farm.Info2"}), color=KeyboardButtonColor.SECONDARY)
            )
        )
    else:
        await message.answer(
            message=f"🥔 Ферма\n\n"
                    f"👨‍🌾 Здраствуй, {data[3]}. Не хочешь сегодня поработать?",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.newGuysWorks"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("⚒ Работать", {"cmd": "farm.choose"}), color=KeyboardButtonColor.POSITIVE)
                    .row()
                    .add(Text("💼 Уволиться", {"cmd": "farm.Leave"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Информация по зарплатам", {"cmd": "farm.Info1"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Виды работ", {"cmd": "farm.Info2"}), color=KeyboardButtonColor.SECONDARY)
            )
        )


async def Getting(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'work', "'Фермер'")
    await message.answer(
        message=f"✅ Вы успешно устроились на работу фермера"
        )
    await Show(message, bot, api)


async def Leave(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'work', "'Безработный'")
    await message.answer(
        message=f"✅ Вы успешно уволились с работы"
        )
    await Show(message, bot, api)


async def Info1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.Info1'")
    await message.answer(
        message=f"🥔 » 📖 Информация по зарплатам\n\n"
                f"На данной работе есть несколько должностей. На каждой должности вы получаете разную зарплату.\n\n"
                f"Фермер (сбор картошки) » 5 долларов (💵)\n"
                f"Тракторист » 15 долларов (💵)\n"
                f"Комбайнер » 75 долларов (💵)\n"
                f"Пилот кукурузника » 150 долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "farm.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )



async def Info2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.Info2'")
    await message.answer(
        message=f"🥔 » 📖 Виды работ\n\n"
                f"На ферме есть несколько служебных должностей, на которых вы можете работать. Узнать на каких должностях вы можете "
                f"работать, вы можете узнать в скиллах -> навык фермера\n\n"
                f"Фермер (сбор картошки) — это самая первая должность на ферме. Именно на данной должности вы будете ходить по полю и собирать "
                f"картошку.\n"
                f"Тракторист — вторая должность после фермера. На данной должности вы будете работать на тракторе и вспахивать поле ковшом\n"
                f"Комбайнер — третья должность после тракториста. На данной должности вы собираете готовую кукурузу\n"
                f"Пилот кукурзника — четвертая должность после комбайнера. На данной должности вы должны будете иметь лицензию пилотирования. Тут вы будете летать на кукурзнике и сбрасывать химические элементы.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "farm.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )


async def choose(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.choose'")
    await message.answer(
        message=f"🥔 » ⚒ Работать\n\n"
                f"Выберите, на какой должности вы будете работать",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "farm.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("⚒ Фермер", {"cmd": "farm.CheckRab1"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("⚒ Тракторист", {"cmd": "farm.CheckRab2"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("⚒ Комбайнер", {"cmd": "farm.CheckRab3"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("⚒ Пилот кукурузника", {"cmd": "farm.CheckRab4"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



# --------------------------------------------------------------------------------------------

# Работа чернорабочего (первая)

# --------------------------------------------------------------------------------------------

async def CheckRab1(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    data = ast.literal_eval(data[30])
    data = list(data)
    if int(data[0]) >= 0:
        await message.answer(
            message=f"✅ Вы успешно устроились на работу фермера"
        )
        await rab1_1(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Вы не можете работать на данной должности, так-как у вас недостаточно очков навыка фермера"
        )
        await choose(message, bot, api)


async def rab1_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab1_1'")
    await database.setUserData(message.from_id, 'temporary_var', f"'0'")
    await message.answer(
        message=f"📦 Для того, чтобы начать работу, вам необходимо взять спец. инструменты из ангара фермы",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("📦 Взять инструменты", {"cmd": "farm.rab1_2"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab1_2'")
    await message.answer(
        message=f"📦 Вы взяли спец. инструменты из ангара"
    )
    await message.answer(
        message=f"🥔 Найдите поле, где можно собирать картошку",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👁 Найти поле", {"cmd": "farm.rab1_3"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"👁 Вы ищете поле для сбора урожая"
    )
    await asyncio.sleep(2)
    await message.answer(
        message=f"👁 Вы нашли поле, где можно собирать урожай"
    )
    await rab1_4(message, bot, api)



async def rab1_4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab1_4'")
    await message.answer(
        message=f"🚶 Подойдите к полю, чтобы начать собирать урожай",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶 Подойти к полю", {"cmd": "farm.rab1_5"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚶 Вы идете к полю"
    )
    await asyncio.sleep(2)
    await message.answer(
        message=f"🚶 Вы подошли к полю и готовы собирать картошку"
    )
    await rab1_6(message, bot, api)



async def rab1_6(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab1_6'")
    await asyncio.sleep(1)
    await message.answer(
        message=f"👨‍🌾 Собирайте урожай",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🥔 Собирать картошку", {"cmd": "farm.rab1_7"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_7(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🥔 Вы наклонились и начинаете собирать картошку"
    )
    await asyncio.sleep(random.randint(5,15))
    kukurusa = random.randint(1, 5) # количество кукурузы, которое можем забрать за раз
    data = await database.getUserData(message.from_id)
    datafarm = ast.literal_eval(data[30])
    datafarm = list(datafarm)
    new_data = int(data[44]) + kukurusa
    datafarm[0] = int(datafarm[0]) + 1
    await database.setMultiUserData(message.from_id, f"temporary_var = '{new_data}', skillWorks = '{datafarm}'")
    await message.answer(
        message=f"🥔 Вы собрали {kukurusa} картошку(и)"
    )
    await rab1_8(message, bot, api)



async def rab1_8(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab1_8'")
    await asyncio.sleep(1)
    await message.answer(
        message=f"🥔 Хотите продолжить работу или сдать всю картошку и получить деньги за труд?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💵 Закончить работу", {"cmd": "farm.rab1_end"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🥔 Продолжить работу", {"cmd": "farm.rab1_6"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_end(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.Show'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    zarplata = int(data[44]) * 5 * server_settings[26]
    itog = int(data[12]) + zarplata
    await database.setUserData(message.from_id, 'dollars', f"'{itog}'")

    await message.answer(
        message=f"👨‍🌾 Том » Спасибо, что поработал на моей ферме. Ты собрал {int(data[44])} картошки и в итоге твоя зарплата составляет {zarplata} долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💵 Забрать деньги", {"cmd": "farm.Show"}), color=KeyboardButtonColor.SECONDARY)
        )
    )





# --------------------------------------------------------------------------------------------

# Работа тракториста (вторая)

# --------------------------------------------------------------------------------------------


async def CheckRab2(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    datafarm = ast.literal_eval(data[30])
    datafarm = list(datafarm)
    datalicense = ast.literal_eval(data[24])
    datalicense = list(datalicense)
    if int(datafarm[0]) >= 500:
        if datalicense[0] != '❌ Отсутствует':
            await message.answer(
                message=f"✅ Вы успешно устроились на работу тракториста"
            )
            await rab2_1(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Вы не можете работать на тракторе, так-как у вас нет прав на автомобили!"
            )
            await choose(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Вы не можете работать на данной должности, так-как у вас недостаточно очков навыка фермера"
        )
        await choose(message, bot, api)



async def rab2_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab2_1'")
    await database.setUserData(message.from_id, 'temporary_var', f"'0'")
    await message.answer(
        message=f"📦 Для того, чтобы начать работу трактористом, вам необходимо взять ключи от трактора",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔑 Взять ключи", {"cmd": "farm.rab2_2"}), color=KeyboardButtonColor.SECONDARY)
        )
    )




async def rab2_2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab2_2'")
    await message.answer(
        message=f"🔑 Вы взяли ключи от трактора в гараже"
    )
    await message.answer(
        message=f"🚜 Подойдите и сядьте в тот трактор, от которого вы взяли ключи",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Подойти и сесть в трактор", {"cmd": "farm.rab2_3"}), color=KeyboardButtonColor.SECONDARY)
        )
    )




async def rab2_3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚜 Вы идете к трактору..."
    )
    await asyncio.sleep(3)
    await message.answer(
        message=f"🚜 Вы садитесь в трактор..."
    )
    await asyncio.sleep(1)
    await database.setUserData(message.from_id, 'state', "'farm.rab2_3'")
    await message.answer(
        message=f"🔑 Заведите трактор",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔑 Завести трактор", {"cmd": "farm.rab2_4"}), color=KeyboardButtonColor.SECONDARY)
        )
    )




async def rab2_4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🔑 Вы вставили ключ в зажигание"
    )
    await asyncio.sleep(1)
    await message.answer(
        message=f"🔑 Вы вставили ключ и поворачиваете его..."
    )
    await asyncio.sleep(1)
    await message.answer(
        message=f"🔑 Трактор завелся"
    )
    await asyncio.sleep(1)
    await database.setUserData(message.from_id, 'state', "'farm.rab2_4'")
    await message.answer(
        message=f"🚜 Выезжайте из гаража и едьте к полю",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Выехать из гаража", {"cmd": "farm.rab2_5"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab2_5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚜 Вы выезжаете из гаража"
    )
    await asyncio.sleep(5)
    await message.answer(
        message=f"🚜 Вы выехали из гаража и едете к полю..."
    )
    await asyncio.sleep(1)
    await message.answer(
        message=f"🚜 Вы приехали к полю"
    )
    await asyncio.sleep(1)
    await database.setUserData(message.from_id, 'state', "'farm.rab2_5'")
    await message.answer(
        message=f"🚜 Прицепите ковш к трактору",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Прицепить ковш к трактору", {"cmd": "farm.rab2_6"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab2_6(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚜 Вы цепляете ковш к трактору"
    )
    await asyncio.sleep(5)
    await message.answer(
        message=f"🚜 Вы прицепили ковш к трактору"
    )
    await asyncio.sleep(1)
    await database.setUserData(message.from_id, 'state', "'farm.rab2_6'")
    await message.answer(
        message=f"🚜 Если вы готовы, то начинайте движение по полю",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Начать движение", {"cmd": "farm.rab2_7"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab2_7(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚜 Вы начали движение"
    )
    await asyncio.sleep(5)
    await message.answer(
        message=f"🚜 Вы вспахиваете землю своим ковшом"
    )
    await asyncio.sleep(10)
    await message.answer(
        message=f"🚜 Вы вспахали половину поля, продолжаем оставшуюся часть вспахивать"
    )
    await asyncio.sleep(10)
    await rab2_8(message, bot, api)



async def rab2_8(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data = await database.getUserData(message.from_id)
    datafarm = ast.literal_eval(data[30])
    datafarm = list(datafarm)
    new_data = int(data[44]) + 1
    datafarm[0] = int(datafarm[0]) + 2
    await database.setMultiUserData(message.from_id, f"temporary_var = '{new_data}', skillWorks = '{datafarm}'")
    await message.answer(
        message=f"🌽 Вы вспохали поле"
    )
    await rab2_9(message, bot, api)



async def rab2_9(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab2_9'")
    await message.answer(
        message=f"🌽 Желаете продолжить или хотите закончить работу и получить деньги за труд?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💵 Закончить работу", {"cmd": "farm.rab2_end"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌽 Продолжить работу", {"cmd": "farm.rab2_10"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab2_10(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab2_10'")
    await message.answer(
        message=f"🚜 Вы едете к новому полю"
    )
    await asyncio.sleep(5)
    await message.answer(
        message=f"🚜 Вы приехали к новому полю"
    )
    await message.answer(
        message=f"🚜 Если вы готовы, то начинайте движение по полю",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Начать движение", {"cmd": "farm.rab2_7"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab2_end(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.Show'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    zarplata = int(data[44]) * 15 * server_settings[26]
    itog = int(data[12]) + zarplata
    await database.setUserData(message.from_id, 'dollars', f"'{itog}'")

    await message.answer(
        message=f"👨‍🌾 Том » Спасибо, что поработал на моей ферме. Ты вспохал {int(data[44])} поле(й) и в итоге твоя зарплата составляет {zarplata} долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💵 Забрать деньги", {"cmd": "farm.Show"}), color=KeyboardButtonColor.SECONDARY)
        )
    )












# --------------------------------------------------------------------------------------------

# Работа комбайнера (третья)

# --------------------------------------------------------------------------------------------


async def CheckRab3(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    datafarm = ast.literal_eval(data[30])
    datafarm = list(datafarm)
    datalicense = ast.literal_eval(data[24])
    datalicense = list(datalicense)
    if int(datafarm[0]) >= 3000:
        if datalicense[0] != '❌ Отсутствует':
            await message.answer(
                message=f"✅ Вы успешно устроились на работу комбайнера"
            )
            await rab3_1(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Вы не можете работать на комбайне, так-как у вас нет прав на автомобили!"
            )
            await choose(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Вы не можете работать на данной должности, так-как у вас недостаточно очков навыка фермера"
        )
        await choose(message, bot, api)



async def rab3_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab3_1'")
    await database.setUserData(message.from_id, 'temporary_var', f"'0'")
    await message.answer(
        message=f"📦 Для того, чтобы начать работу на комбайне, вам необходимо взять ключи от данного транспортного средства",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔑 Взять ключи", {"cmd": "farm.rab3_2"}), color=KeyboardButtonColor.SECONDARY)
        )
    )




async def rab3_2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab3_2'")
    await message.answer(
        message=f"🔑 Вы взяли ключи от комбайна"
    )
    await message.answer(
        message=f"🚜 Подойдите и сядьте в тот комбайн, от которого вы взяли ключи",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Подойти и сесть в комбайн", {"cmd": "farm.rab3_3"}), color=KeyboardButtonColor.SECONDARY)
        )
    )




async def rab3_3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚜 Вы идете к комбайну..."
    )
    await asyncio.sleep(5)
    await message.answer(
        message=f"🚜 Вы садитесь в комбайн..."
    )
    await asyncio.sleep(3)
    await database.setUserData(message.from_id, 'state', "'farm.rab3_3'")
    await message.answer(
        message=f"🔑 Заведите комбайн",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔑 Завести комбайн", {"cmd": "farm.rab3_4"}), color=KeyboardButtonColor.SECONDARY)
        )
    )




async def rab3_4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🔑 Вы вставили ключ в замок зажигания"
    )
    await asyncio.sleep(1)
    await message.answer(
        message=f"🔑 Вы поворачиваете ключ, чтобы завести комбайн"
    )
    await asyncio.sleep(3)
    await message.answer(
        message=f"🔑 Комбайн завелся"
    )
    await asyncio.sleep(1)
    await database.setUserData(message.from_id, 'state', "'farm.rab3_4'")
    await message.answer(
        message=f"🚜 Выезжайте из гаража и едьте к полю",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Выехать из гаража", {"cmd": "farm.rab3_5"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab3_5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚜 Вы выезжаете из гаража"
    )
    await asyncio.sleep(5)
    await message.answer(
        message=f"🚜 Вы выехали из гаража и едете к полю..."
    )
    await asyncio.sleep(10)
    await message.answer(
        message=f"🚜 Вы приехали к полю"
    )
    await asyncio.sleep(1)
    await database.setUserData(message.from_id, 'state', "'farm.rab3_5'")
    await message.answer(
        message=f"🚜 Трактор с прицепом уже ждет вас. Вы готовы срезать колосья и выбивать из колосков зёрна?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Начать сбор зерен", {"cmd": "farm.rab3_6"}), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("❌ Закончить работу", {"cmd": "farm.rab3_end1"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab3_6(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚜 Вы включили жатки и начали движение по полю."
    )
    await asyncio.sleep(5)
    await message.answer(
        message=f"🚜 Параллельно за вами поехал трактор с прицепом"
    )
    await asyncio.sleep(3)
    await database.setUserData(message.from_id, 'state', "'farm.rab3_6'")
    await message.answer(
        message=f"🚜 Вы сбиваетесь с маршрута, выровните комбайн",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Выровнить комбайн", {"cmd": "farm.rab3_7"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab3_7(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚜 Вы выровнили комбайн и продолжаете движение"
    )
    await asyncio.sleep(10)
    await database.setUserData(message.from_id, 'state', "'farm.rab3_7'")
    await message.answer(
        message=f"🚜 Вы сбиваетесь с маршрута, выровните комбайн",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Выровнить комбайн", {"cmd": "farm.rab3_8"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab3_8(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚜 Вы выровнили комбайн и продолжаете движение"
    )
    await asyncio.sleep(10)
    await database.setUserData(message.from_id, 'state', "'farm.rab3_8'")
    await message.answer(
        message=f"🏞 Вы доехали до конца поле, разверните комбайн, чтобы продолжить работу.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Развернуть комбайн", {"cmd": "farm.rab3_9"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab3_9(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab3_9'")
    await message.answer(
        message=f"🚜 Перед разворотом комбайна, выключите жатки",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Выключить жатки", {"cmd": "farm.rab3_9_1"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab3_9_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data = await database.getUserData(message.from_id)
    datafarm = ast.literal_eval(data[30])
    datafarm = list(datafarm)
    new_data = int(data[44]) + 1
    datafarm[0] = int(datafarm[0]) + 2
    await database.setMultiUserData(message.from_id, f"temporary_var = '{new_data}', skillWorks = '{datafarm}'")
    await rab3_10(message, bot, api)


async def rab3_10(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚜 Вы выключили жатки и начинаете разворот"
    )
    await asyncio.sleep(12)
    await database.setUserData(message.from_id, 'state', "'farm.rab3_10'")
    await message.answer(
        message=f"🚜 Вы развернули комбайн. Готовы ли вы продолжить?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Продолжить", {"cmd": "farm.rab3_6"}), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("❌ Закончить работу", {"cmd": "farm.rab3_end1"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab3_end1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab3_end1'")
    await message.answer(
        message=f"🚜 Вы решили, что хотите закончить работу. Для завершения работы, верните комбайн обратно в ангар.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Ехать к ангару", {"cmd": "farm.rab3_end2"}), color=KeyboardButtonColor.SECONDARY)
        )
    )

async def rab3_end2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚜 Вы едете к ангару..."
    )
    await asyncio.sleep(8)
    await database.setUserData(message.from_id, 'state', "'farm.rab3_end2'")
    await message.answer(
        message=f"🚜 Вы приехали в ангар. Аккуратно припаркуйте комбайн",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚜 Припарковать комбайн", {"cmd": "farm.rab3_end3"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab3_end3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚜 Вы паркуете комбайн"
    )
    await asyncio.sleep(8)
    await database.setUserData(message.from_id, 'state', "'farm.rab3_end2'")
    await message.answer(
        message=f"🚜 Комбайн припаркован. Заглушите двигатель и сдайте ключи начальству",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔑 Заглушить двигатель", {"cmd": "farm.rab3_end4"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab3_end4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🔑 Вы заглушили двигатель и вытащили ключи из замка зажигания"
    )
    await asyncio.sleep(8)
    await message.answer(
        message=f"🚶 Вы вышли из трактора и закрыли дверь"
    )
    await asyncio.sleep(2)
    await database.setUserData(message.from_id, 'state', "'farm.rab3_end2'")
    await message.answer(
        message=f"🚶 Подойдите к начальству, чтобы получить деньги и сдать ключи от комбайна",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶 Подойти к начальству", {"cmd": "farm.rab3_end5"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab3_end5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚶 Вы идете к начальству..."
    )
    await asyncio.sleep(8)
    await rab3_end6(message, bot, api)


async def rab3_end6(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.Show'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    zarplata = int(data[44]) * 75 * server_settings[26]
    itog = int(data[12]) + zarplata
    await database.setUserData(message.from_id, 'dollars', f"'{itog}'")

    await message.answer(
        message=f"👨‍🌾 Том » Спасибо за вашу работу на комбайне. Вы проехали на тракторе {int(data[44])} раз(а) и получаете за это {zarplata} долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💵 Забрать деньги", {"cmd": "farm.Show"}), color=KeyboardButtonColor.SECONDARY)
        )
    )















# --------------------------------------------------------------------------------------------

# Работа комбайнера (третья)

# --------------------------------------------------------------------------------------------


async def CheckRab4(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    datafarm = ast.literal_eval(data[30])
    datafarm = list(datafarm)
    datalicense = ast.literal_eval(data[24])
    datalicense = list(datalicense)
    if int(datafarm[0]) >= 7500:
        if datalicense[5] != '❌ Отсутствует':
            await message.answer(
                message=f"✅ Вы успешно устроились на работу пилота кукурузника"
            )
            await rab4_1(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Вы не можете работать на кукурузнике, так-как у вас нет прав на самолеты!"
            )
            await choose(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Вы не можете работать на данной должности, так-как у вас недостаточно очков навыка фермера"
        )
        await choose(message, bot, api)



async def rab4_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab4_1'")
    await database.setUserData(message.from_id, 'temporary_var', f"'0'")
    await message.answer(
        message=f"👨‍🌾 Том » Подойди к Джейн, она тебе расскажет все детали про работу на кукурузнике. Желаю заранее хорошей работы.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💬 Спасибо", {"cmd": "farm.rab4_2_1"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💬 Благодарю", {"cmd": "farm.rab4_2_1"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💬 Такое не говорят заранее", {"cmd": "farm.rab4_2_2"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("❌ Закончить работу", {"cmd": "farm.rab4_end1_1"}), color=KeyboardButtonColor.SECONDARY)
        )
    )




async def rab4_2_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab4_2_1'")
    await message.answer(
        message=f"👨‍🌾 Том » Да-да. Времени у нас мало, иди уже к ней.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶 Подойти к Джейн", {"cmd": "farm.rab4_3"}), color=KeyboardButtonColor.SECONDARY)
        )
    )




async def rab4_2_2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab4_2_2'")
    await message.answer(
        message=f"👨‍🌾 Том » Ну как лучше считаешь, ладно, беги уже",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶 Подойти к Джейн", {"cmd": "farm.rab4_3"}), color=KeyboardButtonColor.SECONDARY)
        )
    )




async def rab4_3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚶 Вы идете к Джейн"
    )
    await asyncio.sleep(8)
    await message.answer(
        message=f"🚶 Вы подошли к Джейн."
    )
    await asyncio.sleep(1)
    await database.setUserData(message.from_id, 'state', "'farm.rab4_3'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"👩‍🌾 Джейн » Привет, {data[3]}.\n\n"
                f"У нас в ангаре стоит кукурузник, раз уж ты отважился на нем полетать, то получи от меня задание.\n\n"
                f"1. Тебе необходимо загрузить в кукурузник удобрения для полей.\n"
                f"2. Взлететь и подлететь к полю\n"
                f"3. Распылить удобрения на поле\n"
                f"4. Вернуться назад\n\n"
                f"У нас есть множество полей, которые необходимо удобрить.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💬 Окей", {"cmd": "farm.rab4_4"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("❌ Закончить работу", {"cmd": "farm.rab4_end2_1"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab4_4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab4_4'")
    await message.answer(
        message=f"👩‍🌾 Джейн » Тогда бери ключи от кукурузника и заводи его.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔑 Взять ключи", {"cmd": "farm.rab4_5"}), color=KeyboardButtonColor.POSITIVE)
        )
    )



async def rab4_5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab4_5'")
    await message.answer(
        message=f"🔑 Вы взяли ключи от кукурузника"
    )
    await message.answer(
        message=f"🛩 Подойдите к кукурузнику и откройте дверь",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶‍♂ Подойти к кукурузнику", {"cmd": "farm.rab4_6"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab4_6(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🚶‍♂ Вы идете к кукурузнику..."
    )
    await asyncio.sleep(10)
    await database.setUserData(message.from_id, 'state', "'farm.rab4_7'")
    await message.answer(
        message=f"‍♂ Вы подошли к кукурузнику",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔑  Открыть дверь кукурузника", {"cmd": "farm.rab4_7"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab4_7(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🔑 Вы открыли дверь кукурузника и сели за штурвал."
    )
    await asyncio.sleep(2)
    await database.setUserData(message.from_id, 'state', "'farm.rab4_7'")
    await message.answer(
        message=f"‍🔑 Вставьте ключи в замок зажигания",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔑 Вставить ключ", {"cmd": "farm.rab4_8"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab4_8(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🔑 Вы вставили ключ в замок зажигания"
    )
    await asyncio.sleep(2)
    await message.answer(
        message=f"🛩 Кукурузник завелся"
    )
    await database.setUserData(message.from_id, 'state', "'farm.rab4_8'")
    await message.answer(
        message=f"🛩 Подгоните ваш кукурузник к месту загрузки удобрений.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🛩 Подогнать кукурузник", {"cmd": "farm.rab4_9"}), color=KeyboardButtonColor.SECONDARY)
        )
    )

async def rab4_9(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🛩 Вы подгоняете кукурузник к месту загрузки удобрений..."
    )
    await asyncio.sleep(10)
    await database.setUserData(message.from_id, 'state', "'farm.rab4_9'")
    await message.answer(
        message=f"🛩 В ваш кукурузник загрузили удобрения, вы готовы к вылету.Подгоните кукурузник к взлетной полосе.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🛩 Подогнать кукурузник к полосе", {"cmd": "farm.rab4_10"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab4_10(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🛩 Вы подгоняете кукурузник к взлетной полосе"
    )
    await asyncio.sleep(10)
    await database.setUserData(message.from_id, 'state', "'farm.rab4_10'")
    await message.answer(
        message=f"🛩 Кукурузник на взлетной полосе. Взлетайте!",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🛩 Взлететь", {"cmd": "farm.rab4_11"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab4_11(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🛩 Вы взлетаете..."
    )
    await asyncio.sleep(5)
    await database.setUserData(message.from_id, 'state', "'farm.rab4_11'")
    await message.answer(
        message=f"🛩 Поверните кукурузник в ту сторону, в которую необходимо распылить удобрения",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🛩 Повернуть кукурузник", {"cmd": "farm.rab4_12"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab4_12(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🛩  Вы поворачиваете кукурузник в строну поля"
    )
    await asyncio.sleep(6)
    await message.answer(
        message=f"🛩 Вы летите в сторону поля"
    )
    await asyncio.sleep(15)
    await database.setUserData(message.from_id, 'state', "'farm.rab4_12'")
    await message.answer(
        message=f"🛩 Вы подлетаете к необходимому полю, пора открывать клапан для распыления удобрений",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🛩 Открыть клапан", {"cmd": "farm.rab4_13"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab4_13(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🛩 Вы открыли клапан и распыляете удобрения."
    )
    await asyncio.sleep(10)
    await database.setUserData(message.from_id, 'state', "'farm.rab4_13'")
    await message.answer(
        message=f"🛩 Вы распылили все удобрения, пора закрывать клапан.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🛩 Закрыть клапан", {"cmd": "farm.rab4_14"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab4_14(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab4_14'")
    await message.answer(
        message=f"🛩 Вы закрыли клапан. Возвращаетесь обратно на взлетную полосу",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🛩 Повернуть кукурузник", {"cmd": "farm.rab4_15"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab4_15(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🛩 Вы поворачиваете кукурузник в сторону взлетной полосы"
    )
    await asyncio.sleep(10)
    await database.setUserData(message.from_id, 'state', "'farm.rab4_15'")
    await message.answer(
        message=f"🛩 Вы повернули кукурузник, продолжайте пилотировать",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🛩 Пилотировать кукурузником", {"cmd": "farm.rab4_16"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab4_16(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🛩 Вы летите в строну взлетной полосы"
    )
    await asyncio.sleep(13)
    await database.setUserData(message.from_id, 'state', "'farm.rab4_16'")
    await message.answer(
        message=f"🛩 Вы подлетаете к полосе, приготовьтесь к посадке",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🛩 Приготовиться к посадке", {"cmd": "farm.rab4_16_1"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab4_16_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data = await database.getUserData(message.from_id)
    datafarm = ast.literal_eval(data[30])
    datafarm = list(datafarm)
    new_data = int(data[44]) + 1
    datafarm[0] = int(datafarm[0]) + 3
    await database.setMultiUserData(message.from_id, f"temporary_var = '{new_data}', skillWorks = '{datafarm}'")
    await rab4_17(message, bot, api)



async def rab4_17(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🛩 Вы готовитесь к посадке..."
    )
    await asyncio.sleep(15)
    await message.answer(
        message=f"🛩 Вы посадили кукурузник"
    )
    await database.setUserData(message.from_id, 'state', "'farm.rab4_17'")
    await message.answer(
        message=f"🛩 Готовы ли вы продолжить?",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Продолжить", {"cmd": "farm.rab4_9"}), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("❌ Закончить работу", {"cmd": "farm.rab4_end3_1"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab4_18(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab4_18'")
    await message.answer(
        message=f"🛩 Для продолжения работы, вам необходимо подогнать ваш кукурузник к месту загрузки удобрений.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🛩 Подогнать кукурузник", {"cmd": "farm.rab4_15"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab4_end1_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab4_end1_1'")
    await message.answer(
        message=f"👨‍🌾 Том » Страшно стало? Ладно, если захочешь поработать на кукурузнике, то приходи сюда снова.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💬 Спасибо", {"cmd": "farm.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💬 Хорошо", {"cmd": "farm.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💬 До свидания", {"cmd": "farm.Show"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab4_end2_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab4_end2_1'")
    await message.answer(
        message=f"👩‍🌾 Джейн » Испугался? Тогда ты не получаешь оплату. Как только передумаешь, вернешься в ангар. Я тут всегда.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💬 Хорошо", {"cmd": "farm.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💬 До свидания", {"cmd": "farm.Show"}), color=KeyboardButtonColor.SECONDARY)
        )
    )

async def rab4_end3_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.rab4_end3_1'")
    await message.answer(
        message=f"🛩 Подгоните кукурузник к ангару",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🛩 Подогнать кукурузник", {"cmd": "farm.rab4_end3_2"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab4_end3_2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🛩 Вы подгоняете кукурузник к ангару..."
    )
    await asyncio.sleep(10)
    await database.setUserData(message.from_id, 'state', "'farm.rab4_end3_2'")
    await message.answer(
        message=f"🔑 Заглушите двигатель и выньте ключи зажигания",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔑 Заглушить двигатель", {"cmd": "farm.rab4_end3_3"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab4_end3_3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🔑 Вы заглушили двигатель"
    )
    await asyncio.sleep(2)
    await database.setUserData(message.from_id, 'state', "'farm.rab4_end3_3'")
    await message.answer(
        message=f"🔑 Выньте ключи из замка зажигания",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔑 Вынуть ключи", {"cmd": "farm.rab4_end3_4"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab4_end3_4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🔑 Вы вытащили ключи"
    )
    await asyncio.sleep(4)
    await message.answer(
        message=f"🔑 Вы закрыли дверь у кукурузника"
    )
    await asyncio.sleep(2)
    await database.setUserData(message.from_id, 'state', "'farm.rab4_end3_4'")
    await message.answer(
        message=f"👨‍🌾 Джейн » Как работа? Думаю ты нам помог достаточно, однако приходи к нам еще раз, ведь работы у нас всегда много.\n\nПодойти к Тому, он выдаст тебе деньги за проделанный труд",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶‍♂ Подойти к Тому", {"cmd": "farm.rab4_end3_5"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab4_end3_5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'farm.Show'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    zarplata = int(data[44]) * 150 * server_settings[26]
    itog = int(data[12]) + zarplata
    await database.setUserData(message.from_id, 'dollars', f"'{itog}'")
    await message.answer(
        message=f"👨‍🌾 Том » Ты отлично поработал на моей ферме. Ты сделал {int(data[44])} полет(а) и получаешь за это {zarplata} долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💵 Забрать деньги", {"cmd": "farm.Show"}), color=KeyboardButtonColor.SECONDARY)
        )
    )