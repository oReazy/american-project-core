
# Карта

# ----------------------------------------------------------------------------------------------------------------------

import asyncio, vkbottle.api, vkbottle_types
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, API, GroupEventType, GroupTypes, LoopWrapper, Callback
import json, time, os, sys, re, ast, datetime, random

from modules import database

# ----------------------------------------------------------------------------------------------------------------------

async def Show(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'map.Show'")
    await message.answer(
        message=f"🎯 » 🗺 Карта",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "mainMenu.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🏛 Важные места", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🧱 Работы для новичков", {"cmd": "map.newGuysWorks"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🛠 Основные работы", {"cmd": "map.Works"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🚙 Автосалоны", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🏢 Отели", {"cmd": "map.Hotels"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🏷 Разное", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🔩 Автомастерские", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🍐 Фермы", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("👕 Секонд-хенды", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🎭 Мероприятия", {"cmd": "map.events"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("👥 Квестовые персонажи", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🛢 Нефтевышки", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .get_json()
        )
    )


async def Hotels(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'map.Hotels'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏢 Отели",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "map.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🏢 Titanic Palace", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🏢 Beverly Hills", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🏢 Bellagio", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🏢 Fairmont Century Plaza", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🏢 The Beverly Hilton", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🏢 Mosaic Hotel", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .get_json()
        )
    )



async def importandPlaces1(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'map.importandPlaces1'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 Важные места",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "map.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "map.importandPlaces2"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🏛 Мэрия", {"cmd": "CityHall.Show"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("⚒ Центр занятости", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🏥 Больница", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("📒 Центр лицензирования", {"cmd": "LicensingCenter.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🌅 Пирс", {"cmd": "Pier.Show"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🏦 Центральный банк", {"cmd": "CentralBank.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🏰 Центральный рынок", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🏣 Страховая компания", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🚓 Штрафстоянка", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🛡 Военкомат", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🧿 Черный рынок", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("💪 Спортивный зал", {"cmd": "SportsHall.Show"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("⛪ Церковь", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🏢 Лотерейный магазин", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🎰 Казино", {"cmd": "casino.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )


async def importandPlaces2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'map.importandPlaces2'")
    await message.answer(
        message=f"🎯 » 🗺 » 🏛 Важные места (2 страница)",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "map.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "map.importandPlaces1"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📻 Радиостанция", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("📺 Телецентр", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🛡 Военная база", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🛡 Тюрьма строгого режима", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🛡 Авианосец", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("📱 Салон сотовой связи", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🏦 Банковское отделение", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .get_json()
        )
    )


async def newGuysWorks(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'map.newGuysWorks'")
    await message.answer(
        message=f"🎯 » 🗺 » 🧱 Работы для новичков",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "map.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🥔 Ферма", {"cmd": "farm.Show"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🏭 Завод", {"cmd": "factory.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("📦 Склад", {"cmd": "warehouse.Show"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("🍕 Доставщик", {"cmd": "delivery.Show"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🚗 Автомобильный завод", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🍔 Макдоналдс", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🛍 Продавец", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .get_json()
        )
    )



async def Works(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'map.Works'")
    await message.answer(
        message=f"🎯 » 🗺 » 🛠 Основные работы",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "map.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "map.Works2"}), color=KeyboardButtonColor.PRIMARY)
                .row()
                .add(Text("🚛 Водитель мусоровоза", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🚚 Дальнобойщик", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🚕 Таксист", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("💵 Инкассатор", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🧯 Пожарный", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("✈ Пилот", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("💰 Налоговая служба", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🚌 Водитель автобуса", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🧰 Механик", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🚋 Водитель трамвая", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .get_json()
        )
    )



async def Works2(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'map.Works2'")
    await message.answer(
        message=f"🎯 » 🗺 » 🛠 Основные работы",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "map.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "map.Works"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🚈 Машинист электропоезда", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .add(Text("🧰 Дорожная служба", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .row()
                .add(Text("🌭 Продавец хотдогов", {"cmd": "none"}), color=KeyboardButtonColor.NEGATIVE)
                .get_json()
        )
    )



async def events(message: Message, bot: Bot, api: API):
    await database.setUserData(message.from_id, 'state', "'map.events'")
    await message.answer(
        message=f"🎯 » 🗺 » 🎭 Мероприятия",
        keyboard=(
            Keyboard(one_time=True, inline=False)
                .add(Text("◀ Назад", {"cmd": "map.Show"}), color=KeyboardButtonColor.PRIMARY)
                .add(Text("◀", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .add(Text("▶", {"cmd": "none"}), color=KeyboardButtonColor.SECONDARY)
                .row()
                .add(Text("🥚 Собиратели", {"cmd": "collectors.Show"}), color=KeyboardButtonColor.SECONDARY)
                .get_json()
        )
    )