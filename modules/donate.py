
# Донат

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

# Главная страница с донатом
async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Show'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 Донат\n\n"
                f'На данной странице вы можете узнать номер своего аккаунта, а также узнать текущее состояние '
                f'вашего доната. Чтобы воспользоваться донатом, нажмите на кнопку «Заказать». Если вам необходимо '
                f'пополнить счет, то нажмите на кнопку «Пополнить счет»\n\n'
                f'🆔 Номер вашего аккаунта » {data[0]}\n'
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🛍 Заказать", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.POSITIVE)
                .add(Text("➕ Пополнить счет", {"cmd": "donate.Show_ADD"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Меню пополнения доната
async def Show_ADD(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Show'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » ➕ Пополнить счет\n\n"
                f'Пополнить счет игрового аккаунта можно с помощью разных способов. Выберите самый удобный и подходящий для вас.',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Show"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Страница с донатом (первая страница)
async def ShopMenu1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.ShopMenu1'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 Заказать\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "donate.ShopMenu2"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("👑 VIP", {"cmd": "donate.VIP"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("💵 Получить доллары", {"cmd": "donate.Dollars"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 Эксклюзивный телефон", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👕 Эксклюзивная одежда", {"cmd": "donate.clothes"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📝 Сменить ник", {"cmd": "donate.ChangeNick"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌐 Купить очки опыта", {"cmd": "donate.EXP"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📄 Получить все лицензии", {"cmd": "donate.Licences"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )



# Страница с донатом (вторая страница)
async def ShopMenu2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.ShopMenu2'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 Заказать\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌽 Навык фермера", {"cmd": "donate.SkillFarmer"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🚚 Навык дальнобойщика", {"cmd": "donate.SkillTruck"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🚕 Навык таксиста", {"cmd": "donate.SkillTaxi"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📦 Коробки", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🅰️ Снять варн", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Покупка VIP
async def VIP(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.VIP'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 👑 VIP\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n\n'
                f'📄 VIP — уникальная возможность получить дополнительные привелегии. У нас есть множество вариантов VIP и возможно один из них вам подойдет.',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("💎 VIP PREMIUM", {"cmd": "donate.VIPPremium"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🥇 VIP Gold", {"cmd": "donate.VIPGold"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🥈 VIP Silver", {"cmd": "donate.VIPSilver"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🥉 VIP Bronze", {"cmd": "donate.VIPBronze"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Информация о VIP Premium
async def VIPPremium(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.VIPPremium'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 👑 » 💎 VIP PREMIUM\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'🛍 Цена » 3000 💎\n'
                f'⏰ Срок действия VIP » Выдается навсегда\n\n'
                f'💎 VIP PREMIUM — самая лучшая подписка на нашем сервере. С помощью данной подписки вы получаете самое большое количество бонусов на нашем сервере:\n\n'
                f'⚠ В РАЗРАБОТКЕ',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.VIP"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.VIPPremiumCheck"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )


# Информация о VIP Gold
async def VIPGold(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.VIPGold'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 👑 » 🥇 VIP Gold\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'🛍 Цена » 1500 💎\n'
                f'⏰ Срок действия VIP » Выдается навсегда\n\n'
                f'🥇 VIP Gold — универсальная VIP, которая включает в себе все бонусы из Bronze и Silver, однако дополняет своими:\n\n'
                f'⚠ В РАЗРАБОТКЕ',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.VIP"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.VIPGoldCheck"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )


# Информация о VIP Silver
async def VIPSilver(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.VIPSilver'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 👑 » 🥈 VIP Silver\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'🛍 Цена » 499 💎\n'
                f'⏰ Срок действия VIP » Выдается навсегда\n\n'
                f'🥈 VIP Silver — отличная VIP для игры на нашем проекте. Покупая данную VIP вы получаете следующие бонусы:\n\n'
                f'⚠ В РАЗРАБОТКЕ',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.VIP"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.VIPSilverCheck"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )


# Информация о VIP Bronze
async def VIPBronze(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.VIPBronze'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 👑 » 🥉 VIP Bronze\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'🛍 Цена » 199 💎\n'
                f'⏰ Срок действия VIP » Выдается на 30 дней\n\n'
                f'🥉 VIP Bronze — подойдет для новичков, чтобы быстро развиться на сервере:\n\n'
                f'⚠ В РАЗРАБОТКЕ',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.VIP"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.VIPBronzeCheck"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Покупка VIP Premium
async def VIPPremiumCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 3000:
        vip_data = ast.literal_eval(data[21])
        vip_data = list(vip_data)
        vip_data[0] = 'PREMIUM'
        vip_data[1] = 10
        new_donate = int(data[20]) - 3000
        await database.setMultiUserData(message.from_id, f'donate = "{new_donate}", VIP = "{vip_data}"')
        await message.answer(
            message=f'✅ Вы успешно купили VIP PREMIUM (навсегда)',
        )
        await VIPPremium(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await VIPPremium(message, bot, api)


# Покупка VIP Gold
async def VIPGoldCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 1500:
        vip_data = ast.literal_eval(data[21])
        vip_data = list(vip_data)
        vip_data[0] = 'Gold'
        vip_data[1] = 10
        new_donate = int(data[20]) - 1500
        await database.setMultiUserData(message.from_id, f'donate = "{new_donate}", VIP = "{vip_data}"')
        await message.answer(
            message=f'✅ Вы успешно купили VIP Gold (навсегда)',
        )
        await VIPGold(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await VIPGold(message, bot, api)


# Покупка VIP Silver
async def VIPSilverCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 499:
        vip_data = ast.literal_eval(data[21])
        vip_data = list(vip_data)
        vip_data[0] = 'Silver'
        vip_data[1] = 10
        new_donate = int(data[20]) - 499
        await database.setMultiUserData(message.from_id, f'donate = "{new_donate}", VIP = "{vip_data}"')
        await message.answer(
            message=f'✅ Вы успешно купили VIP Silver (навсегда)',
        )
        await VIPSilver(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await VIPSilver(message, bot, api)


# Покупка VIP Bronze
async def VIPBronzeCheck(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 199:
        vip_data = ast.literal_eval(data[21])
        vip_data = list(vip_data)
        vip_data[0] = 'Bronze'
        vip_data[1] = int(time.time()) + 2592000
        new_donate = int(data[20]) - 199
        await database.setMultiUserData(message.from_id, f'donate = "{new_donate}", VIP = "{vip_data}"')
        await message.answer(
            message=f'✅ Вы успешно купили VIP Bronze (на 30 дней)',
        )
        await VIPBronze(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await VIPBronze(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Смена ника
async def ChangeNick(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.ChangeNick'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📝 Сменить ник\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'🛍 Цена » 30 💎\n\n'
                f'📄 Купив данную услугу, вы сможете поменять себе ник. Главной особенностью данной услуги является то, что вы сможете поставить ник длинной от 3 до 30 символов!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Поменять ник", {"cmd": "donate.ChangeNickGet"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Процесс смены ника
async def ChangeNickGet(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if int(data[20]) >= 30:
        await database.setUserData(message.from_id, 'state', "'donate.ChangeNickGetCheck'")
        await message.answer(
            message=f'✏ Напишите новый желаемый ник от 3 до 30 символов',
            keyboard=(
                Keyboard(one_time=True, inline=False)
                    .add(Text("Отменить", {"cmd": "donate.ChangeNick"}), color=KeyboardButtonColor.PRIMARY)
                    .get_json()
            )
        )
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для смены ника',
        )
        await ChangeNick(message, bot, api)


# Изменение ника
async def ChangeNickGetCheck(message: Message, bot: Bot, api: API):
    if 3 <= len(message.text) <= 30:
        if await database.findBaseData('nick', f"'{message.text}'") == 0:
            data = await database.getUserData(message.from_id)
            info = ast.literal_eval(data[33])
            info = list(info)
            info.append(f'{data[3]}')
            new_donate = int(data[20]) - 30
            await database.setMultiUserData(message.from_id, f'donate = "{new_donate}", nick = "{message.text}", history_nicks = "{info}"')
            await message.answer(
                message='✅ Вы успешно поменяли себе ник'
            )
            await ChangeNick(message, bot, api)
        else:
            await message.answer(
                message='❌ Ошибка. Данный ник уже занят. Попробуйте другой'
            )
            await ChangeNickGet(message, bot, api)
    else:
        await message.answer(
            message=f'❌ Ошибка. Вы ввели либо короткий ник, либо слишком длинный.'
        )
        await ChangeNickGet(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Информация о навыке таксиста
async def SkillTaxi(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.SkillTaxi'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 🚕 Навык таксиста\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'🛍 Цена » 100 💎\n\n'
                f'📄 Купив данную услугу, вы получаете максимальный навык таксиста. Это означает, что вы сможете получать больше денег за работу.',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu2"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.SkillTaxiBuy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )

# Информация о навыке дальнобойщика
async def SkillTruck(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.SkillTruck'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 🚚 Навык дальнобойщика\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'🛍 Цена » 250 💎\n\n'
                f'📄 Купив данную услугу, вы получаете максимальный навык дальнобойщика. Это означает, что вы сможете получать больше денег за работу.',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu2"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.SkillTruckBuy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )

# Информация о навыке фермера
async def SkillFarmer(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.SkillFarmer'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 🌽 Навык фермера\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'🛍 Цена » 150 💎\n\n'
                f'📄 Купив данную услугу, вы получаете максимальный навык фермера. Это означает, что вы сможете работать на любой должности фермы',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu2"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.SkillFarmerBuy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )


# ----------------------------------------------------------------------------------------------------------------------

# Покупка скиллов такси
async def SkillTaxiBuy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 100:
        skills = ast.literal_eval(data[30])
        skills = list(skills)
        skills[3] = 10000
        new_donate = int(data[20]) - 100
        await database.setMultiUserData(message.from_id, f'donate = "{new_donate}", skillWorks = "{skills}"')
        await message.answer(
            message=f'✅ Вы успешно купили максимальный навык таксиста',
        )
        await SkillTaxi(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await SkillTaxi(message, bot, api)

# Покупка скиллов дальнобойщика
async def SkillTruckBuy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 250:
        skills = ast.literal_eval(data[30])
        skills = list(skills)
        skills[2] = 5000
        new_donate = int(data[20]) - 250
        await database.setMultiUserData(message.from_id, f'donate = "{new_donate}", skillWorks = "{skills}"')
        await message.answer(
            message=f'✅ Вы успешно купили максимальный навык дальнобойщика',
        )
        await SkillTruck(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await SkillTruck(message, bot, api)


# Покупка скиллов фермера
async def SkillFarmerBuy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 150:
        skills = ast.literal_eval(data[30])
        skills = list(skills)
        skills[0] = 7500
        new_donate = int(data[20]) - 150
        await database.setMultiUserData(message.from_id, f'donate = "{new_donate}", skillWorks = "{skills}"')
        await message.answer(
            message=f'✅ Вы успешно купили максимальный навык фермера',
        )
        await SkillFarmer(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await SkillFarmer(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Все лицензии
async def Licences(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Licences'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📄 Получить все лицензии\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'🛍 Цена » 250 💎\n\n'
                f'📄 Купив данную услугу, вы получаете все виды лицензий.',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.LicencesBuy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

# Покупка всех лицензий
async def LicencesBuy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 250:
        skills = ast.literal_eval(data[24])
        skills = list(skills)
        skills[0] = '✅ Имеется'
        skills[1] = '✅ Имеется'
        skills[2] = '✅ Имеется'
        skills[3] = '✅ Имеется'
        skills[4] = '✅ Имеется'
        skills[5] = '✅ Имеется'
        skills[6] = '✅ Имеется'
        skills[7] = '✅ Имеется'
        new_donate = int(data[20]) - 250
        await database.setMultiUserData(message.from_id, f'donate = "{new_donate}", license = "{skills}"')
        await message.answer(
            message=f'✅ Вы успешно купили все лицензии',
        )
        await Licences(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Licences(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Очки EXP
async def EXP(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.EXP'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 🌐 Купить очки опыта\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'📊 Курс обмена » 1 очко опыта (🌐) = {await database.pretty(server_settings[22])} 💎\n\n'
                f'📄 Воспользовавшись данной услугой, вы можете получить неограниченное количество очков опыта. Очки опыта необходимы для повышения вас на новый уровень.',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Получить очки опыта", {"cmd": "donate.EXPGet"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )

# Ввод количества очков EXP
async def EXPGet(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.EXPGetCheck'")
    await message.answer(
        message=f'✏ Напишите, сколько доната вы готовы потратить',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отменить", {"cmd": "donate.EXP"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )

# Проверка, хватает ли доната на количество очков опыта
async def EXPGetCheck(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.EXPGetCheck'")
    if message.text.isdigit():
        money = int(message.text)
        if 1 <= money <= 999999999:
            data = await database.getUserData(message.from_id)
            server_settings = await database.getBdData('settings', 'id', "'1'")
            await database.setMultiUserData(message.from_id, f"temporary_var = '{message.text}'")
            if int(data[20]) >= int(int(message.text) * int(server_settings[22])):
                await message.answer(
                    message=f'⚠ Подтвердите действие\n\n'
                            f'Вы действительно хотите получить {await database.pretty(message.text)} очков опыта (🌐) за {await database.pretty(int(message.text) * int(server_settings[22]))} алмазов 💎',
                    keyboard=(
                        Keyboard(one_time=True, inline=False)
                            .add(Text("Подтверждаю", {"cmd": "donate.EXPGetCheckOK"}), color=KeyboardButtonColor.POSITIVE)
                            .row()
                            .add(Text("❌ Отказываюсь", {"cmd": "donate.EXP"}), color=KeyboardButtonColor.SECONDARY)
                            .get_json()
                    )
                )
            else:
                await message.answer(
                    message=f"❌ У вас нет столько алмазов"
                )
                await EXPGet(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Введите число от 1 до 999 999 999"
            )
            await EXPGet(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Введите корректное число"
        )
        await EXPGet(message, bot, api)

# Вывод об успешной транзакции
async def EXPGetCheckOK(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    new_donate = int(data[20]) - int(int(data[44]) * int(server_settings[22]))
    new_exp = int(data[7]) + int(int(data[44]))
    await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', exp = '{new_exp}'")
    await message.answer(
        message=f'✅ Транзакция успешно проведена.',
    )
    data = await database.getUserData(message.from_id)
    if new_exp >= (data[6] * server_settings[20]):
        await database.def_new_lvl(message, bot, api, data, server_settings)
    await EXP(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Меню покупки долларов
async def Dollars(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Dollars'")
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 💵 Получить доллары\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'💵 Долларов на руках » {await database.pretty(data[12])}\n\n'
                f'📊 Курс обмена » 1 💎 = {await database.pretty(server_settings[23])} долларов (💵)\n\n'
                f'📄 Воспользовавшись данной услугой, вы можете получить неограниченное количество долларов в обмен на донат. С помощью долларов вы можете покупать внутриигровые предметы, а также взаимодействовать с другими игроками',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Получить доллары", {"cmd": "donate.DollarsGet"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )

# Ввод количества доната
async def DollarsGet(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.DollarsGetCheck'")
    await message.answer(
        message=f'✏ Напишите, сколько доната вы готовы потратить',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("Отменить", {"cmd": "donate.Dollars"}), color=KeyboardButtonColor.PRIMARY)
                .get_json()
        )
    )

# Проверка, хватает ли доната и подтверждение обмена
async def DollarsGetCheck(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.DollarsGetCheck'")
    if message.text.isdigit():
        money = int(message.text)
        if 1 <= money <= 999999999:
            data = await database.getUserData(message.from_id)
            server_settings = await database.getBdData('settings', 'id', "'1'")
            await database.setMultiUserData(message.from_id, f"temporary_var = '{message.text}'")
            if int(data[20]) >= int(message.text):
                await message.answer(
                    message=f'⚠ Подтвердите действие\n\n'
                            f'Вы действительно хотите потратить {await database.pretty(message.text)} алмазов (💎) в обмен на {await database.pretty(int(message.text) * int(server_settings[23]))} игровых доллара (💵)',
                    keyboard=(
                        Keyboard(one_time=True, inline=False)
                            .add(Text("Подтверждаю", {"cmd": "donate.DollarsGetCheckOK"}), color=KeyboardButtonColor.POSITIVE)
                            .row()
                            .add(Text("❌ Отказываюсь", {"cmd": "donate.Dollars"}), color=KeyboardButtonColor.SECONDARY)
                            .get_json()
                    )
                )
            else:
                await message.answer(
                    message=f"❌ У вас нет столько алмазов"
                )
                await DollarsGet(message, bot, api)
        else:
            await message.answer(
                message=f"❌ Введите число от 1 до 999 999 999"
            )
            await DollarsGet(message, bot, api)
    else:
        await message.answer(
            message=f"❌ Введите корректное число"
        )
        await DollarsGet(message, bot, api)

# Успешный обмен
async def DollarsGetCheckOK(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    server_settings = await database.getBdData('settings', 'id', "'1'")
    new_donate = int(data[20]) - int(data[44])
    new_dollars = int(data[12]) + int(int(data[44]) * int(server_settings[23]))
    await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', dollars = '{new_dollars}'")
    await message.answer(
        message=f'✅ Транзакция успешно проведена.',
    )
    await Dollars(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

# Покупка телефона
async def Telephone(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 Эксклюзивный телефон\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'📱 Ваш текущий телефон » {data[5]}\n\n'
                f'📱 iPhone 13 » 500 алмазов 💎\n'
                f'📱 iPhone 12 » 450 алмазов 💎\n'
                f'📱 iPhone 11 » 400 алмазов 💎\n'
                f'📱 SAMSUNG Galaxy S21 » 350 алмазов 💎\n'
                f'📱 SAMSUNG Galaxy A72 » 250 алмазов 💎\n'
                f'📱 SAMSUNG Galaxy S20 » 200 алмазов 💎\n'
                f'📱 Xiaomi Mi 11 Lite » 150 алмазов 💎\n'
                f'📱 Xiaomi Redmi Note 10 Pro » 100 алмазов 💎\n'
                f'📱 Xiaomi Redmi Note 8 Pro » 50 алмазов 💎\n\n'
                f'📄 Воспользовавшись данной услугой, вы обмениваете донат на эксклюзивный телефон. Вы его сможете продать/обменять другому игроку, однако в игровом мире его нельзя получить за доллары, евро, иены или фунты.\n'
                f'Покупая эксклюзивные телефоны, вы получаете дополнительные приложения в телефон, которые доступны только на этих моделях',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("📱 iPhone 13", {"cmd": "donate.Telephone_iPhone13"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 iPhone 12", {"cmd": "donate.Telephone_iPhone12"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 iPhone 11", {"cmd": "donate.Telephone_iPhone11"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 SAMSUNG Galaxy S21", {"cmd": "donate.Telephone_SamsungS21"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 SAMSUNG Galaxy A72", {"cmd": "donate.Telephone_SamsungA72"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 SAMSUNG Galaxy S20", {"cmd": "donate.Telephone_SamsungS20"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 Xiaomi Mi 11 Lite", {"cmd": "donate.Telephone_Xiaomi11Lite"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 Xiaomi Redmi Note 10 Pro", {"cmd": "donate.Telephone_Xiaomi10Pro"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📱 Xiaomi Redmi Note 8 Pro", {"cmd": "donate.Telephone_Xiaomi8Pro"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

async def Telephone_Xiaomi8Pro(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_Xiaomi8Pro'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 Xiaomi Redmi Note 8 Pro\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'⚠ Вы действительно хотите купить Xiaomi Redmi Note 8 Pro за 50 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_Xiaomi8Pro_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )


async def Telephone_Xiaomi8Pro_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 50:
        new_donate = int(data[20]) - 50
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'Xiaomi Redmi Note 8 Pro'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_Xiaomi8Pro(message, bot, api)



async def Telephone_Xiaomi10Pro(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_Xiaomi10Pro'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 Xiaomi Redmi Note 10 Pro\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'⚠ Вы действительно хотите купить Xiaomi Redmi Note 10 Pro за 100 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_Xiaomi10Pro_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )


async def Telephone_Xiaomi10Pro_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 100:
        new_donate = int(data[20]) - 100
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'Xiaomi Redmi Note 10 Pro'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_Xiaomi10Pro(message, bot, api)





async def Telephone_Xiaomi11Lite(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_Xiaomi11Lite'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 Xiaomi Mi 11 Lite\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'⚠ Вы действительно хотите купить Xiaomi Mi 11 Lite за 150 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_Xiaomi11Lite_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )


async def Telephone_Xiaomi11Lite_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 150:
        new_donate = int(data[20]) - 150
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'Xiaomi Mi 11 Lite'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_Xiaomi11Lite(message, bot, api)



async def Telephone_SamsungS20(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_SamsungS20'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 SAMSUNG Galaxy S20\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'⚠ Вы действительно хотите купить SAMSUNG Galaxy S20 за 200 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_SamsungS20_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )


async def Telephone_SamsungS20_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 200:
        new_donate = int(data[20]) - 200
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'SAMSUNG Galaxy S20'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_SamsungS20(message, bot, api)




async def Telephone_SamsungA72(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_SamsungA72'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 SAMSUNG Galaxy A72\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'⚠ Вы действительно хотите купить SAMSUNG Galaxy A72 за 250 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_SamsungA72_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )


async def Telephone_SamsungA72_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 250:
        new_donate = int(data[20]) - 250
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'SAMSUNG Galaxy A72'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_SamsungA72(message, bot, api)



async def Telephone_SamsungS21(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_SamsungS21'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 SAMSUNG Galaxy S21\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'⚠ Вы действительно хотите купить SAMSUNG Galaxy S21 за 350 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_SamsungS21_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )


async def Telephone_SamsungS21_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 350:
        new_donate = int(data[20]) - 350
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'SAMSUNG Galaxy S21'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_SamsungS21(message, bot, api)




async def Telephone_iPhone11(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_iPhone11'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 iPhone 11\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'⚠ Вы действительно хотите купить iPhone 11 за 400 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_iPhone11_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )


async def Telephone_iPhone11_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 400:
        new_donate = int(data[20]) - 400
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'iPhone 11'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_iPhone11(message, bot, api)


async def Telephone_iPhone12(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_iPhone12'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 iPhone 12\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'⚠ Вы действительно хотите купить iPhone 12 за 500 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_iPhone12_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )


async def Telephone_iPhone12_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 450:
        new_donate = int(data[20]) - 450
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'iPhone 12'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_iPhone12(message, bot, api)




async def Telephone_iPhone13(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.Telephone_iPhone13'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 📱 » 📱 iPhone 13\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'⚠ Вы действительно хотите купить iPhone 13 за 500 алмазов 💎. Обратите внимание, что предыдущий телефон будет потерян!',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.Telephone"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.Telephone_iPhone13_Buy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )


async def Telephone_iPhone13_Buy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 500:
        new_donate = int(data[20]) - 500
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', telephone = 'iPhone 13'")
        await message.answer(
            message=f'✅ Транзакция успешно проведена.',
        )
        await Telephone(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await Telephone_iPhone13(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

async def clothes(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.clothes'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 👕 Эксклюзивная одежда\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.ShopMenu1"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👕 Набор Adidas", {"cmd": "donate.clothesAdidas"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👕 Набор Thrasher", {"cmd": "donate.clothesThrasher"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👕 Набор бизнесмена", {"cmd": "donate.clothesBizmen"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )

# ----------------------------------------------------------------------------------------------------------------------

async def clothesAdidas(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.clothesAdidas'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 👕 » 👕 Набор Adidas\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'🛍 Цена » 250 💎\n\n'
                f'После покупки, ваша одежда будет:\n'
                f'🧢 Голова » Повязка для тенниса by Adidas\n'
                f'👕 Тело » Футболка CAMO PACK by Adidas\n'
                f'👖 Ноги » Брюки Adicolor Classics 3-Stripes by Adidas\n'
                f'🥾 Обувь » Кеды VL Court 2.0 by Adidas',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.clothes"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.clothesAdidasBuy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )


async def clothesAdidasBuy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 250:
        new_donate = int(data[20]) - 250
        data_clothes = ast.literal_eval(data[24])
        data_clothes = list(data_clothes)
        data_clothes[0] = 'Повязка для тенниса by Adidas'
        data_clothes[1] = 'Футболка CAMO PACK by Adidas'
        data_clothes[2] = 'Брюки Adicolor Classics 3-Stripes by Adidas'
        data_clothes[3] = 'Кеды VL Court 2.0 by Adidas'
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', clothes = \"{data_clothes}\"")
        await message.answer(
            message=f'✅ Набор Adidas успешно куплен и одет на вас',
        )
        await clothes(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await clothesAdidas(message, bot, api)


# ----------------------------------------------------------------------------------------------------------------------

async def clothesThrasher(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.clothesAdidas'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 👕 » 👕 Набор Thrasher\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'🛍 Цена » 350 💎\n\n'
                f'После покупки, ваша одежда будет:\n'
                f'🧢 Голова » Flame Logo Bucket Hat by Thrasher\n'
                f'👕 Тело » Godzilla Flame T-shirt by Thrasher\n'
                f'👖 Ноги » Джинсы by H&M\n'
                f'🥾 Обувь » Кеды by VANZ',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.clothes"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.clothesThrasherBuy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )


async def clothesThrasherBuy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 350:
        new_donate = int(data[20]) - 350
        data_clothes = ast.literal_eval(data[24])
        data_clothes = list(data_clothes)
        data_clothes[0] = 'Flame Logo Bucket Hat by Thrasher'
        data_clothes[1] = 'Godzilla Flame T-shirt by Thrasher'
        data_clothes[2] = 'Джинсы by H&Ms'
        data_clothes[3] = 'Кеды by VANZ'
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', clothes = \"{data_clothes}\"")
        await message.answer(
            message=f'✅ Набор Thrasher успешно куплен и одет на вас',
        )
        await clothes(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await clothesThrasher(message, bot, api)

# ----------------------------------------------------------------------------------------------------------------------

async def clothesBizmen(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'donate.clothesAdidas'")
    data = await database.getUserData(message.from_id)
    await message.answer(
        message=f"🎯 » 💎 » 🛍 » 👕 » 👕 Набор бизнесмена\n\n"
                f'💎 Текущее состояние счета » {await database.pretty(data[20])}\n'
                f'🛍 Цена » 400 💎\n\n'
                f'После покупки, ваша одежда будет:\n'
                f'👕 Тело » Белая рубашка by СУДАРЬ\n'
                f'👖 Ноги » Черные штаны by СУДАРЬ\n'
                f'🥾 Обувь » Черные туфли by СУДАРЬ',
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "donate.clothes"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("Купить", {"cmd": "donate.clothesBizmenBuy"}), color=KeyboardButtonColor.POSITIVE)
                .get_json()
        )
    )


async def clothesBizmenBuy(message: Message, bot: Bot, api: API):
    data = await database.getUserData(message.from_id)
    if data[20] >= 400:
        new_donate = int(data[20]) - 400
        data_clothes = ast.literal_eval(data[24])
        data_clothes = list(data_clothes)
        data_clothes[1] = 'Белая рубашка by СУДАРЬ'
        data_clothes[2] = 'Черные штаны by СУДАРЬ'
        data_clothes[3] = 'Черные туфли by СУДАРЬ'
        await database.setMultiUserData(message.from_id, f"donate = '{new_donate}', clothes = \"{data_clothes}\"")
        await message.answer(
            message=f'✅ Набор бизнесмена успешно куплен и одет на вас',
        )
        await clothes(message, bot, api)
    else:
        await message.answer(
            message=f'❌ У вас недостаточно алмазов для покупки',
        )
        await clothesBizmen(message, bot, api)