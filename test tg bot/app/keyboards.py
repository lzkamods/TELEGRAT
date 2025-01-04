from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Управление Системой💻', callback_data='os_cntl')],
    [InlineKeyboardButton(text='Запуск Приложений📌', callback_data='aps'), InlineKeyboardButton(text='Интернет🌐', callback_data='web')],
    [InlineKeyboardButton(text='Команды📎', callback_data='cmnds')]
])

cmnd = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/help'), KeyboardButton(text='/author')],
    [KeyboardButton(text='/start'), KeyboardButton(text='/github')],
    [KeyboardButton(text='Назад⬅️')]
],
resize_keyboard=True,
input_field_placeholder='Выбери пункт меню')

os_control = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сделать Снимок Экрана🖼️', callback_data='scrn'), InlineKeyboardButton(text='Получить Снимок Камеры📸', callback_data='csht')],
    [InlineKeyboardButton(text='Выключить ПК🔌', callback_data='shtdwn'), InlineKeyboardButton(text='Получить Сведения Системы📲', callback_data='sysabt')],
    [InlineKeyboardButton(text='Выполнить📨', callback_data='run'), InlineKeyboardButton(text='Управление Файлами🗂️', callback_data='flmgt')],
    [InlineKeyboardButton(text='Убить процесс💣', callback_data='kilprc'), InlineKeyboardButton(text='Вывести текст на экран💬', callback_data='scrntxt')],
    [InlineKeyboardButton(text='Диспетчер Задач📊', callback_data='tskmgr'), InlineKeyboardButton(text='Громкость🔊', callback_data='vol')],
    [InlineKeyboardButton(text='Назад⬅️', callback_data='back')]
])


file = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Создать Файл📄', callback_data='fcre')], [InlineKeyboardButton(text='Создать Папку📁', callback_data='dcre')],
    [InlineKeyboardButton(text='Удалить Файл🗑️', callback_data='fdel')], [InlineKeyboardButton(text='Удалить Папку🗑️', callback_data='ddel')],
    [InlineKeyboardButton(text='Назад⬅️', callback_data='back_os')]
])

ffl  = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Documents', callback_data='Documents_dir')],
    [InlineKeyboardButton(text='Downloads', callback_data='Downloads_dir')],
    [InlineKeyboardButton(text='Desktop', callback_data='Desktop_dir')],
    [InlineKeyboardButton(text='Назад⬅️', callback_data='back_os')]
])

file_l = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Documents', callback_data='Documents_file')],
    [InlineKeyboardButton(text='Downloads', callback_data='Downloads_file')],
    [InlineKeyboardButton(text='Desktop', callback_data='Desktop_file')],
    [InlineKeyboardButton(text='Назад⬅️', callback_data='back_os')]
])

volm = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Громкость +', callback_data='volup')],
    [InlineKeyboardButton(text='Громкость -', callback_data='voldn')],
    [InlineKeyboardButton(text='Назад⬅️', callback_data='back_os')]
])

apps = InlineKeyboardMarkup(inline_keyboard=[    
    [InlineKeyboardButton(text='Steam🎮', callback_data='stm'), InlineKeyboardButton(text='Калькулятор🧮', callback_data='calc'), InlineKeyboardButton(text='Блокнот📝', callback_data='ntpd')],
    [InlineKeyboardButton(text='Explorer📁', callback_data='expl'), InlineKeyboardButton(text='Discord🎙️', callback_data='dsc'), InlineKeyboardButton(text='Параметры⚙️', callback_data='sett')],
    [InlineKeyboardButton(text='Другое приложение', callback_data='othr')],
    [InlineKeyboardButton(text='Назад⬅️', callback_data='back')]
])

net = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Открыть YouTube▶️', callback_data='yt'), InlineKeyboardButton(text='Открыть ChatGPT🤖', callback_data='gpt')],
    [InlineKeyboardButton(text='Открыть SoundCloud🎧', callback_data='sc'), InlineKeyboardButton(text='Открыть Другой Сайт🌐', callback_data='othrs')],
    [InlineKeyboardButton(text='Назад⬅️', callback_data='back')]
])

startin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Feedback🔴', url='https://t.me/lzka777'), InlineKeyboardButton(text='Donate💵', url='https://new.donatepay.ru/@1094917')],
    [InlineKeyboardButton(text='Начать работу', callback_data='go')]
    ])
    
back_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад⬅️', callback_data='back_os')]
])

back_scrn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад⬅️', callback_data='back_scrn')]
])

