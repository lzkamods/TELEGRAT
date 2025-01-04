from req_import import *
from Userst import Userstat

router = Router()

#start
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_photo(photo='https://i.imgur.com/4HnBLWt.png', caption=F'Привет, {message.from_user.first_name}.\nЧто хочешь сделать со своим пк?', reply_markup=kb.startin)

@router.callback_query(F.data == 'go')
async def catalog(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_caption(caption='Что желаешь сделать?', reply_markup=kb.main)

#os control
@router.callback_query(F.data == 'os_cntl')
async def os_cntl(callback: CallbackQuery):
    await callback.message.edit_caption(caption='Управление Системой💻', reply_markup=kb.os_control)
    await callback.answer('')

#net
@router.callback_query(F.data == 'web')
async def net(callback: CallbackQuery):
    await callback.message.edit_caption(caption='Интернет🌐', reply_markup=kb.net)

#apps
@router.callback_query(F.data == 'aps')
async def os_cntl(callback: CallbackQuery):
    await callback.message.edit_caption(caption='Запуск Приложений📌', reply_markup=kb.apps)

#another
@router.callback_query(F.data == 'back_os')
async def os_cntl(callback: CallbackQuery):
    await callback.message.edit_caption(caption='', reply_markup=kb.os_control)
    await callback.answer('Готово!')

@router.callback_query(F.data == 'back')
async def os_cntl(callback: CallbackQuery):
    await callback.message.edit_caption(caption='', reply_markup=kb.main)
    await callback.answer('Готово!')

#code written by lzkamods
#checkout on github