from req_import import *



bot = Bot(token=conf.TOKEN)
dp = Dispatcher()

conf.icon_tg

async def main():
    dp.include_routers(router, s_router, f_router,
                        c_router, sggv_router, t_router,
                        k_router, w_router, a_router, d_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')