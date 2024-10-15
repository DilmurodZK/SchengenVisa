from apscheduler.schedulers.asyncio import AsyncIOScheduler
import apsched
from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor

token = ''#Enter your Telegram Bot token
bot = Bot(token=token)
dp = Dispatcher(bot=bot)
scheduler = AsyncIOScheduler(timezone="Asia/Tashkent")


@dp.message_handler(commands='start')
async def select_info(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Schengen visa uchun ariza sanasi qidiruvi ishga tushdi')

    scheduler.add_job(apsched.send_message_interval, trigger='interval', seconds=20, kwargs={'bot': bot})
    scheduler.start()


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)
