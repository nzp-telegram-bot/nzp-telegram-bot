import os

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)


TOKEN = os.getenv("BOT_TOKEN")


MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["🍽 Меню"],
        ["📍 Адреса и телефоны"],
        ["✨ Что сегодня в НЗП"],
        ["❤️ Отзыв / чаевые"],
        ["📸 Интерьеры"],
        ["💳 Мой профиль и карта лояльности"],
    ],
    resize_keyboard=True,
)


async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Добро пожаловать в НЗП.\n\n"
        "Здесь можно посмотреть меню, выбрать заведение, "
        "узнать, что происходит сегодня, оставить отзыв "
        "и открыть карту лояльности."
    )

    await update.message.reply_text(
        text,
        reply_markup=MAIN_KEYBOARD,
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_main_menu(update, context)


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_main_menu(update, context)


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🍽 Меню":
        await update.message.reply_text(
            "Выберите заведение:\n\n"
            "НЗП Ленина\n"
            "НЗП 8 Марта\n"
            "НЗП Цюрупы\n"
            "ВОЗДУХ"
        )

    elif text == "📍 Адреса и телефоны":
        await update.message.reply_text(
            "Здесь будут адреса, телефоны и ссылки на карты всех заведений НЗП."
        )

    elif text == "✨ Что сегодня в НЗП":
        await update.message.reply_text(
            "Здесь будут актуальные события и специальные предложения НЗП."
        )

    elif text == "❤️ Отзыв / чаевые":
        await update.message.reply_text(
            "Здесь мы сделаем систему отзывов и чаевых."
        )

    elif text == "📸 Интерьеры":
        await update.message.reply_text(
            "Здесь появятся фотографии интерьеров наших заведений."
        )

    elif text == "💳 Мой профиль и карта лояльности":
        await update.message.reply_text(
            "Здесь позже подключим карту лояльности НЗП из iiko."
        )

    else:
        await update.message.reply_text(
            "Выберите нужный раздел в меню ниже.",
            reply_markup=MAIN_KEYBOARD,
        )


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN не задан")

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, buttons)
    )

    print("NZP bot started")
    application.run_polling()


if __name__ == "__main__":
    main()
