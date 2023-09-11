import telebot
import requests
import datetime
import time
import glob
import json
import random
import threading
from bs4 import BeautifulSoup
from functools import partial
from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="Mozilla/5.0 (Windows; U; WinNT; en; rv:1.0.2) Gecko/20030311 Beonex/0.8.2-stable")
token = "TOKEN"

sportru = 'https://news.yandex.ru/smi/sportru'
kinopoisk = 'https://news.yandex.ru/smi/kinopoisk'
vedomosti = 'https://news.yandex.ru/smi/vedomosti'
avtoru = 'https://news.yandex.ru/smi/magautoru'
geektimes = 'https://news.yandex.ru/smi/geektimes'
vtimes = 'https://news.yandex.ru/smi/vtimes-io'
meduza = 'https://news.yandex.ru/smi/meduzaio'
rbc = 'https://news.yandex.ru/smi/rbc'
thebell = 'https://news.yandex.ru/smi/thebell'

parsing_url = [vedomosti, rbc, kinopoisk, sportru, geektimes, vtimes, meduza, thebell, avtoru]

subscribed_users = set()  # множество подписанных пользователей
users_choises = {}  #  словарь предпочтений пользователей: имя пользователя - количество статей. будем расширять


users_temp_db = []  # временный список для храненения сведений о юзере до момента записи собранных данных в файл bd
def define_user(id, username, first_name, last_name, location='Москва', currency='USD', crypto='btc', smi=None, genre=None, amount_articles='3'):
	temp_dict = {}
	temp_dict['id'] = id
	temp_dict['username'] = username
	temp_dict['first_name'] = first_name
	temp_dict['last_name'] = last_name
	temp_dict['location'] = location
	if genre is None:
		temp_dict['genre'] = ['main']
	else:
		temp_dict['genre'] = genre
	if smi is None:
		temp_dict['smi'] = ['meduza']
	else:
		temp_dict['smi'] = smi
	temp_dict['currency'] = currency
	temp_dict['crypto'] = crypto
	temp_dict['amount_articles'] = amount_articles
	users_temp_db.append(temp_dict)




currency_name_dict = {}  # словарь где храним наименования и коды всех валют. Нужно будет переделать в файл
def define_currency_list():
	answer_cur_name = requests.get('https://api.coingate.com/v2/currencies')
	cur_name = answer_cur_name.json()
	for el in cur_name:
		currency_name_dict[el['symbol']] = el['title']
define_currency_list()


def what_weather(city='Москва'):
	"""Определят погоду в требуемом пользователю городе"""
	url = f'http://wttr.in/{city}'
	weather_parameters = {
		'format': 2,
		'M': ''
	}
	try:
		response = requests.get(url, params=weather_parameters)
	except requests.ConnectionError:
		return '<сетевая ошибка>'
	if response.status_code == 200:
		return response.text.strip()
	else:
		return '<ошибка на сервере погоды>'


def currency_rate(valute='USD'):
	"""Обрабатывает необходимые операции c выбранной валютой"""
	answer_rate = requests.get('https://api.coingate.com/v2/rates/merchant')
	cross_usd = answer_rate.json()['USDT']
	rub_usd = float(cross_usd['RUB'])

	rate_list = []
	for el in cross_usd:
		rate_list.append(el)

	rub_rate = {}
	for el in rate_list:
		rub_el = rub_usd / float(cross_usd[el])
		rub_rate[el] = rub_el

	if valute.upper() in currency_name_dict.keys():
		answer_rate = round(rub_rate[valute.upper()], 4)
		# answer_cur = currency_name_dict[valute.upper()]
		return f'{currency_name_dict[valute.upper()]} = {answer_rate} ₽'


def city_check(city):
	"""Проверяет существование города"""
	url_check = requests.get(f'https://nominatim.openstreetmap.org/search.php?city={city}&format=jsonv2')
	if not url_check.json():
		return False
	else:
		return True


# f = open("log.txt", "w") #использовалось только для первого запуска, чтобы создать файл.
# f.close()
def wright_db(user_log):
	with open('log.txt', 'a',
	          encoding='utf8') as f:  # не забыть, что повторное выполнение кода приводит к дозаписи(!) в файл
		f.write(f'{user_log}\n')


"""Данный модуль отвечает за парсинг: обрабатывает поток ссылок из Я.Новостей на конечные сайты СМИ, вытягивает из 
них ссылки на 5 последних новостей и записывает их в файл"""


