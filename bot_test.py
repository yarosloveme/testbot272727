import discord
from discord.ext import commands
import os
PREFIX = '!'

client = commands.Bot( command_prefix=PREFIX)

# Words
fuck_word1 =  "пидр"
fuck_word2 = "гей"
fuck_word3 = "мразь"
fuck_word4 = "урод"
fuck_word5 = "конченный"
fuck_word6 = "дебил"
fuck_word7 = "бизи"
fuck_word8 = "нитро"
fuck_word9 = "привет"
fuck_word10 = "френда"
fuck_word11 = "денег"
fuck_word12 = "пизда"
fuck_word13 = "алло"
fuck_word14 = "клоун"
fuck_word15 = " бро"
fuck_word16 = "ахуел"
fuck_word17 = "охуел"
fuck_word18 = "сосешь"
fuck_word19 = "яpик"
fuck_word20 = "чмо"
fuck_word21 = "выеб"
fuck_word22 = "дурак"
fuck_word23 = "высрал"
fuck_word24 = "пидорас"
fuck_word25 = "пидарас"
fuck_word26 = "даун"
fuck_word27 = "каблук"
fuck_word28 = " лох"
fuck_word29 = "главный"
fuck_word30 = "главная"
fuck_word31 = "базар"
fuck_word32 = "наебал"
fuck_word33 = "обманул"
fuck_word34 = "хуйня"
fuck_word35 = "добавь"
fuck_word36 = "свободен"
fuck_word37 = "блять"
fuck_word38 = "сука"
fuck_word39 = "придурок"
fuck_word40 = "отсоси"
fuck_word41 = "шлюха"
fuck_word42 = "смешно"
fuck_word43 = "тьфу"
fuck_word44 = "бро"


@client.event
async def on_ready():
	print ('Bot online')


@client.event

