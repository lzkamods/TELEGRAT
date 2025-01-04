from req_import import *
from Userst import Userstat

k_router = Router()

@router.callback_query(F.data == 'kilprc')
async def kill(callback: CallbackQuery, state:FSMContext):
    await callback.answer('')
    await callback.message.edit_caption(caption='Напишите название процесса', reply_markup=kb.back_kb)
    kill_name = callback.message.text
    await state.set_state(Userstat.killproc)

@router.message(Userstat.killproc)
async def kill_handler(message: Message, state:FSMContext):
    data = await state.update_data(killname = message.text)
    kill_name = message.text
    await state.clear()
    for process in conf.psutil.process_iter():
        if process.name() == kill_name:
            process.kill()

@router.callback_query(F.data == 'tskmgr')
async def tskmgr(callback: CallbackQuery):
    await callback.answer('')
    os.system('TaskMgr.exe')