def get_smi_links(smi_link):
	"""Основная функция для парсинга - получает ссылку на сми и вытягивает из неё (пока) список 5 статей"""
	# список статей записывается в файлы на винте, имя файла - имя сми
	headers = {f"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
	                          "Chrome/90.0.4430.212 Safari/537.36"}
	answer = requests.get(smi_link, headers=headers)
	soup = BeautifulSoup(answer.text, 'lxml')

	urls = []
	for link in soup.find_all('a'):
		urls.append(link.get('href'))

	with open('links.txt', 'w', encoding='utf8') as f:
		for el in urls:
			f.write(f'{el}\n')

	result = []
	with open('links.txt', 'r', encoding='utf8') as f:
		for line in f:
			result.append(line.strip('\n').strip())
	# print(result)

	links = []
	for el in result[19:24]:
		links.append(el)
	# os.remove("links.txt")

	with open(f'articles\\{smi_link[27:]}.txt', 'w', encoding='utf8') as f:
		for el in links:
			f.write(f'{el}\n')


def parsing_smi():
	"""Функция, запускающая процесс парсинга - передает в основную функцию get_smi_links набор ссылок для парсинга"""
	# скоро будет добавлена функция, которая будет парсит весь массив ссылок из Я.Новостей и передавать сюда
	# эта функция дважды использует задержку: для задержки парсинга страницы и самого процесса парсинга чтобы не банили
	# в дальнейшем работа с запросами пользователя идёт через обработку сохранённых в процессе парсинга файлов:
	# так быстрее для пользователя, и безопаснее для меня
	while True:
		time.sleep(3600)  # временная строка - чтобы не парсилось при старте сразу (пока не снимут мой блок на Я)
		for url in parsing_url:
			get_smi_links(url)
			time.sleep(250)


"""Данный модуль отвечает за формирование сводной базы статей, спарсенных в последний раз"""
# Из этой базы бот будет тащить запросы, отсюда будут формироваться словари пользовательских предпочтений"


def get_fresh_smi_json():
	"""Собирает результаты парсинга отдельных сайтов в сводный словарь и помещает в специальный json-файл"""
	today_links = []
	filenames_list = glob.glob("articles\\*.txt")  # сохраняет в список файлы в директории articles с расширением *.txt
	# print(filenames_list)
	for file in filenames_list:
		with open(f'{file}', 'r', encoding='utf8') as f:
			templist = []  # Временный список для хранения ссылок по каждому сми
			today_smi_list = {}
			for line in f:
				templist.append(line.strip('\n').strip())
			# print(templist)
			today_smi_list['smi'] = file.lstrip('articles\\').rstrip('.txt')
			today_smi_list['articles'] = templist
			today_links.append(today_smi_list)
	with open('today_links_db.txt', 'w', encoding='utf8') as f:
		json.dump(today_links, f)


