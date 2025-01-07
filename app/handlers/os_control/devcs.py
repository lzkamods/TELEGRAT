from req_import import *
from Userst import Userstat

d_router = Router()
sz = pyautogui.size()
pz = pyautogui.position()

@d_router.callback_query(F.data == 'devices')
async def dvcs(callback: CallbackQuery):
    await callback.message.edit_caption(caption=F'Выбери пункт меню \n Парметры экрана: {sz} \n Положение курсора: {pz}', reply_markup=kb.dvcs)
    await callback.answer('')

@d_router.callback_query(F.data == 'keyb')
async def keyp(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_caption(caption='Нажмите клавишу или напишите текст...')
    key = callback.message.text
    await callback.answer('')
    await state.set_state(Userstat.key)

@d_router.message(Userstat.key)
async def keyp_handler(message: Message, state:FSMContext):
    data = await state.update_data(key = message.text)
    key = message.text
    await state.clear()

    pyautogui.typewrite(key, interval=0.2)

@d_router.callback_query(F.data == 'mse')
async def msm(callback: CallbackQuery):
    await callback.message.edit_caption(caption=F'Выбери пункт меню \n Парметры экрана: {sz} \n Положение курсора: {pz}', reply_markup=kb.mose)
    await callback.answer('')

@d_router.callback_query(F.data == 'lkm')
async def lkm(callback: CallbackQuery):
    pyautogui.leftClick()
    await callback.answer('Готово!')

@d_router.callback_query(F.data == 'pkm')
async def pkm(callback: CallbackQuery):
    pyautogui.rightClick()
    await callback.answer('Готово!')