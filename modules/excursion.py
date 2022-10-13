
# Экскурсия по штату

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'excursion.Show1'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"👋 Добро пожаловать на @{server_settings[3]}({server_settings[1]}) в штат @{server_settings[4]}({server_settings[2]})\n\n"
                f"На нашем проекте вы найдете много интересного для себя. Увлекательные работы не позволят вам скучать! Уникальные "
                f"системы не дадут вам слоняться без дела. Администрация ответит вам на все интересующие вопросы. Каждый день "
                f"на сервере происходят обновления.\n\n"
                f"Новостная группа ВКонтакте » @{server_settings[3]}({server_settings[1]})\n"
                f"Новостная группа сервера » @{server_settings[4]}({server_settings[2]})",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("▶ Далее", {"cmd": "excursion.Show2"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

async def Show2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'excursion.Show2'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🗺 Сейчас вам желательно добраться до мэрии и получить паспорт\n\nЧтобы получить паспорт, "
                f"вам необходимо будет обратиться на ресепшен. После заполнение документов, вы сможете получить паспорт. С "
                f"этого момента вы сможете строить свою карьеру на нашем сервере.\n\n"
                f"Мэрию можно найти во вкладке «🗺 Карта», выбрав пункт «🏛 Важные места»",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("▶ Далее", {"cmd": "excursion.Show3"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

async def Show3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'excursion.Show3'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"👕 Вы можете в любой момент купить себе одежду в любом магазине одежды\n\n"
                f"Вы можете одевать майки, толстовки, шапки, кроссовки, цепочки и многое другое. Носить модную "
                f"и современную одежду или старую — решать вам.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("▶ Далее", {"cmd": "excursion.Show4"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

async def Show4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'excursion.Show4'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🪚 На нашем проекте вы можете работать на одной из этих работ:\n\n"
                f"— Фермер\n"
                f"— Тракторист\n"
                f"— Комбайнер\n"
                f"— Пилот кукурузника\n"
                f"— Работник на заводе\n"
                f"— Грузчик\n"
                f"— Доставщик\n"
                f"— Сборщик автомобилей\n"
                f"— Продавец в магазине одежды\n"
                f"— Водитель мусоровоза\n"
                f"— Дальнобойщик\n"
                f"— Таксист\n"
                f"— Инкассатор\n"
                f"— Пожарник\n"
                f"— Пилот\n"
                f"— Работник налоговой службы\n"
                f"— Водитель автобуса\n"
                f"— Механик\n"
                f"— Водитель трамвая\n"
                f"— Машинист электропоезда\n"
                f"— Дорожная служба\n"
                f"— Продавец хот-догов\n\n"
                f"Найти работу для новичков можно во вкладке «🗺 Карта», выбрав пункт «🧱 Работы для новичков»\n"
                f"Как только вы получите лицензии, то можете попробовать работать на основных работах",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("▶ Далее", {"cmd": "excursion.Show5"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

async def Show5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'excursion.Show5'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"📒 После этого отправляйтесь в центр лицензирования, чтобы получить лицензии.\n\n"
                f"Сдача на права в центре лицензирования не составит особого труда.\n"
                f"Сдача на права состоит из одного этапа:\n\n"
                f"— Теория\n\n"
                f"Центр лицензирования можно найти во вкладке «🗺 Карта», выбрав пункт «🏛 Важные места»",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("▶ Далее", {"cmd": "excursion.Show6"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

async def Show6(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'excursion.Show6'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🏬 Вы можете вступить в одну из организаций.\n\n"
                f"Любите защищать невиновных и наказывать преступников? Тогда ваш путь в законники!\n\n"
                f"Наоборот, любите грабить, разбойничать и убивать? Тогда ваш выбор банда или мафия\n\n"
                f"🔎 Не нашли что искали? Ничего страшного, так-как на нашем проекте можно создавать частные организации",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("▶ Далее", {"cmd": "excursion.Show7"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

async def Show7(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'excursion.Show7'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🚗 А как же машины? На данный момент у нас есть 5 автосалонов.\n\n"
                f"Авторынки разделены на несколько классов\n"
                f"На каждом из них можно купить транспортное средство\n"
                f"Будьте внимательны, количество автомобилей на сервере ограничено!",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("▶ Далее", {"cmd": "excursion.Show8"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

async def Show8(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'excursion.Show8'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🏡 На нашем сервере больше 1000 домов\n\n"
                f"На нашем сервере представлены дома разного класса, с разной комплектацией и многое другое.\n"
                f"Вы можете делать ремонт дома, тем самым меняя его интерьер и внешний облик дома.\n"
                f"У домов есть несколько улучшений, которые позволят создавать уникальные предметы!",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("▶ Далее", {"cmd": "excursion.Show9"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

async def Show9(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'excursion.Show9'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🔫 Став бандитом, вам придется сделать трудный выбор...\n\n"
                f"Вы можете воровать материалы, залезая на базы военных или ограбляя матовозы, подрывая их самодельной "
                f"бомбой, чтобы забрать груз,\n"
                f"Или вы можете без высоких рисков выращивать наркотики, где-то за городом, чтобы вас никто не заметил.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("▶ Далее", {"cmd": "excursion.Show10"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

async def Show10(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'excursion.Show10'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"💰 Заработав кругленькую сумму, можно купить бизнес\n\n"
                f"На нашем проекте можно купить различные бизнесы: АЗС, отели, магазины 24/7 и многое другое.\n\n"
                f"▶ Покупайте себе бизнес и зарабатывайте на нем!",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("▶ Далее", {"cmd": "excursion.Show11"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

async def Show11(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'excursion.Show10'")
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎉 Поздравляем, вы прошли краткий курс обучения.\n\n"
                f"Желаем вам приятной игры на нашем проекте",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👌 Спасибо", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )