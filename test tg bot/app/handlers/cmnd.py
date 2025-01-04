from req_import import *

@router.message(F.text.lower() == 'команды📎')
async def cmnd(message: Message):
    await message.reply('Команды📎', reply_markup=kb.cmnd)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.reply('Все Доступные Команды:\n /help - Помощь\n /start - Начало\n /github - Ссылка на GitHub\n /author - Автор \n Чтобы начать работу бота, нажмите "Начать работу"')

@router.message(Command('github'))
async def cmd_github(message: Message):
    await message.reply('GitHub: https://github.com/lzkamods')

@router.message(Command('author'))
async def cmd_author(message: Message):
    await message.reply('Автор: lzkamods')