def get_smi_compilation(number=3):
	"""Генерирует заданное количество призвольных статей, хранящихся в json-файле today_links_db"""
	get_fresh_smi_json()
	with open('today_links_db.txt', 'r', encoding='utf8') as f:
		json_file = json.load(f)`

	articles_for_choise = []
	for smi in json_file:
		common_result = smi['articles'][:1][0]  # в дальнейшем здесь не забыть использовать переменную
		articles_for_choise.append(common_result)
	random_final_article = random.choices(articles_for_choise, k=number)
	return random_final_article


def the_morning_show():
	while True:
		for username in subscribed_users:
			number = users_choises[username]
			bot.send_message(username, f'Доброе утро, страна!')
			bot.send_message(username, f'Биржевой курс ихних бумажек:\n {currency_rate()}')
			bot.send_message(username, f'Случайная подборка {number} новостей, как ты и хотел:\n')
			for digit in range(number):
				bot.send_message(username, {get_smi_compilation()[digit - 1]})
			bot.send_message(username, f'Интересного тебе дня и хорошего настроения!')
		time.sleep(86400)


# подключаемся к телеграму
bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start'])
def start(message):
	user = message.chat.id
	start_text = 'Чтобы начать, достаточно прислать боту свои координаты, ввести название города или код валюты (' \
	             'например, USD, BTC, EUR, TRY). '
	bot.send_message(user, start_text)
	nickname = message.from_user.username
	first_name = message.from_user.first_name
	last_name = message.from_user.last_name
	what_weather()
	currency_rate()
	define_user(user, nickname, first_name, last_name)
	print(users_temp_db)


@bot.message_handler(commands=['help'])
def help(message):
	user = message.chat.id
	help_text = 'Поделишься своими координатами - получишь целую подборку,\nзапросишь город - вышлю прогноз погоды,' \
	            '\nа если валюту - свежие данные курса.\n\nГорода понимаю на любом языке, курс валют - только по ' \
	            'стандартным трёхбуквенным аббревиатурам (USD, EUR, CNY), но в любом регистре.\n\nПотихоньку научусь ' \
	            'большему - какие мои годы! '
	bot.send_message(user, help_text)


@bot.message_handler(commands=['subscribe'])
def subscribe(message):
	subscribed_users.add(message.chat.id)
	chat_id = message.chat.id
	amount_articles = message.text
	msg = bot.send_message(chat_id, 'Сколько случайных новостей вы хотите получать за раз?')
	bot.register_next_step_handler(msg, how_much_articles)


def how_much_articles(message):
	chat_id = message.chat.id
	amount_articles = message.text
	if not amount_articles.isdigit():
		msg = bot.send_message(chat_id, 'Возраст должен быть числом, введите ещё раз.')
		bot.register_next_step_handler(msg, how_much_articles)
		return
	msg = bot.send_message(chat_id, f'Спасибо, я запомнил: вам слать {amount_articles} статьи! (статей? статьёв?)\n '
	                                f' Начну рассылать в ближайшее утро ')
	users_choises[message.chat.id] = int(amount_articles)
	print(users_choises)


@bot.message_handler(commands=['unsubscribe'])
def unsubscribe(message):
	try:
		subscribed_users.discard(message.chat.id)
		user = message.chat.id
		bye_text = 'Вы отписались от утренней рассылки, больше спамить не буду'
		bot.send_message(user, bye_text)
	except:
		pass


@bot.message_handler(content_types=['text'])
def guess_answer(message):
	"""Функция, которая пытается угадать из текста, что хочет пользователь: валюту или погоду"""
	# message - входящее сообщение
	user = message.chat.id  # temp_dict автора сообщения
	answer = message.text  # текст сообщения

	if answer.upper() in currency_name_dict.keys():
		currency_answer = currency_rate(answer)
		bot.send_message(user, currency_answer)
	elif city_check(answer.lower()):
		weather_answer = what_weather(answer)
		bot.send_message(user, weather_answer)
	else:
		bot.send_message(user, f'Не смог понять ваше сообщение: умею работать с координатами, городами и курсами '
		                       f'валют/криптовалют. А у вас какая-то чушь, бумажки или компот')


@bot.message_handler(content_types=['location'])
def handle_loc(message):
	user = message.chat.id  # temp_dict автора сообщения
	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	coord_dict = message.location
	coord = (coord_dict.latitude, coord_dict.longitude)
	reverse = partial(geolocator.reverse, language="ru")
	address = reverse(coord).raw['address']
	country = address['country']
	city = address['city']
	district = address['city_district']
	street = address['road']
	flat = address['house_number']
	bot.send_message(user, f'Доброе утро, {message.from_user.first_name} {message.from_user.last_name},\nболее '
	                       f'известный в сети как {message.from_user.username}')
	bot.send_message(user, f'Готовлю подборку главного для тебя, жителя человеческого поселения {city}, {country}')
	bot.send_message(user, f'Погодка сегодня у тебя такая:\n {what_weather(city)}')
	bot.send_message(user, f'Биржевой курс ихних бумажек:\n {currency_rate()}')
	bot.send_message(user, f'Случайная подборка новостей:\n')
	for number in range(3):
		bot.send_message(user, {get_smi_compilation()[number-1]})
	bot.send_message(user, f'Вы держитесь здесь, вам всего доброго, хорошего настроения и здоровья!')
	user_log = [user, now, message.from_user.username, message.from_user.first_name, message.from_user.last_name, coord, country, city, district, street, flat]
	print(user_log)
	wright_db(user_log)


thread1 = threading.Thread(target=parsing_smi)
thread2 = threading.Thread(target=the_morning_show())
thread1.start()
thread2.start()


while True:
	try:
		bot.polling(none_stop=True)
	except:
		pass
