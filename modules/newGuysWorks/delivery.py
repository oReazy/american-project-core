
# Доставщик пиццы

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'delivery.Show'")
    data = await database.getUserData(message.from_id)
    if data[27] == 'Безработный' or data[27] != 'Доставщик пиццы':
        await message.answer(
            message=f"🍕 Доставщик\n\n"
                    f"👩‍🦰 У нас очень много заказов и нам очень нужны доставщики пиццы",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.newGuysWorks"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("💼 Устроиться на работу", {"cmd": "delivery.Getting"}), color=KeyboardButtonColor.POSITIVE)
                    .row()
                    .add(Text("📖 Информация по зарплатам", {"cmd": "delivery.Info1"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Информация о работе", {"cmd": "delivery.Info2"}), color=KeyboardButtonColor.SECONDARY)
            )
        )
    else:
        await message.answer(
            message=f"🍕 Доставщик\n\n"
                    f"👩‍🦰 {data[3]}, выходи скорее на смену. У нас завал по заказам и их пора развзить",
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("◀ Назад", {"cmd": "map.newGuysWorks"}), color=KeyboardButtonColor.PRIMARY)
                    .row()
                    .add(Text("⚒ Работать", {"cmd": "delivery.rab1_1"}), color=KeyboardButtonColor.POSITIVE)
                    .row()
                    .add(Text("💼 Уволиться", {"cmd": "delivery.Leave"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Информация по зарплатам", {"cmd": "delivery.Info1"}), color=KeyboardButtonColor.SECONDARY)
                    .row()
                    .add(Text("📖 Информация о работе", {"cmd": "delivery.Info2"}), color=KeyboardButtonColor.SECONDARY)
            )
        )


async def Getting(message: Message, bot: Bot, api: API):
    datauser = await database.getUserData(message.from_id)
    data = ast.literal_eval(datauser[24])
    data = list(data)
    if data[1] == "✅ Имеется":
        if datauser[43] == '✅ Имеется':
            await database.setUserData(message.from_id, 'work', "'Доставщик пиццы'")
            await message.answer(
                message=f"✅ Вы успешно устроились на работу доставщика пиццы"
                )
            await Show(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Вы не можете работать доставщиком пиццы\n\n"
                        f"— Вам нужна банковская карта"
            )
            await Show(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Вы не можете работать доставщиком пиццы\n\n"
                    f"— Вам нужна лицензия на мотоциклы"
        )
        await Show(message, bot, api)


async def Leave(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'work', "'Безработный'")
    await message.answer(
        message=f"✅ Вы успешно уволились с работы"
        )
    await Show(message, bot, api)


async def Info1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'delivery.Info1'")
    await message.answer(
        message=f"🍕 » 📖 Информация по зарплатам\n\n"
                f"🛵 За одну успешную доставку вам заплатят » 150 долларов (💵)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "delivery.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )



async def Info2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'delivery.Info2'")
    await message.answer(
        message=f"🍕 » 📖 Информация о работе\n\n"
                f"Вы любите сочную, вкусную и ароматную пиццу? Тогда пиццерия «BOBO пицца» вам точно понравится!\n\n"
                f"У нас есть множество пицц на выбор, но вы, как работник ее не выбираете, а доставляете. Для начала "
                f"вам необходимо получить заказ на пиццу, забираем ее в пиццерии и доставляем покупателю.\n\n"
                f"Работая у нас, вы получаете стабильную и гарантированную зарплату.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "delivery.Show"}), color=KeyboardButtonColor.PRIMARY)
        )
    )

# ---------------------------------------------------------------------------------------------------------


async def rab1_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_1'")
    await database.setUserData(message.from_id, 'temporary_var', f"'0'")
    await message.answer(
        message=f"🚶🏻 Зайдите в ресторан BOBO пиццы",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶🏻 Зайдите в ресторан BOBO пиццы", {"cmd": "delivery.rab1_2"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🚶🏻 Вы вошли в ресторан')
    await asyncio.sleep(2)
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_2'")
    await message.answer(
        message=f"🔑 Возьмите в служебном кабинете ключи от мопеда",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔑 Взять ключи от мопеда", {"cmd": "delivery.rab1_3"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🔑 Вы взяли ключи от мопеда')
    await asyncio.sleep(2)
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_3'")
    await message.answer(
        message=f"📱 Включите приложение доставки, чтобы начать отслеживать доступные заказы",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("📱 Включить приложение", {"cmd": "delivery.rab1_4"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('📱 Вы включили приложение')
    await asyncio.sleep(2)
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_4'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"📱 Приложение » Здравствуйте, {data[3]}. Перед тем, чтобы начать развозить пиццу, вы должны сделать фото-отчет себя.Сделайте селфи себя и пришлите его нам. ",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("📷 Сделать селфи", {"cmd": "delivery.rab1_5"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_5(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('📷 Вы сделали селфи и отправили его на проверку...')
    await asyncio.sleep(5)
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_5'")
    await message.answer(
        message=f"📱 Приложение » Вы прошли фото-проверку. Теперь вы можете брать доступные заказы!"
    )
    await message.answer(
        message=f"📱 Приложение » В данный момент доступны следующие заказы\n\n"
                f"🍕 {int(random.randint(1, 7))} пицца(ы) — 🗺 {int(random.randint(1, 20))} км.\n"
                f"🍕 {int(random.randint(1, 7))} пицца(ы) — 🗺 {int(random.randint(1, 20))} км.\n"
                f"🍕 {int(random.randint(1, 7))} пицца(ы) — 🗺 {int(random.randint(1, 20))} км.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🍕 Взять первый заказ", {"cmd": "delivery.rab1_6"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🍕 Взять второй заказ", {"cmd": "delivery.rab1_6"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🍕 Взять третий заказ", {"cmd": "delivery.rab1_6"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("❌ Закончить смену", {"cmd": "delivery.rab1_end1_1"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_6(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('✅ Вы приняли данный заказ')
    await asyncio.sleep(2)
    await message.answer('📱 Приложение » Вы приняли заказ. Дождитесь, когда его приготовят.')
    await asyncio.sleep(int(random.randint(15, 30)))
    await message.answer('📱 Приложение » Статус готовности заказа изменен.')
    await asyncio.sleep(2)
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_6'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🧑 Работник BOBO Pizza » Доставка #{int(random.randint(1000,9999))} готова к выдаче",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("💬 Спасибо", {"cmd": "delivery.rab1_6_1"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💬 Благодарю", {"cmd": "delivery.rab1_6_1"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💬 Вы все положили?", {"cmd": "delivery.rab1_6_2"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💬 Горячая пицца?", {"cmd": "delivery.rab1_6_3"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💬 Что-то вы медленно", {"cmd": "delivery.rab1_6_4"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_6_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_6_1'")
    await message.answer(
        message=f"🧑 Работник BOBO Pizza » Хорошей доставки. Заберите заказ",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🍕 Взять заказ", {"cmd": "delivery.rab1_7"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_6_2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_6_2'")
    await message.answer(
        message=f"🧑 Работник BOBO Pizza » Да, мы проверили все и все положили. Заберите заказ",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🍕 Взять заказ", {"cmd": "delivery.rab1_7"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_6_3(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_6_3'")
    await message.answer(
        message=f"🧑 Работник BOBO Pizza » У нас всегда горячая пицца. Если вы быстро ее доставите, то она все еще будет горячей. Заберите заказ",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🍕 Взять заказ", {"cmd": "delivery.rab1_7"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_6_4(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_6_4'")
    await message.answer(
        message=f"🧑 Работник BOBO Pizza » Простите, но у нас есть другие заказы, которые необходимо делать. Заберите заказ",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🍕 Взять заказ", {"cmd": "delivery.rab1_7"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_7(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🍕 Вы забрали заказ и положили его в термосумку')
    await asyncio.sleep(3)
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_7'")
    await message.answer(
        message=f"🛵 Вы завели мопед. Едьте на адрес клиента",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🛵 Поехать на адрес клиента", {"cmd": "delivery.rab1_8"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_8(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🛵 Вы завели мопед и поехали на адрес клиента')
    await asyncio.sleep(int(random.randint(15,50)))
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_8'")
    await message.answer(
        message=f"🛵 Вы подъехали к месту, куда надо доставить пиццу. Заходите в подъезд",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚪 Зайти в подъезд", {"cmd": "delivery.rab1_9"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_9(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🚪 Вы зашли в подъезд')
    await asyncio.sleep(2)
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_9'")
    await message.answer(
        message=f"⚪ Вызовите лифт, чтобы подняться до необходимого этажа",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔴 Вызвать лифт", {"cmd": "delivery.rab1_10"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_10(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🔴 Вы вызвали лифт')
    await asyncio.sleep(2)
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_10'")
    await message.answer(
        message=f"🚶🏻 Лифт приехал. Заходите в него и выберите этаж",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶🏻 Зайти в лифт и выбрать этаж", {"cmd": "delivery.rab1_11"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_11(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🚶🏻 Вы зашли в лифт и выбрали этаж')
    await asyncio.sleep(2)
    await message.answer('🔴 Двери лифта закрылись и вы едете на выбранный этаж...')
    await asyncio.sleep(7)
    await message.answer('🔴 Вы поднялись на свой этаж, двери лифта открываются')
    await asyncio.sleep(3)
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_10'")
    await message.answer(
        message=f"👤 Клиент » Спасибо за доставку. Благодарю",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🍕 Отдать пиццу", {"cmd": "delivery.rab1_12"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_12(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🍕 Вы отдали заказ клиенту')
    await asyncio.sleep(2)
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_12'")
    await message.answer(
        message=f"⚪ Вызовите лифт, чтобы спуститься на первый этаж",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔴 Вызвать лифт", {"cmd": "delivery.rab1_13"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_13(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🔴 Двери лифта открылись')
    await asyncio.sleep(2)
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_13'")
    await message.answer(
        message=f"🚶🏻 Зайдите в лифт",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶🏻 Зайти в лифт", {"cmd": "delivery.rab1_14"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_14(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🚶🏻 Вы зашли в лифт')
    await asyncio.sleep(2)
    await message.answer('🔴 Вы выбрали первый этаж и двери лифта закрылись')
    await asyncio.sleep(10)
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_14'")
    await message.answer(
        message=f"🔴 Вы спустились на первый этаж, двери лифта открылись",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🚶🏻 Выйти из лифта", {"cmd": "delivery.rab1_15"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_15(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🚶🏻 Вы вышли из лифта')
    await asyncio.sleep(2)
    await message.answer('🚶🏻 Вы вышли из подъезда')
    await asyncio.sleep(3)
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_15'")
    await message.answer(
        message=f"🛵 Вы завели мопед. Возвращаетесь в пиццерию",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🛵 Вернуться в пиццерию", {"cmd": "delivery.rab1_16"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_16(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer('🛵 Вы возвращаетесь в пиццерию...')
    await asyncio.sleep(random.randint(15,50))
    await message.answer('🛵 Вы вернулись в пиццерию')
    await asyncio.sleep(3)
    random_num = int(random.randint(1,3))
    if random_num == 1: stars = 'Отлично'
    if random_num == 2: stars = 'Хорошо'
    if random_num == 3: stars = 'Средне'
    await message.answer(f'📱 Приложение » Клиент поставил вам оценку: {stars}')
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_17'")
    await message.answer(
        message=f"📱 Приложение » Доступны новые заказы! Посмотрите",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("📱 Посмотреть новые заказы", {"cmd": "delivery.rab1_17"}), color=KeyboardButtonColor.SECONDARY)
        )
    )



async def rab1_17(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    data = await database.getUserData(message.from_id)
    new_data = int(data[44]) + 1
    await database.setMultiUserData(message.from_id, f"temporary_var = '{new_data}'")

    await rab1_18(message, bot, api)


async def rab1_18(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_18'")
    await message.answer(
        message=f"📱 Приложение » Вы прошли фото-проверку. Теперь вы можете брать доступные заказы!"
    )
    await message.answer(
        message=f"📱 Приложение » В данный момент доступны следующие заказы\n\n"
                f"🍕 {int(random.randint(1, 7))} пицца(ы) — 🗺 {int(random.randint(1, 20))} км.\n"
                f"🍕 {int(random.randint(1, 7))} пицца(ы) — 🗺 {int(random.randint(1, 20))} км.\n"
                f"🍕 {int(random.randint(1, 7))} пицца(ы) — 🗺 {int(random.randint(1, 20))} км.",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🍕 Взять первый заказ", {"cmd": "delivery.rab1_6"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🍕 Взять второй заказ", {"cmd": "delivery.rab1_6"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🍕 Взять третий заказ", {"cmd": "delivery.rab1_6"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("❌ Закончить смену", {"cmd": "delivery.rab1_end2_1"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_end1_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_end1_1'")
    await message.answer(
        message=f"🔑 Вы решили закончить смену. Верните ключи в служебный кабинет",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔑 Вернуть ключи", {"cmd": "delivery.rab1_end1_2"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_end1_2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🔑 Вы возвращаете ключи в служебный кабинет..."
    )
    await asyncio.sleep(3)
    await message.answer(
        message=f"🔑 Вы вернули ключи"
    )
    await asyncio.sleep(3)
    await Show(message, bot, api)



async def rab1_end2_1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'delivery.rab1_end2_1'")
    await message.answer(
        message=f"🔑 Вы решили закончить смену. Верните ключи в служебный кабинет",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("🔑 Вернуть ключи", {"cmd": "delivery.rab1_end2_2"}), color=KeyboardButtonColor.SECONDARY)
        )
    )


async def rab1_end2_2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'block.Show'")
    await message.answer(
        message=f"🔑 Вы возвращаете ключи в служебный кабинет..."
    )
    await asyncio.sleep(3)
    await message.answer(
        message=f"🔑 Вы вернули ключи"
    )
    await asyncio.sleep(3)

    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    zarplata = int(data[44]) * 150 * server_settings[26]
    itog = int(data[16]) + zarplata

    await database.setUserData(message.from_id, 'bank_dollars', f"'{itog}'")

    await message.answer(
        message=f"📱 Приложение » Поздравляем! Вы заработали {zarplata} долларов (💵).\n\nМы уже перевели эти деньги на ваш банковский счет (🏦)"
    )
    await Show(message, bot, api)