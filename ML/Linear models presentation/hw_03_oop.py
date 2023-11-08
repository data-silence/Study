"""
This is an attempt to realize the class structure of the home buying process
"""


class House:
	"""Хранит информацию о параметрах дома и помогает рассчитать финальную стоимость."""

	def __init__(self, price: int | float, area: int | float):
		"""Инициализирует дом с параметрами цена и площадь."""
		self._price = price
		self._area = area

	def final_price(self, discount: int | float = 0) -> int | float:
		"""Рассчитывает цену дома с учетом информации о дисконте."""
		final_price = self._price * (100 - discount) * 0.01
		return final_price


class SmallHouse(House):
	"""Дочерний класс Дома: предназначен для работы с домами площадью 42 кв.м."""

	def __init__(self, price: int | float, area: int | float = 42):
		super().__init__(price, area)


class Client:
	"""
	Класс, предназначенный для работы с пользователями, позволяющий хранить информацию о пользователе
	и фиксировать изменения его доходов.
	"""
	default_name = 'James Bond'
	default_age = 42

	def __init__(self, bank, name: str = default_name, age: int = default_age):
		""" Создаёт профиль пользователя и инициализирует создание информации о наличии у него счета в Банке."""
		self.name = name
		self.age = age
		self.__account = bank.add_account(client=self)
		self.__house = None

	def info(self):
		"""Справочный метод: выводит информацию о клиенте."""
		print(self.__str__())

	def __str__(self):
		return f'Имя: {self.name}, Возраст: {self.age}, Остаток на счёте: {self.__account.amount} руб.'

	@staticmethod
	def default_info(default_name=default_name, default_age=default_age):
		"""Печатает данные пользователя, используемые в нашей системе по умолчанию."""
		print(f'{default_name=}, {default_age=}')

	def __make_deal(self, house: House, price: int | float):
		"""Вносит изменения в систему в случае покупки пользователем дома."""
		self.__house = house
		self.__account.amount -= price

	def earn_money(self, amount: int | float) -> None:
		"""Вносит в систему заработок пользователя."""
		self.__account.amount += amount
		print(f'{self.name} заработал {amount} рублей. У него на счёте {self.__account.amount} рублей.')

	def buy_house(self, house: House) -> None:
		"""Определяет платежеспособность пользователя и в зависимости от этого авторизует покупку Пользователем дома."""
		price = house.final_price()
		if price > self.__account.amount:
			print(f'У {self.name} недостаточно денег для этой покупки')
		else:
			self.__make_deal(house=house, price=price)
			print(f'Клиент {self.name} успешно приобрёл дом за {price} рублей.')


class Bank:
	"""Хранит информацию о счетах клиентов."""

	def __init__(self):
		"""Инициализирует хранение счетов в пустом списке."""
		self.__accounts = []

	def add_account(self, client: Client):
		"""Добавляет аккаунт нового клиента в банк."""
		if client.name not in [acc.client.name for acc in self.__accounts]:
			client_account = Account(client=client)
			self.__accounts.append(client_account)
			print(f'Добавлена информация о банковском счёте {client.name}')
			return client_account
		else:
			raise ValueError(f'{client.name} уже имеет счет в нашем банке')

	def __str__(self):
		banks_acc = [acc.client.name for acc in self.__accounts]
		return 'Клиенты банка: ' + str(banks_acc)


class Account:
	"""Хранит информацию о счетах клиента."""
	default_amount = 0

	def __init__(self, client: Client, amount: int | float = default_amount):
		""""""
		self.client = client
		self.amount = amount

	def __str__(self):
		return f'{self.client}'

	# def __add__(self, other):
	#     self.amount += other
	#     return self.amount

	def __iadd__(self, other):
		self.amount += other
		print('Операция успешно выполнена')
		return self.amount

	def __isub__(self, other):
		if other > self.amount:
			print(f'У вас недостаточно денег для этой покупки, {self.client.name}')
		else:
			self.amount -= other
			print('Операция успешно выполнена')


if __name__ == "__main__":
	green_bank = Bank()
	red_bank = Bank()

	Client.default_info()

	student = Client(name='Вася Пупкин', age=18, bank=green_bank)
	teacher = Client(name='Василий Пуповин', age=35, bank=red_bank)

	teacher.info()
	print(teacher)
	sm_house = SmallHouse(price=10000)
	# print(sm_house._price, sm_house._area)
	student.buy_house(sm_house)
	student.earn_money(15000)
	print(student)
	student.buy_house(sm_house)
	print(student)
	print(teacher)
	bg_house = House(price=18_000, area=76)
	teacher.buy_house(house=bg_house)
	student.earn_money(7000)
	print(student)
	teacher.earn_money(20_000)
	teacher.buy_house(bg_house)
	print(teacher)
	print(red_bank)
	print(green_bank)
	green_bank.add_account(student)
