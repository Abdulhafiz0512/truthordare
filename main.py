import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token - replace with your actual bot token
BOT_TOKEN = "7826833219:AAFK-CJFtDjpDCiHIYIg5WXopDd2aeVzjHU"

# Truth questions in Uzbek
TRUTH_QUESTIONS = [
    "Eng katta qo'rquvingiz nima?",
    "Biror kishiga yolg'on gapirgansiz, aytib bering?",
    "Eng g'alati tush ko'rgansiz, qanday edi?",
    "Kimgadir yashirincha oshiq bo'lgansiz?",
    "Eng noqulay vaziyatga tushgan paytingizni aytib bering?",
    "Agar dunyoda faqat bitta taom qolsa, uni qaysi bo'lardi?",
    "Eng katta ayibingiz nima?",
    "Biror payt politsiyadan qochgansizmi?",
    "Eng qiziq sarguzashtingizni aytib bering?",
    "Qaysi mashhur odam bilan uchrashishni xohlaysiz?",
    "Eng yomon bayramingiz qanday o'tdi?",
    "Biror payt sevgilingizni aldagansizmi?",
    "Eng katta xayolingiz nima?",
    "Qaysi filmdan eng ko'p yig'lagansiz?",
    "Eng g'alati ovqat yegansiz, nima edi?",
    "Biror payt maktabdan qochgansizmi?",
    "Eng utanishli paytingizni aytib bering?",
    "Qaysi she'rni yoddan bilasiz?",
    "Eng sevimli o'yiningiz nima?",
    "Biror payt raqsga tushgansizmi?",
    "Qaysi kitobni eng ko'p marta o'qigansiz?",
    "Eng qiziq tug'ilgan kuningiz qanday o'tdi?",
    "Biror payt yolg'iz qo'rqib qolgansizmi?",
    "Eng sevimli rangingiz nima va nega?",
    "Qaysi mushukcha videosini eng ko'p marta ko'rgansiz?",
    "Eng kulgili xotirangiz nima?",
    "Biror payt yig'lab uxlagansizmi?",
    "Eng sevimli ovqatingiz nima?",
    "Qaysi joyga sayohat qilishni xohlaysiz?",
    "Eng qiziq do'stingiz haqida aytib bering?"
]

# Dare tasks in Uzbek
DARE_TASKS = [
    "10 ta otirish-turish qiling",
    "Biror qo'shiqni kuylab bering",
    "Hayvon ovozini chiqarib ko'ring",
    "5 daqiqa ichida hammaga kompliment qiling",
    "Kulgili rasm chizing",
    "Biror she'rni o'qib bering",
    "10 soniya davomida bir oyoqda turing",
    "Biror kishiga qiziqarli savol bering",
    "Kulgili hikoya aytib bering",
    "Biror mashhur odamni taqlid qiling",
    "5 ta raqam sanang, lekin teskari tartibda",
    "Biror do'stingizga rahmat aytib bering",
    "Kulgili selfie oling",
    "Biror qo'shiqni rap qilib ayting",
    "Mashxur film satrini takrorlang",
    "Biror hayvonni taqlid qilib yuring",
    "Sevimli ovqatingiz haqida qo'shiq kuylang",
    "Biror tilni taqlid qilib gapiring",
    "Kulgili mimika qiling",
    "Biror sport harakatini bajaring",
    "Sevimli rangingizni hamma narsada toping",
    "Biror eski xotirangizni aytib bering",
    "Kulgili yuqori ovozda gapiring",
    "1 dan 10 gacha sanang",
    "Barcha chatdagilar bilan salomlashing",
    "Biror raqs harakatini qiling",
    "Kulgili ovoz chiqarib ko'ring",
    "Biror she'r yoki qo'shiq yozing",
    "5 ta pushup qiling",
    "Biror gap ingliz tilida gapiring"
]

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command handler"""
    welcome_text = """
🎮 **Truth or Dare Bot'ga xush kelibsiz!**

📝 **Buyruqlar:**
• `/truth` - Tasodifiy Truth savoli
• `/dare` - Tasodifiy Dare vazifasi
• `/help` - Yordam

🎯 **Qanday o'ynash:**
1. Biror kishi `/truth` yoki `/dare` yozadi
2. Bot savol yoki vazifa beradi
3. Javob bering yoki vazifani bajaring!

**Oddiy va oson! 🎭**

Abdulhafizga rahmat!
    """
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command handler"""
    help_text = """
🆘 **Yordam:**

📝 **Buyruqlar:**
• `/start` - Botni ishga tushirish
• `/truth` - Truth savoli olish
• `/dare` - Dare vazifasi olish
• `/help` - Bu yordam

🎯 **Truth (Haqiqat):**
- Shaxsiy savol beriladi
- Rostgo'y javob berish kerak

🎭 **Dare (Jur'at):**
- Vazifa beriladi
- Uni bajarish kerak

**Shunchaki `/truth` yoki `/dare` yozing!**


    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def truth_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a random truth question"""
    user_name = update.effective_user.first_name or "Do'st"
    question = random.choice(TRUTH_QUESTIONS)
    
    text = f"🎯 **Truth savoli {user_name} uchun:**\n\n❓ {question}"
    
    await update.message.reply_text(text, parse_mode='Markdown')

async def dare_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a random dare task"""
    user_name = update.effective_user.first_name or "Do'st"
    task = random.choice(DARE_TASKS)
    
    text = f"🎭 **Dare vazifasi {user_name} uchun:**\n\n🎯 {task}"
    
    await update.message.reply_text(text, parse_mode='Markdown')

def main():
    """Main function to run the bot"""
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("truth", truth_command))
    application.add_handler(CommandHandler("dare", dare_command))
    
    # Run the bot
    print("Truth or Dare Bot ishga tushdi...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()