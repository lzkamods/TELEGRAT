from req_import import *
from Userst import Userstat

t_router = Router()

@router.callback_query(F.data == 'scrntxt')
async def scrntxt(callback: CallbackQuery, state:FSMContext):
    await callback.answer('')
    await callback.message.edit_caption(caption='Напишите текст для выведения...', reply_markup=kb.back_kb)
    scrn_txt = callback.message.text
    await state.set_state(Userstat.scrntext)

@router.message(Userstat.scrntext)
async def scrntxt_handler(message: Message, state:FSMContext) -> None:
    data = await state.update_data(scrntext=message.text)
    scrn_text = message.text
    await state.clear()
    window = Tk()
    entry = Entry()
    entry.config(font=('Segoe UI',50))
    entry.insert(0, scrn_text)
    entry.pack()
    window.mainloop()