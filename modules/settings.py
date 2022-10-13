
# Настройки игрока

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

# НАГРАДА ЗА АКТИВАЦИЮ УРОВНЯ
PROMOCODE_REWARD = [0, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 60000]

# ----------------------------------------------------------------------------------------------------------------------

# Главное меню настроен
async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'settings.Show'")
    await message.answer(
        message=f"🎯 » ⚙ Настройки персонажа",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🎟 Промокод", {"cmd": "settings.Promocodes"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("✉ Email", {"cmd": "settings.Email"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📬 Рассылки", {"cmd": "settings.Mailing"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🗃 Компактный дизайн", {"cmd": "settings.reDesign"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Меню промокодов
async def Promocodes(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'settings.Promocodes'")
    data = await database.getUserData(message.from_id)
    if data[52] == '':
        await message.answer(
            message=f"🎯 » ⚙ » 🎟 Промокод\n\n"
                    f"Промокоды — отличная возможность получить начальные игровые бонусы.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "settings.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text(f"🎟 Ввести промо-код", {"cmd": "settings.PromocodesEdit"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text(f"🎟 Управление промокодом", {"cmd": "settings.PromocodesCheck"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    if data[52] != '':
        await message.answer(
            message=f"🎯 » ⚙ » 🎟 Промокод\n\n"
                    f"Так-как вы уже активировали промокод, вам больше не доступен ввод нового",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "settings.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text(f"🎟 Управление промокодом", {"cmd": "settings.PromocodesCheck"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )

# ----------------------------------------------------------------------------------------------------------------------

# Панель промокодов
async def PromocodesPanel(message: Message, bot: Bot, api: API):
        await database.setUserData(message.from_id, 'state', "'settings.PromocodesPanel'")
        await message.answer(
            message=f"🎯 » ⚙ » 🎟 » 🎟 Управление промокодом\n\n",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "settings.Promocodes"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("📈 Рейтинг промокодов сервера", {"cmd": "settings.PromocodesPanelTOPServer"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🎟 Управление промокодом", {"cmd": "settings.PromocodesPanelEdit"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )

# ----------------------------------------------------------------------------------------------------------------------

# Управление промокодом
async def PromocodesPanelEdit(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'settings.PromocodesPanelEdit'")
    data_promocode = await database.getBdData('promo', 'creator_vk_id', f"'{message.from_id}'")

    if data_promocode[3] == 1:
        min_lvl = 6
    if data_promocode[3] == 2:
        min_lvl = 6
    if data_promocode[3] == 3:
        min_lvl = 6
    if data_promocode[3] == 4:
        min_lvl = 6
    if data_promocode[3] == 5:
        min_lvl = 6
    if data_promocode[3] == 6:
        min_lvl = 6
    if data_promocode[3] == 7:
        min_lvl = 5
    if data_promocode[3] == 8:
        min_lvl = 5
    if data_promocode[3] == 9:
        min_lvl = 5
    if data_promocode[3] == 10:
        min_lvl = 4

    await message.answer(
        message=f"🎯 » ⚙ » 🎟 » 🎟 » 🎟 Управление промокодом\n\n"
                f"🎟 Ваш промо-код » {data_promocode[2]}\n\n"
                f"🌐 Уровень промо-кода » {data_promocode[3]} из 10\n"
                f"✅ Количество активаций » {data_promocode[4]}\n\n"
                f"🌐 Для активации промо-кода, игроку необходим {min_lvl} игровой уровень\n"
                f"💰 За активацию промокода, игрок получает {await database.pretty(PROMOCODE_REWARD[data_promocode[3]])} долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "settings.PromocodesPanel"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🔼 Улучшить промокод", {"cmd": "settings.PromocodesPanelEditUpLVL"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Панель улучшения промокода
async def PromocodesPanelEditUpLVL(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'settings.PromocodesPanelEditUpLVL'")
    data_promocode = await database.getBdData('promo', 'creator_vk_id', f"'{message.from_id}'")
    data_user = await database.getUserData(message.from_id)
    if data_promocode[3] < 1:
        LVL_1 = f'Уровень 1 » Бонус {await database.pretty(PROMOCODE_REWARD[1])} долларов (💵) при активации.\n\n'
    if data_promocode[3] >= 1:
        LVL_1 = f'✅ Уровень 1 » Бонус {await database.pretty(PROMOCODE_REWARD[1])} долларов (💵) при активации.\n\n'

    if data_promocode[3] < 2:
        LVL_2 = f'Уровень 2 » Бонус {await database.pretty(PROMOCODE_REWARD[2])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 5 активаций промокода\n\n'
    if data_promocode[3] >= 2:
        LVL_2 = f'✅ Уровень 2 » Бонус {await database.pretty(PROMOCODE_REWARD[2])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 5 активаций промокода\n\n'

    if data_promocode[3] < 3:
        LVL_3 = f'Уровень 3 » Бонус {await database.pretty(PROMOCODE_REWARD[3])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 10 активаций промокода\n\n'
    if data_promocode[3] >= 3:
        LVL_3 = f'✅ Уровень 3 » Бонус {await database.pretty(PROMOCODE_REWARD[3])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 10 активаций промокода\n\n'

    if data_promocode[3] < 4:
        LVL_4 = f'Уровень 4 » Бонус {await database.pretty(PROMOCODE_REWARD[4])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 20 активаций промокода\n\n'
    if data_promocode[3] >= 4:
        LVL_4 = f'✅ Уровень 4 » Бонус {await database.pretty(PROMOCODE_REWARD[4])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 20 активаций промокода\n\n'

    if data_promocode[3] < 5:
        LVL_5 = f'Уровень 5 » Бонус {await database.pretty(PROMOCODE_REWARD[5])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 50 активаций промокода\n\n'
    if data_promocode[3] >= 5:
        LVL_5 = f'✅ Уровень 5 » Бонус {await database.pretty(PROMOCODE_REWARD[5])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 50 активаций промокода\n\n'

    if data_promocode[3] < 6:
        LVL_6 = f'Уровень 6 » Бонус {await database.pretty(PROMOCODE_REWARD[6])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 100 активаций промокода\n\n'
    if data_promocode[3] >= 6:
        LVL_6 = f'✅ Уровень 6 » Бонус {await database.pretty(PROMOCODE_REWARD[6])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 100 активаций промокода\n\n'

    if data_promocode[3] < 7:
        LVL_7 = f'Уровень 7 » Бонус {await database.pretty(PROMOCODE_REWARD[7])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 150 активаций промокода\n\n'
    if data_promocode[3] >= 7:
        LVL_7 = f'✅ Уровень 7 » Бонус {await database.pretty(PROMOCODE_REWARD[7])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 150 активаций промокода\n\n'

    if data_promocode[3] < 8:
        LVL_8 = f'Уровень 8 » Бонус {await database.pretty(PROMOCODE_REWARD[8])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 350 активаций промокода\n\n'
    if data_promocode[3] >= 8:
        LVL_8 = f'✅ Уровень 8 » Бонус {await database.pretty(PROMOCODE_REWARD[8])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 350 активаций промокода\n\n'

    if data_promocode[3] < 9:
        LVL_9 = f'Уровень 9 » Бонус {await database.pretty(PROMOCODE_REWARD[9])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 500 активаций промокода\n\n'
    if data_promocode[3] >= 9:
        LVL_9 = f'✅ Уровень 9 » Бонус {await database.pretty(PROMOCODE_REWARD[9])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 500 активаций промокода\n\n'

    if data_promocode[3] < 10:
        LVL_10 = f'Уровень 10 » Бонус {await database.pretty(PROMOCODE_REWARD[10])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 750 активаций промокода'
    if data_promocode[3] >= 10:
        LVL_10 = f'✅ Уровень 10 » Бонус {await database.pretty(PROMOCODE_REWARD[10])} долларов (💵) при активации.\n' \
                f'📃 Цена » 1000 алмазов (💎) и 750 активаций промокода'


    await message.answer(
        message=f"🎯 » ⚙ » 🎟 » 🎟 » 🎟 » 🔼 Улучшить промокод\n\n"
                f"🌐 Уровень промо-кода » {data_promocode[3]}\n"
                f"✅ Количество активаций » {data_promocode[4]}\n"
                f"💎 Текущее состояние счета » {await database.pretty(data_user[20])}\n\n"
                f"{LVL_1} {LVL_2} {LVL_3} {LVL_4} {LVL_5} {LVL_6} {LVL_7} {LVL_8} {LVL_9} {LVL_10}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "settings.PromocodesPanelEdit"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🔼 Повысить", {"cmd": "settings.PromocodesPanelEditUpLVLQuestion"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Вопрос: вы дейсвительно хотите протратить алмазы
async def PromocodesPanelEditUpLVLQuestion(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'settings.PromocodesPanelEditUpLVLQuestion'")
    data_promocode = await database.getBdData('promo', 'creator_vk_id', f"'{message.from_id}'")
    data_user = await database.getUserData(message.from_id)
    if data_promocode[3] != 10:
        if data_promocode[3] == 0:
            min_activation = 0
        if data_promocode[3] == 1:
            min_activation = 5
        if data_promocode[3] == 2:
            min_activation = 10
        if data_promocode[3] == 3:
            min_activation = 20
        if data_promocode[3] == 4:
            min_activation = 50
        if data_promocode[3] == 5:
            min_activation = 100
        if data_promocode[3] == 6:
            min_activation = 150
        if data_promocode[3] == 7:
            min_activation = 350
        if data_promocode[3] == 8:
            min_activation = 500
        if data_promocode[3] == 9:
            min_activation = 750
        if min_activation == 0:
            await message.answer(
                message=f"🎯 » ⚙ » 🎟 » 🎟 » 🎟 » 🔼 » 🔼 Повысить\n\n"
                        f"⚠ Вы уверены, что хотите потратить 1000 алмазов (💎) на повышение до {data_promocode[3] + 1} уровня промо-кода",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("◀ Назад", {"cmd": "settings.PromocodesPanelEditUpLVL"}), color=KeyboardButtonColor.PRIMARY)
                        .row()
                        .add(Text("Повысить", {"cmd": "settings.PromocodesPanelEditUpLVLBuy"}), color=KeyboardButtonColor.POSITIVE)
                        .get_json()
                )
            )
        else:
            await message.answer(
                message=f"🎯 » ⚙ » 🎟 » 🎟 » 🎟 » 🔼 » 🔼 Повысить\n\n"
                        f"⚠ Вы уверены, что хотите потратить 1000 алмазов (💎) и имеете {min_activation} активаций на повышение до {data_promocode[3] + 1} уровня промо-кода",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("◀ Назад", {"cmd": "settings.PromocodesPanelEditUpLVL"}), color=KeyboardButtonColor.PRIMARY)
                        .row()
                        .add(Text("Повысить", {"cmd": "settings.PromocodesPanelEditUpLVLBuy"}), color=KeyboardButtonColor.POSITIVE)
                        .get_json()
                )
            )
    else:
        await message.answer('❌ Ошибка. У вас максимальный уровень промо-кода')
        await PromocodesPanelEditUpLVL(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Покупка повышения уровня
async def PromocodesPanelEditUpLVLBuy(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data_promocode = await database.getBdData('promo', 'creator_vk_id', f"'{message.from_id}'")
    data_user = await database.getUserData(message.from_id)
    if data_promocode[3] != 10:
        if data_user[20] >= 1000:

            if data_promocode[3] == 0:
                min_activation = 0
            if data_promocode[3] == 1:
                min_activation = 5
            if data_promocode[3] == 2:
                min_activation = 10
            if data_promocode[3] == 3:
                min_activation = 20
            if data_promocode[3] == 4:
                min_activation = 50
            if data_promocode[3] == 5:
                min_activation = 100
            if data_promocode[3] == 6:
                min_activation = 150
            if data_promocode[3] == 7:
                min_activation = 350
            if data_promocode[3] == 8:
                min_activation = 500
            if data_promocode[3] == 9:
                min_activation = 750

            if data_promocode[4] >= min_activation:
                new_lvl = data_promocode[3] + 1
                new_donate = data_user[20] - 1000
                await database.setUserData(message.from_id, 'donate', f"'{new_donate}'")
                await database.setBdData('promo', 'creator_vk_id', f"'{message.from_id}'", 'lvl', f"'{new_lvl}'")
                await message.answer('✅ Поздравляем вас с повышением промо-кода. Теперь люди, которые будут активировать ваш промокод, будут получать больше бонусов')
                await PromocodesPanelEditUpLVL(message, bot, api)
            else:
                await message.answer('❌ Ошибка.У вас недостаточно активаций промо-кода')
                await PromocodesPanelEditUpLVL(message, bot, api)
        else:
            await message.answer('❌ Ошибка. У вас недостаточно доната')
            await PromocodesPanelEditUpLVL(message, bot, api)
    else:
        await message.answer('❌ Ошибка. У вас максимальный уровень промо-кода')
        await PromocodesPanelEditUpLVL(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# ТОП 20 промокодов сервера
async def PromocodesPanelTOPServer(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'settings.PromocodesPanelTOPServer'")
    TOP_MONEY = await database.yourSQL('SELECT * FROM `promo` ORDER BY `activation_count` DESC LIMIT 20;')
    spisok = ''
    count = 1
    for row in TOP_MONEY:
        spisok = f'{spisok}\n{count}. {row[2]} — {row[4]} активаций'
        count = count + 1
    await message.answer(
        message=f"🎯 » ⚙ » 🎟 » 🎟 » 📈 Рейтинг промокодов сервера (топ 20)\n\n{spisok}",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "settings.PromocodesPanel"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Проверка на наличие промокода
async def PromocodesCheck(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    num = await database.findBaseDataSetting('promo', 'creator_vk_id', f"'{message.from_id}'")
    if num > 0:
        await PromocodesPanel(message, bot, api)
    else:
        await database.setUserData(message.from_id, 'state', "'settings.PromocodesCheck2'")
        await message.answer(
            message=f"🎯 » ⚙ » 🎟 » 🎟 Управление промокодом (Создание промокода)\n\n"
                    f"У вас пока-что нету собственного промокода!\n\n"
                    f"📝 Придумайте и введите промокод (без решетки и смайликов)",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "settings.Promocodes"}), color=KeyboardButtonColor.PRIMARY)
                    .get_json()
            )
        )

# ----------------------------------------------------------------------------------------------------------------------

# Проверка на наличие одинаковых промокодов
async def PromocodesCheck2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    if len(message.text) < 31:
        num = await database.findBaseDataSetting('promo', 'code', f"'#{message.text}'")
        if num == 0:
            await database.newDataInBase('promo', "creator_vk_id, code, lvl, activation_count", f"'{message.from_id}', '#{message.text}', '1', '0'")
            await message.answer('✅ Теперь вы владеете своим промокодом!')
            await Promocodes(message, bot, api)
        else:
            await message.answer('❌ Ошибка. Данный промокод уже существует')
            await PromocodesCheck(message, bot, api)
    else:
        await message.answer('❌ Ошибка. Длинна промокода не должна превышать 30 символов')
        await PromocodesCheck(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Ввод промокода
async def PromocodesEdit(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'settings.PromocodesEditCheck'")
    await message.answer(
        message=f"🎯 » ⚙ » 🎟 » 🎟 Ввести промо-код\n\n"
                f"📝 Введите промо-код",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "settings.Promocodes"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Активация промокода
async def PromocodesEditCheck(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    if len(message.text) < 100:
        num = await database.findBaseDataSetting('promo', 'code', f"'{message.text}'")
        if num > 0:
            data_promocode = await database.getBdData('promo', 'code', f"'{message.text}'")

            if data_promocode[3] == 1:
                min_lvl = 6
            if data_promocode[3] == 2:
                min_lvl = 6
            if data_promocode[3] == 3:
                min_lvl = 6
            if data_promocode[3] == 4:
                min_lvl = 6
            if data_promocode[3] == 5:
                min_lvl = 6
            if data_promocode[3] == 6:
                min_lvl = 6
            if data_promocode[3] == 7:
                min_lvl = 5
            if data_promocode[3] == 8:
                min_lvl = 5
            if data_promocode[3] == 9:
                min_lvl = 5
            if data_promocode[3] == 10:
                min_lvl = 4

            data_user = await database.getUserData(message.from_id)


            if data_user[6] >= min_lvl:
                if data_promocode[1] != message.from_id:
                    new_balance = data_user[12] + PROMOCODE_REWARD[data_promocode[3]]
                    new_data_promocode = data_promocode[4] + 1
                    await database.setUserData(message.from_id, 'dollars', f"'{new_balance}'")
                    await database.setUserData(message.from_id, 'promocode', f"'{message.text}'")
                    await database.setBdData('promo', 'id', f"'{data_promocode[0]}'", 'activation_count', f"'{new_data_promocode}'")
                    await message.answer(f'✅ Вы успешно активировали промо-код и получили {await database.pretty(PROMOCODE_REWARD[data_promocode[3]])} долларов (💵)')
                    await Promocodes(message, bot, api)
                else:
                    await message.answer(
                        f'❌ Ошибка. Вы пытаетесь активировать свой промокод, попробуйте другой')
                    await Promocodes(message, bot, api)
            else:
                await message.answer(f'❌ Ошибка. Вы не можете активировать данный промокод, так-как вам нужен {min_lvl} игровой уровень')
                await Promocodes(message, bot, api)
        else:
            await message.answer('❌ Ошибка. Данного промокода не существует!')
            await Promocodes(message, bot, api)
    else:
        await message.answer('❌ Ошибка. Данного промокода не существует!')
        await Promocodes(message, bot, api)


# ----------------------------------------------------------------------------------------------------------------------




# Компактное меню
async def reDesign(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'settings.reDesign'")
    data = await database.getUserData(message.from_id)
    if data[47] == 0:
        button = 'Включить компактный дизайн'
        status = '❌ Выключен'
    if data[47] == 1:
        button = 'Выключить компактный дизайн'
        status = '✅ Включен'
    await database.setUserData(message.from_id, 'state', "'settings.Show'")
    await message.answer(
        message=f"🎯 » ⚙ » 🗃 Компактный дизайн\n\n"
                f"🗃 Компактный дизайн » {status}\n\n"
                f"Если вы опытный игрок и уже понимаете, как работает главное меню, мы разработали специальное "
                f"компактное меню. Оно в два раза меньше по высоте и вмещает все основные настройки.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "settings.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text(f"{button}", {"cmd": "settings.reDesignSwitch"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Переключение компактного меню
async def reDesignSwitch(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[47] == 0:
        await database.setUserData(message.from_id, 'reDesign', "'1'")
        await message.answer(
            message=f"✅ Вы успешно обновили вид главного меню",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("👉🏻 Далее", {"cmd": "settings.reDesign"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("🎯 Перейти в главное меню", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    else:
        if data[47] == 1:
            await database.setUserData(message.from_id, 'reDesign', "'0'")
            await message.answer(
                message=f"✅ Вы успешно обновили вид главного меню",
                keyboard=(
                    Keyboard(one_time=True, inline=False)
                        .add(Text("👉🏻 Далее", {"cmd": "settings.reDesign"}), color=KeyboardButtonColor.SECONDARY)
                        .row()
                        .add(Text("🎯 Перейти в главное меню", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.SECONDARY)
                        .get_json()
                )
            )

# ----------------------------------------------------------------------------------------------------------------------

# Прикрепление почты к аккаунту
async def Email(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    await database.setUserData(message.from_id, 'state', "'settings.Email'")
    if data[4] == 'No email address':
        await message.answer(
            message=f"🎯 » ⚙ » ✉ Email\n\n"
                    f"❌ Почта не установлена\n\n"
                    f"ℹ Мы рекомендуем добавить электронную почту, так-как это дополнительно "
                    f"обезопасит ваш аккаут: на данную электронную почту мы будем отправлять "
                    f"сообщения о подозрительных действий с вашим аккаунтом.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "settings.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("✉ Добавить почту", {"cmd": "settings.addMail"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )
    else:
        await message.answer(
            message=f"🎯 » ⚙ » ✉ Email\n\n"
                    f"✉ Привязана почта » {data[4]}\n\n"
                    f"💬 На указанную электронную почту мы будем отправлять сообщения о "
                    f"подозрительных действий на вашем аккаунте. В случае, если вам надо поменять почту, "
                    f"нажмите на кнопку ниже.",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "settings.Show"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("✉ Изменить почту", {"cmd": "settings.editMail"}), color=KeyboardButtonColor.SECONDARY)
                    .get_json()
            )
        )

# ----------------------------------------------------------------------------------------------------------------------

# Добавление почты к аккаунту
async def addMail(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'settings.addMail_check'")
    await message.answer(
        message=f"🎯 » ⚙ » ✉ » ✉ Добавить почту\n\n"
                f"📝 Введите электронную почту",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "settings.Email"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Проверка почты на валидность
async def addMail_check(message: Message, bot: Bot, api: API):
    result = database.regularCheck('^(?!.*@.*@.*$)(?!.*@.*\-\-.*\..*$)(?!.*@.*\-\..*$)(?!.*@.*\-$)(.*@.+(\..{1,11})?)$', str(message.text))
    if result[0] == 1:
        await database.setUserData(message.from_id, 'mail', f"'{result[1]}'")
        await addMail_OK(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Ошибка. Такой почты не существует, либо вы ее написали неправильно"
        )
        await addMail(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Успешное добавление почты
async def addMail_OK(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'settings.addMail_OK'")
    await message.answer(
        message=f"✅ Вы успешно добавили почту.\n\n"
                f"⚠ Для максимальной безопасности, мы рекомендуем вам поставить двухфакторную аунтификацию от ВКонтакте. В случае, "
                f"если она у вас уже стоит, то беспокоится не надо",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Продолжить", {"cmd": "settings.Email"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Изменение почты
async def editMail(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'settings.editMail_check'")
    await message.answer(
        message=f"🎯 » ⚙ » ✉ » ✉ Изменить почту\n\n"
                f"📝 Введите новую электронную почту",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "settings.Email"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Проверка почты на валидность
async def editMail_check(message: Message, bot: Bot, api: API):
    result = await database.regularCheck('^(?!.*@.*@.*$)(?!.*@.*\-\-.*\..*$)(?!.*@.*\-\..*$)(?!.*@.*\-$)(.*@.+(\..{1,11})?)$', str(message.text))
    if result[0] == 1:
        await database.setUserData(message.from_id, 'mail', f"'{result[1]}'")
        await editMail_OK(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Ошибка. Такой почты не существует, либо вы ее написали неправильно"
        )
        await editMail(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Успешная смена почты
async def editMail_OK(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'settings.editMail_OK'")
    await message.answer(
        message=f"✅ Вы успешно изменили почту",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Продолжить", {"cmd": "settings.Email"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ---------------------------------------------------------------------------------------------------------------

# РАССЛЫКИ
async def Mailing(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await database.setUserData(message.from_id, 'state', "'settings.Mailing'")

    KEYBOARD_MAILING = Keyboard(one_time=True, inline=False)
    KEYBOARD_MAILING.add(Text("◀ Назад", {"cmd": "settings.Show"}), color=KeyboardButtonColor.PRIMARY)
    KEYBOARD_MAILING.row()
    temporary = str(data[41])
    if temporary != '❌ Не подписан':
        KEYBOARD_MAILING.add(Text("📮 Отписаться от рассылок проекта", {"cmd": "settings.MailingLeaveProject"}), color=KeyboardButtonColor.SECONDARY)
    else:
        KEYBOARD_MAILING.add(Text("📮 Подписаться на рассылки проекта", {"cmd": "settings.MailingAddProject"}), color=KeyboardButtonColor.SECONDARY)
    KEYBOARD_MAILING.row()
    temporary = str(data[42])
    if temporary != '❌ Не подписан':
        KEYBOARD_MAILING.add(Text("📮 Отписаться от рассылок сервера", {"cmd": "settings.MailingLeaveServer"}), color=KeyboardButtonColor.SECONDARY)
    else:
        KEYBOARD_MAILING.add(Text("📮 Подписаться на рассылки сервера", {"cmd": "settings.MailingAddServer"}), color=KeyboardButtonColor.SECONDARY)
    KEYBOARD_MAILING = KEYBOARD_MAILING.get_json()

    await message.answer(
        message=f"🎯 » ⚙ » 📬 Рассылки\n\n"
                f"📮 Рассылка с новостями проекта » {data[41]} » 💵 {await database.pretty(server_settings[14])}\n"
                f"📮 Рассылка с новостями сервера » {data[42]} » 💵 {await database.pretty(server_settings[15])}\n\n"
                f"💵 Мы платим за рассылки! Читайте новости нашего проекта и получайте гарантированное вознаграждение за это. Для того, "
                f"чтобы получить вознаграждение, вам необходимо нажать на специальную кнопку в рассылке и после чего вы получите деньги.\n"
                f"Кроме этого, в наших рассылках мы информируем наших игроков о грядущих обновляниях, а серверная рассылка позволяет "
                f"следить за новостями вашего сервера: мероприятия, РП-ситуации, наборы во фракции и многое другое.",
        keyboard=KEYBOARD_MAILING
    )



async def MailingLeaveProject(message: Message, bot: Bot, api: API):
    await database.setMultiUserData(message.from_id, "mailing_project = '❌ Не подписан', state = 'settings.MailingLeaveProject'")
    await message.answer(
        message=f"😭 Вы отписались от рассылки с новостями проекта\n\n"
                f"👉🏻 Теперь вы не будете получать вознаграждений от рассылок, так-как они к вам больше не поступают. "
                f"Если вы передумаете и решите снова подписаться на рассылки, то перейдите в раздел «Настройки персонажа» в "
                f"раздел «Рассылки».",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Продолжить", {"cmd": "settings.Mailing"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def MailingAddProject(message: Message, bot: Bot, api: API):
    await database.setMultiUserData(message.from_id, "mailing_project = '✅ Подписан', state = 'settings.MailingAddProject'")
    await message.answer(
        message=f"🎉 Вы подписались на новости проекта\n\nМы благодарим вас за подписку на рассылку новостей от проекта. В ней "
                f"мы рассказываем о будущих обновлениях, так и об актуальных. Никакой воды и рекламы, только все по делу. Также "
                f"мы предалгаем каждому нашему игроку, который подписался на новости, небольшой бонус. Узнать сумму бонуса "
                f"можно в «Настройки персонажа» в разделе «Рассылки»",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Продолжить", {"cmd": "settings.Mailing"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def MailingLeaveServer(message: Message, bot: Bot, api: API):
    await database.setMultiUserData(message.from_id, "mailing_server = '❌ Не подписан', state = 'settings.MailingLeaveServer'")
    await message.answer(
        message=f"😭 Вы отписались от рассылки с новостями сервера\n\n"
                f"👉🏻 Теперь вы не будете получать вознаграждений от рассылок, так-как они к вам больше не поступают. "
                f"Если вы передумаете и решите снова подписаться на рассылки, то перейдите в раздел «Настройки персонажа» в "
                f"раздел «Рассылки».",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Продолжить", {"cmd": "settings.Mailing"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



async def MailingAddServer(message: Message, bot: Bot, api: API):
    await database.setMultiUserData(message.from_id, "mailing_server = '✅ Подписан', state = 'settings.MailingAddServer'")
    await message.answer(
        message=f"🎉 Вы подписались на новости сервера\n\nМы благодарим вас за подписку на рассылку новостей от сервера. В ней "
                f"мы рассказываем о мероприятиях, новостях, наборах во фракции и различные РП-ситуации. Также "
                f"мы предалгаем каждому нашему игроку, который подписался на новости, небольшой бонус. Узнать сумму бонуса "
                f"можно в «Настройки персонажа» в разделе «Рассылки»",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("👉🏻 Продолжить", {"cmd": "settings.Mailing"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )