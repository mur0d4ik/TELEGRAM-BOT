import logging
from config import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types
from button import lang, menu_uz, menu_ru, menu_en



bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO)



@dp.message_handler(commands = ['start'])
async def welcome(message: types.Message):
    await message.answer(f'Til tanglang:\nВыберете язык:\nChoose language:', reply_markup=lang)

@dp.message_handler(commands = ['spam'])
async def spam_func(message: types.Message):
    while True:
        await message.answer(f'GG')

@dp.message_handler(text = "O'zbekcha🇺🇿")
async def salom(message: types.Message):
    await message.answer(f'Salom {message.from_user.first_name}!')
    await message.answer(f"Menu: ",reply_markup =  menu_uz)
    
    @dp.message_handler(text = "O'zingiz xaqida ma'lumot📚")
    async def info(message: types.Message):
        await message.answer(f"ID : {message.from_user.id}\nUsername : @{message.from_user.username}")
        
    @dp.message_handler(text = "Tilni o'zgartirish 🇺🇿/🇷🇺/🇺🇸")
    async def leng_func(message: types.Message):
        await message.answer("Готово✅", reply_markup = menu_ru)
        
    @dp.message_handler(text = "Информация о себе📚")
    async def info(message: types.Message):
        await message.answer(f"ID : {message.from_user.id}\nUsername : @{message.from_user.username}")
        
    @dp.message_handler(text = "Изменить язык 🇺🇿/🇷🇺/🇺🇸")
    async def leng_func(message: types.Message):
        await message.answer("Ready✅", reply_markup = menu_en)
        
    @dp.message_handler(text = "Personal information📚")
    async def info(message: types.Message):
        await message.answer(f"ID : {message.from_user.id}\nUsername : @{message.from_user.username}")
        
    @dp.message_handler(text = "Change the language 🇺🇿/🇷🇺/🇺🇸")
    async def leng_func(message: types.Message):
        await message.answer("Tayyor✅", reply_markup = menu_uz)
        
    @dp.message_handler(text = '◀️Ortga')
    async def main_menu(message: types.Message):
        await message.answer(f"Menu:",reply_markup = lang)
        
    @dp.message_handler(text = '◀️Назад')
    async def main_menu(message: types.Message):
        await message.answer(f"Меню:",reply_markup = lang)
        
    @dp.message_handler(text = '◀️Back')
    async def main_menu(message: types.Message):
        await message.answer(f"Menu:",reply_markup = lang)
    

@dp.message_handler(text = "Русский🇷🇺")
async def salom(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}!')
    await message.answer(f"Меню: ",reply_markup =  menu_ru)
    
    @dp.message_handler(text = "Информация о себе📚")
    async def info(message: types.Message):
        await message.answer(f"ID : {message.from_user.id}\nUsername : @{message.from_user.username}")
        
    @dp.message_handler(text = "Изменить язык 🇺🇿/🇷🇺/🇺🇸")
    async def leng_func(message: types.Message):
        await message.answer("Ready✅", reply_markup = menu_en)
        
    @dp.message_handler(text = "O'zingiz xaqida ma'lumot📚")
    async def info(message: types.Message):
        await message.answer(f"ID : {message.from_user.id}\nUsername : @{message.from_user.username}")
        
    @dp.message_handler(text = "Tilni o'zgartirish 🇺🇿/🇷🇺/🇺🇸")
    async def leng_func(message: types.Message):
        await message.answer("Готово✅", reply_markup = menu_ru)
        
    @dp.message_handler(text = "Personal information📚")
    async def info(message: types.Message):
        await message.answer(f"ID : {message.from_user.id}\nUsername : @{message.from_user.username}")
        
    @dp.message_handler(text = "Change the language 🇺🇿/🇷🇺/🇺🇸")
    async def leng_func(message: types.Message):
        await message.answer("Tayyor✅", reply_markup = menu_uz)
        
    @dp.message_handler(text = '◀️Ortga')
    async def main_menu(message: types.Message):
        await message.answer(f"Menu:",reply_markup = lang)
        
    @dp.message_handler(text = '◀️Назад')
    async def main_menu(message: types.Message):
        await message.answer(f"Меню:",reply_markup = lang)
        
    @dp.message_handler(text = '◀️Back')
    async def main_menu(message: types.Message):
        await message.answer(f"Menu:",reply_markup = lang)
        
@dp.message_handler(text = "English🇺🇸")
async def salom(message: types.Message):
    await message.answer(f'Hi {message.from_user.first_name}!')
    await message.answer(f"Menu: ",reply_markup =  menu_en)
    
    @dp.message_handler(text = "Personal information📚")
    async def info(message: types.Message):
        await message.answer(f"ID : {message.from_user.id}\nUsername : @{message.from_user.username}")
        
    @dp.message_handler(text = "Change the language 🇺🇿/🇷🇺/🇺🇸")
    async def leng_func(message: types.Message):
        await message.answer("Tayyor✅", reply_markup = menu_uz)
    
    @dp.message_handler(text = "Информация о себе📚")
    async def info(message: types.Message):
        await message.answer(f"ID : {message.from_user.id}\nUsername : @{message.from_user.username}")
        
    @dp.message_handler(text = "Изменить язык 🇺🇿/🇷🇺/🇺🇸")
    async def leng_func(message: types.Message):
        await message.answer("Ready✅", reply_markup = menu_en)
        
    @dp.message_handler(text = "O'zingiz xaqida ma'lumot📚")
    async def info(message: types.Message):
        await message.answer(f"ID : {message.from_user.id}\nUsername : @{message.from_user.username}")
        
    @dp.message_handler(text = "Tilni o'zgartirish 🇺🇿/🇷🇺/🇺🇸")
    async def leng_func(message: types.Message):
        await message.answer("Готово✅", reply_markup = menu_ru)
        
    @dp.message_handler(text = '◀️Ortga')
    async def main_menu(message: types.Message):
        await message.answer(f"Menu:",reply_markup = lang)
        
    @dp.message_handler(text = '◀️Назад')
    async def main_menu(message: types.Message):
        await message.answer(f"Меню:",reply_markup = lang)
        
    @dp.message_handler(text = '◀️Back')
    async def main_menu(message: types.Message):
        await message.answer(f"Menu:",reply_markup = lang)
        
        
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = False)