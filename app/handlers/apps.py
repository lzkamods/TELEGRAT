from req_import import *
from Userst import Userstat

a_router = Router()

@router.callback_query(F.data == 'stm')
async def steam(callback: CallbackQuery):
    call(["E:/steam/steam.exe"])
    await callback.answer('')

@router.callback_query(F.data == 'calc')
async def calc(callback: CallbackQuery):
    call(["calc.exe"])
    await callback.answer('')

@router.callback_query(F.data == 'ntpd')
async def mine(callback: CallbackQuery):
    call(["notepad.exe"])
    await callback.answer('')

@router.callback_query(F.data == 'expl')
async def obs(callback: CallbackQuery):
    call(["explorer.exe"])
    await callback.answer('')

@router.callback_query(F.data == 'dsc')
async def ds(callback: CallbackQuery):
    path = Path(os.getenv('LOCALAPPDATA')) / 'Discord' / 'app-1.0.9175' / 'Discord.exe'
    print(path)
    call([path])
    await callback.answer('')

@router.callback_query(F.data == 'sett')
async def sett(callback: CallbackQuery):
    webbrowser.open("ms-settings:")
    await callback.answer('')

@router.callback_query(F.data == 'othr')
async def otherapp(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_caption(caption='Введите путь к приложению', reply_markup=kb.back_kb)
    await callback.answer('')
    app_path = callback.message.text
    await state.set_state(Userstat.app_path)

@router.message(Userstat.app_path)
async def app_handler(message: Message, state:FSMContext):
    data = await state.update_data(app_path = message.text)
    app_path = message.text
    await state.clear()
    call([app_path])