async def on_message( message ):
	await client.process_commands(message)
	
	msg = message.content.lower()
	author = message.author

	if fuck_word1 in msg:
		await message.channel.send('А может ты, пидор?'f' {author.mention}')
	if fuck_word2 in msg:
		await message.channel.send('А ты типо натурал?'f' {author.mention}')
	if fuck_word3 in msg:
		await message.channel.send('Ты на себя посмотри'f' {author.mention}')
	if fuck_word4 in msg:
		await message.channel.send('От такого же слышу'f' {author.mention}')
	if fuck_word5 in msg:
		await message.channel.send('Я лапочка, а ты иди нахуй'f' {author.mention}')
	if fuck_word6 in msg:
		await message.channel.send('Сам такой'f' {author.mention}')
	if fuck_word7 in msg:
		await message.channel.send('Хуизи')
	if fuck_word8 in msg:
		await message.channel.send('Oтсoси, потом проси'f' {author.mention}')
	if fuck_word9 in msg:
		await message.channel.send('Ну здравствуй, дорогуша'f' {author.mention}')
	if fuck_word10 in msg:
		await message.channel.send('А бан не хочешь?'f' {author.mention}')
	if fuck_word11 in msg:
		await message.channel.send('Ясно, бомж'f' {author.mention}')
	if fuck_word12 in msg:
		await message.channel.send('Манда')
	if fuck_word13 in msg:
		await message.channel.send('А хуем по лбу не дало?'f' {author.mention}')
	if fuck_word14 in msg:
		await message.channel.send('Цирк уехал, ты остался'f' {author.mention}')
	if fuck_word15 in msg:
		await message.channel.send('Говно')
	if fuck_word16 in msg:
		await message.channel.send('Аккуратнее с языком, молодой человек'f' {author.mention}')
	if fuck_word17 in msg:
		await message.channel.send('Аккуратнее с языком, молодой человек'f' {author.mention}')
	if fuck_word18 in msg:
		await message.channel.send('Дружочек, ты видимо не понял с кем общаешься. Вот эта твоя манера речи "клoунская" меня не впечатляет, давай встретимся, объясню на понятном тебе языке, языке боли. Ну давай разберем по частям, тобою написанное )) Складывается впечатление что Ты реально контуженный, обиженный жизнью имбицил )) Могу тебе и в глаза сказать, готов приехать послушать? ) Вся та хyйня тобою написанное это простое пиздaбольство, рембо ты комнатный)) от того что ты много написал, ЖИЗНЬ Твоя лучше не станет) ) пиздеть не мешки ворочить, много вас таких по весне оттаяло )) Про таких как Ты говорят: Мама не хотела, папа не старался Вникай в моё послание тебе- постарайся проанализировать и сделать выводы для себя )'f' {author.mention}')
	if fuck_word19 in msg:
		await message.channel.send('Дружочек, ты видимо не понял с кем общаешься. Вот эта твоя манера речи "клoунская" меня не впечатляет, давай встретимся, объясню на понятном тебе языке, языке боли. Ну давай разберем по частям, тобою написанное )) Складывается впечатление что Ты реально контуженный, обиженный жизнью имбицил )) Могу тебе и в глаза сказать, готов приехать послушать? ) Вся та хyйня тобою написанное это простое пиздaбольство, рембо ты комнатный)) от того что ты много написал, ЖИЗНЬ Твоя лучше не станет) ) пиздеть не мешки ворочить, много вас таких по весне оттаяло )) Про таких как Ты говорят: Мама не хотела, папа не старался Вникай в моё послание тебе- постарайся проанализировать и сделать выводы для себя )'f' {author.mention}')
	if fuck_word20 in msg:
		await message.channel.send('Я тебя захуярю, если еще так скажешь'f' {author.mention}')
	if fuck_word21 in msg:
		await message.channel.send('Во 1) хуле ты мне сделаешь 2) вовторых пошел нахуй в тетьих 3) что ты мне сделаешь, я в другмо городе. За мат извени'f' {author.mention}')
	if fuck_word22 in msg:
		await message.channel.send('Соизвольте пойти нахуй, сэр уебан'f' {author.mention}')
	if fuck_word23 in msg:
		await message.channel.send('Обидно, что кулака у меня два, а ебальник у тебя один'f' {author.mention}')
	if fuck_word24 in msg:
		await message.channel.send('Осуждаю'f' {author.mention}')
	if fuck_word25 in msg:
		await message.channel.send('Осуждаю'f' {author.mention}')
	if fuck_word26 in msg:
		await message.channel.send('Начнем с того, что ты пиздоглазое мудило'f' {author.mention}')
	if fuck_word27 in msg:
		await message.channel.send('Деснами будешь улыбаться за такой бaзaр'f' {author.mention}')
	if fuck_word28 in msg:
		await message.channel.send('Выйди, дай себе леща и зайди нормально, или я сам помогу тебе это сделать'f' {author.mention}')
	if fuck_word29 in msg:
		await message.channel.send('Авторитарному авторитету другой авторитет - не всегда авторитет'f' {author.mention}')
	if fuck_word30 in msg:
		await message.channel.send('Авторитарному авторитету другой авторитет - не всегда авторитет'f' {author.mention}')
	if fuck_word31 in msg:
		await message.channel.send('Бaзaр пусть будет на бaзaре, а я говорю и участвую в разговоре'f' {author.mention}')
	if fuck_word32 in msg:
		await message.channel.send('Нас наебaли, всем спасибо, все свободны'f' {author.mention}')
	if fuck_word33 in msg:
		await message.channel.send('Нас наебaли, всем спасибо, все свободны'f' {author.mention}')
	if fuck_word34 in msg:
		await message.channel.send('Страшно, очень страшно! Мы не знаем что это такое, если бы мы знали что это такое, мы не знаем что это такое!'f' {author.mention}')
	if fuck_word35 in msg:
		await message.channel.send('Oтсoси, потом проси'f' {author.mention}')
	if fuck_word36 in msg:
		await message.channel.send('ЕЩЁ ОДИН ГУДОК С ТВОЕЙ ПЛАТФОРМЫ И ТВОЙ ЗУБНОЙ СОСТАВ ТРОНЕТСЯ'f' {author.mention}')
	if fuck_word37 in msg:
		await message.channel.send('Мне бы хотелось объяснить тебе что к чему, но боюсь такой объём информации не уместится в твоём крошечном мозгу.'f' {author.mention}')
	if fuck_word38 in msg:
		await message.channel.send('То, что ты ужасно выглядишь ещё не значит, что нужно себя так же вести.'f' {author.mention}')
	if fuck_word39 in msg:
		await message.channel.send('Я бы хотел увидеть мир с твоей точки зрения, но не могу засунуть голову в задницу.'f' {author.mention}')
	if fuck_word40 in msg:
		await message.channel.send('А у меня была кукла и ее звали Фубля, она на тебя похожа.'f' {author.mention}')
	if fuck_word41 in msg:
		await message.channel.send('Сделай так, что б я тебя искал...'f' {author.mention}')
	if fuck_word42 in msg:
		await message.channel.send('Смеется последним тот, до кого медленно доходит...'f' {author.mention}')
	if fuck_word43 in msg:
		await message.channel.send('Экран протри'f' {author.mention}')
	if msg in fuck_word44:
		await message.channel.send('Говно')
	


token = os.environ.get('BOT_TOKEN')
client.run( token )
