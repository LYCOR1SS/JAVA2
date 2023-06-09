import logging
import requests

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'BOT TOKEN HERE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def echo(message: types.Message):
    respons = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid=e334bf1f0798b5c89fd60c5325131ad0") 

    data = response.json()
    temp_celsium = data['main']['temp']-273.15
    humidity = data['ain']['humidity']
    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)






























