from req_import import *

f_router = Router()
from Userst import Userstat

@f_router.callback_query(F.data == 'flmgt')
async def files(callback: CallbackQuery):
    callback.answer('')
    await callback.message.edit_caption('Выберите действие', reply_markup=kb.file)

@f_router.callback_query(F.data == 'dcre')
async def dir(callback: CallbackQuery):
    callback.answer('')
    await callback.message.edit_caption('Выберите Местоположение Папки', reply_markup=kb.ffl)

@f_router.callback_query(F.data == 'fcre')
async def file(callback: CallbackQuery, state:FSMContext):
    callback.answer('')
    await callback.message.edit_caption('Выберите Местоположение файла', reply_markup=kb.file_l)

@f_router.callback_query(F.data == 'ddel')
async def deldir(callback: CallbackQuery, state:FSMContext):
    callback.answer('')
    await callback.message.reply('Введите Путь к Папке для удаления')
    await state.set_state(Userstat.dir_del)

@f_router.callback_query(F.data == 'fdel')
async def delfile(callback: CallbackQuery, state:FSMContext):
    callback.answer('')
    await callback.message.reply('Введите Путь к Файлу для удаления')
    await state.set_state(Userstat.f_del)

@f_router.callback_query(F.data == 'Documents_dir')
async def doc(callback: CallbackQuery, state:FSMContext):
    await callback.answer('')
    await callback.message.answer('Documents: Введите название папки')
    await state.set_state(Userstat.doc_name)

@f_router.callback_query(F.data == 'Documents_file')
async def doc(callback: CallbackQuery, state:FSMContext):
    await callback.answer('')
    await callback.message.answer('Documents: Введите название Файла \n В формате \n example.txt')
    await state.set_state(Userstat.doc_file)

@f_router.callback_query(F.data == 'Desktop_dir')
async def desk_dir(callback: CallbackQuery, state:FSMContext):
    await callback.answer('')
    await callback.message.answer('Desktop: Введите название папки')
    await state.set_state(Userstat.desk_name)

@f_router.callback_query(F.data == 'Desktop_file')
async def desk(callback: CallbackQuery, state:FSMContext):
    await callback.answer('')
    await callback.message.answer('Desktop: Введите название Файла \n В формате \n example.txt')
    await state.set_state(Userstat.desk_file)

@f_router.callback_query(F.data == 'Downloads_dir')
async def down(callback: CallbackQuery, state:FSMContext):
    await callback.answer('')
    await callback.message.answer('Downloads: Введите название папки')
    await state.set_state(Userstat.down_name)

@f_router.callback_query(F.data == 'Downloads_file')
async def down(callback: CallbackQuery, state:FSMContext):
    await callback.answer('')
    await callback.message.answer('Downloads: Введите название Файла \n В формате \n example.txt')
    await state.set_state(Userstat.down_file)

@f_router.message(Userstat.doc_name)
async def doc_handler(message: Message, state:FSMContext):
    data = await state.update_data(doc_name = message.text)
    doc_name = message.text
    await state.clear()
    path = Path(os.path.join(os.environ['USERPROFILE'], 'Documents', doc_name))
    print(path)
    path.mkdir(parents=True, exist_ok=True)
    await message.reply('Готово!')

@f_router.message(Userstat.desk_name)
async def desk_handler(message: Message, state:FSMContext):
    data = await state.update_data(desk_name = message.text)
    desk_name = message.text
    await state.clear()
    path = Path(os.path.join(os.environ['USERPROFILE'], 'Desktop', desk_name))
    print(path)
    path.mkdir(parents=True, exist_ok=True)
    await message.reply('Готово!')

@f_router.message(Userstat.down_name)
async def down_handler(message: Message, state:FSMContext):
    data = await state.update_data(down_name = message.text)
    down_name = message.text
    await state.clear()
    path = Path(os.path.join(os.environ['USERPROFILE'], 'Downloads', down_name))
    print(path)
    path.mkdir(parents=True, exist_ok=True)
    await message.reply('Готово!')

@f_router.message(Userstat.doc_file)
async def doc_handler(message: Message, state:FSMContext):
    data = await state.update_data(doc_file = message.text)
    doc_file = message.text
    await state.clear()
    path = Path(os.path.join(os.environ['USERPROFILE'], 'Documents', doc_file))
    print(path)
    f = open(path, 'x')
    await message.reply('Готово!')

@f_router.message(Userstat.desk_file)
async def desk_handler(message: Message, state:FSMContext):
    data = await state.update_data(desk_file = message.text)
    desk_file = message.text
    await state.clear()
    path = Path(os.path.join(os.environ['USERPROFILE'], 'Desktop', desk_file))
    print(path)
    f = open(path, 'x')
    await message.reply('Готово!')

@f_router.message(Userstat.down_file)
async def down_handler(message: Message, state:FSMContext):
    data = await state.update_data(down_file = message.text)
    down_file = message.text
    await state.clear()
    path = Path(os.path.join(os.environ['USERPROFILE'], 'Downloads', down_file))
    print(path)
    f = open(path, 'x')
    await message.reply('Готово!')

@f_router.message(Userstat.dir_del)
async def dir_del(message: Message, state:FSMContext):
    data = await state.update_data(dir_del = message.text)
    dir_del = message.text
    await state.clear()
    path = Path(dir_del)
    path.rmdir()
    await message.reply('Готово!')

@f_router.message(Userstat.f_del)
async def f_del(message: Message, state:FSMContext):
    data = await state.update_data(f_del = message.text)
    f_del = message.text
    await state.clear()
    path = Path(f_del)
    path.unlink()
    await message.reply('Готово!')