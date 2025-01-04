from aiogram.fsm.state import State, StatesGroup

class Userstat(StatesGroup):
    msg_text = State()
    scrntext = State()
    weburl = State()
    killproc = State()
    doc_name = State()
    down_name = State()
    desk_name = State()
    doc_file = State()
    down_file = State()
    desk_file = State()
    dir_del = State()
    f_del = State()
    create_rep = State()
    app_path = State()