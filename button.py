from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

lang = ReplyKeyboardMarkup(
    
    keyboard = [
        [
            KeyboardButton(text = "O'zbekcha🇺🇿"),
            KeyboardButton(text = "Русский🇷🇺"),
            KeyboardButton(text = "English🇺🇸")
        ]
    ], 
    resize_keyboard=True
)

menu_uz = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "O'zingiz xaqida ma'lumot📚"),
            KeyboardButton(text = "Tilni o'zgartirish 🇺🇿/🇷🇺/🇺🇸"),
        ],
        [
            KeyboardButton(text = '◀️Ortga')
        ]
    ],
    resize_keyboard=True
)


menu_ru = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "Информация о себе📚"),
            KeyboardButton(text = "Изменить язык 🇺🇿/🇷🇺/🇺🇸"),
        ],
        [
            KeyboardButton(text = '◀️Назад')
        ]
    ],
    resize_keyboard=True
)


menu_en = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "Personal information📚"),
            KeyboardButton(text = "Change the language 🇺🇿/🇷🇺/🇺🇸"),
        ],
        [
            KeyboardButton(text = '◀️Back')
        ]
    ],
    resize_keyboard=True
)