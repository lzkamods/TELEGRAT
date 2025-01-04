from req_import import *
from Userst import Userstat

w_router = Router()

@router.callback_query(F.data == 'yt')
async def yt(callback: CallbackQuery):
    await callback.answer('')
    os.system("start \"\" https://youtube.com")

@router.callback_query(F.data == 'sc')
async def sc(callback: CallbackQuery):
    await callback.answer('')
    os.system("start \"\" https://soundcloud.com")

@router.callback_query(F.data == 'othrs')
async def webname(callback: CallbackQuery, state:FSMContext):
    callback.answer('')
    await callback.message.edit_caption(caption=F'Введите url сайта \n В формате \n https://example.com', reply_markup=kb.back_kb)
    web_name = callback.message.text
    await state.set_state(Userstat.weburl)

@router.message(Userstat.weburl)
async def webname_handler(message: Message, state:FSMContext):
    data = await state.update_data(webname = message.text)
    web_name = message.text
    await state.clear()
    os.system(F"start \"\" {web_name}")

@router.callback_query(F.data == 'gpt')
async def yt(callback: CallbackQuery):
    await callback.answer('')
    os.system("start \"\" https://chatgpt.com")