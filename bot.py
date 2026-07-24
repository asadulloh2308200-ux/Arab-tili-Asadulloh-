import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# Bot Tokeningiz
TOKEN = "8814422208:AAE_DEUZw-GlvmBvp_xJIrVeM872BZQ2_Xs"

# Sizning Telegram ID raqamingiz
ADMIN_ID = 2067767926

dp = Dispatcher()

# Asosiy menyu tugmalari
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👨‍🏫 Ustoz haqida"), KeyboardButton(text="📚 Kurslarimiz")],
        [KeyboardButton(text="💻 Dars shakli"), KeyboardButton(text="📞 Bog'lanish")]
    ],
    resize_keyboard=True
)

# /start buyrug'i
@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    full_name = html.quote(message.from_user.full_name)
    await message.answer(
        f"Assalomu alaykum, {full_name}!\n\n"
        f"Arab tili ustozi <b>Asadulloh Abdulazizov</b>ning rasmiy botiga xush kelibsiz.\n"
        f"Kerakli bo'limni tanlash uchun pastdagi tugmalardan foydalaning yoki o'zingizni qiziqtirgan savolni shu yerga yozib yuboring:",
        reply_markup=main_menu
    )

# Ustoz haqida bo'limi
@dp.message(F.text == "👨‍🏫 Ustoz haqida")
async def about_teacher(message: Message) -> None:
    text = (
        "<b>👨‍🏫 Ustoz haqida ma'lumot:</b>\n\n"
        "• <b>Ism-familiya:</b> Asadulloh Abdulazizov Azizbek o'g'li\n"
        "• <b>Ma'lumoti:</b> Islom akademiyasi bitiruvchisi\n"
        "• <b>Tajriba:</b> 5+ yillik tajriba\n"
        "• <b>O'quvchilar:</b> 1000 dan ziyod muvaffaqiyatli talabalar\n"
        "• <b>Faoliyatim:</b> 2021-yildan beri o'quvchilarga arab tilini mukammal o'rgatib kelaman."
    )
    await message.answer(text)

# Kurslarimiz bo'limi
@dp.message(F.text == "📚 Kurslarimiz")
async def courses_handler(message: Message) -> None:
    text = (
        "<b>📖 Arab tili kurslarimiz:</b>\n\n"
        "✨ <b>1. Fonetika kursi:</b>\n"
        "Arab tili tovushlarini to'g'ri talaffuz qilish, harflarning maxrajlari va qiroat qoidalarini mukammal o'rganishga mo'ljallangan.\n\n"
        "✨ <b>2. Grammatika kursi:</b>\n"
        "Arab tili qoidalarini chuqur o'zlashtirish, matnlarni tahlil qilish va erkin muloqot qilish ko'nikmasini shakllantirish."
    )
    await message.answer(text)

# Dars shakli (Zoom va Telegram)
@dp.message(F.text == "💻 Dars shakli")
async def lesson_format(message: Message) -> None:
    text = (
        "<b>🌐 Darslarimiz qanday o'tkaziladi?</b>\n\n"
        "Darslarimiz zamonaviy onlayn formatda tashkil etiladi:\n\n"
        "1. <b>Zoom platformasi</b> — jonli muloqot, qoidalarni tushuntirish va o'quvchilar bilan savol-javob qilish uchun.\n"
        "2. <b>Telegram platformasi</b> — dars materiallari, audio va video darsliklar, uyga vazifalarni tekshirish uchun."
    )
    await message.answer(text)

# Bog'lanish bo'limi
@dp.message(F.text == "📞 Bog'lanish")
async def contact_handler(message: Message) -> None:
    await message.answer(
        "Kurslarga yozilish yoki savollar yuzasidan murojaat qilish uchun:\n\n"
        "📞 <b>Telefon raqam:</b> +998941454474\n"
        "📩 <b>Telegram:</b> @the_asadulloh"
    )

# Foydalanuvchidan kelgan xabarlarni adminingizga yo'naltirish
@dp.message()
async def forward_to_admin(message: Message, bot: Bot) -> None:
    user = message.from_user
    username_str = f"@{user.username}" if user.username else "Mavjud emas"
    
    user_info = (
        f"📩 <b>Yangi xabar keldi!</b>\n\n"
        f"👤 <b>Foydalanuvchi:</b> {html.quote(user.full_name)}\n"
        f"🔗 <b>Username:</b> {username_str} (ID: {user.id})\n\n"
        f"💬 <b>Xabar:</b>\n{html.quote(message.text or '[Matnli xabar emas]')}"
    )
    
    await bot.send_message(chat_id=ADMIN_ID, text=user_info)
    await message.answer("Xabaringiz ustozga yuborildi! Tez orada siz bilan bog'lanishadi.")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
  
