import aiogram
from aiogram import *
from simpledemotivators import Demotivator

API_TOKEN = '#YOUR TOKEN#'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
	await message.answer(text='Привет, пришли боту изображение и подпись тем текстом, которым хочешь видеть текст в демотиваторе!')

@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
	hm1 = 'Привет, этот бот поможет создавать тебе демотиваторы абсалютно бесплатно и без какой либо рекламы, для этого скинь фото в бот и в подписи укажи подпись для демотиватора\n'
	hm2 = 'Разработчик: /developer\nПожертвовать на хостинг: /donate\nРебята! Бот работает только благодоря вашим донатам, ведь хостинг стоит 180 руб/мес, сейчас бот находиться на лчином хостинге у разработчика, котрый он оплачивает своими силами, поверьте, даже если 18 человек скинуться по 10р, то мы сможем оплатить хостинг на следующий месяц, бот возможно скоро закроется из-за невозможности оплачивать постоянно хостинг разрабочиком, если у вас есть хостинг и вы готовы дать доступ, то пишите разработчику, я буду очень рад если бот обретет новый дом!'
	
	video = open('video.mp4', 'rb')
	await bot.send_video(message.from_user.id, video, caption=hm1)
	await message.answer(text=hm2)

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def echo(message):
	
	await message.photo[-1].download('file.jpg')
	dem = Demotivator(message.caption)
	dem.create('file.jpg')
	photo = open('demresult.jpg', 'rb')
	await bot.send_photo(message.from_user.id, photo)

@dp.message_handler(commands=['developer'])
async def echo(message: types.Message):
	await message.answer(text='Разработчик: @ilian_meta\nGitHub: https://github.com/ilian445')

@dp.message_handler(commands=['donate'])
async def echo(message: types.Message):
	await message.answer(text='Донаты помогают оплачивать хостинг для этого проекта, буду рад если вы пожертвуете мне, на хостинг требуется 180р/мес и я не смогу оплачивать его вечно, поэтому задонатить можно здесь:\n Qiwi: https://qiwi.com/n/ilian445\nТинькофф: 2200700771729976\nАльфа-банк: 2200150959802023\nСбербанк: 5336690105318309\nTON: EQDOi-f39PBbaD_1kO6zNZVacjVPwrk_JZnphuzIw_hq-Voy')
	await message.answer(text='!!!Если донатите, то пожалуйста пишите в комментариях к переводу "На хостниг Демотиватора", иначе деньги могут уйти не туда, если хотите скинуть мне на печеньки, то так и пишите, также, если вам будет не трудно, то присылайте скрины донатов сюда: @giant47, потому что не все банки присылают уведомление, всем заранее спасибо за донаты!!!')

if __name__ == '__main__':
	executor.start_polling(dp)