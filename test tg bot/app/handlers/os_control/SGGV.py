from req_import import * 
from Userst import Userstat

sggv_router = Router()

@router.callback_query(F.data == 'shtdwn')
async def calc(callback: CallbackQuery):
    os.system('shutdown /s /t 0')
    await callback.message.reply('Выключение...')

@router.callback_query(F.data == 'sysabt')
async def calc(callback: CallbackQuery):
    callback.answer('')
    await callback.message.edit_caption(caption=F'{conf.cpun}\n {conf.gpun}\n {conf.dskinfo}\n {conf.meminf}', reply_markup=kb.back_kb)

@router.callback_query(F.data == 'run')
async def run(callback: CallbackQuery, state:FSMContext):
    callback.answer('')
    await callback.message.edit_caption(caption='Напишите команду для выполнения... \n Например: "regedit"', reply_markup=kb.back_kb)
    run_msg = callback.message.text
    await state.set_state(Userstat.msg_text)

@router.message(Userstat.msg_text)
async def msg_text_handler(message: Message, state: FSMContext):
    winrun = message.text
    os.system(winrun)
    await state.clear()

@router.callback_query(F.data == 'vol')
async def volm(callback: CallbackQuery):
    await callback.answer('') 
    await callback.message.edit_caption('Выбран пункт "Громкость🔊"', reply_markup=kb.volm)

@router.callback_query(F.data == 'volup')
async def volmup(callback: CallbackQuery):
    callback.answer('')
    pyautogui.press("volumeup",5)

@router.callback_query(F.data == 'voldn')
async def volmdn(callback: CallbackQuery):
    callback.answer('')
    pyautogui.press("volumedown",5)