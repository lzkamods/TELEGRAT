from req_import import *

s_router = Router()

@s_router.callback_query(F.data == 'scrn')
async def desktop(callback: CallbackQuery):
    await callback.answer('')
    image = pyscreenshot.grab()
    image.save('desktop.png')
    await callback.message.answer_photo(photo=FSInputFile(path='desktop.png'))
    await callback.message.edit_caption(caption=conf.b, reply_markup=kb.back_kb)
    os.remove('desktop.png')