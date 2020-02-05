import random

class Durak:
    def __init__(self): # инициализатор класса
        self.table = []
        self.bito = []   # атрибуты класса
        self.koloda = []


    def all_cards(self): # генерирует все существующие карты в колоде. выход: целая колода (36 карт)
        self.card_type = {'6': 1,'7': 2,'8': 3,'9': 4,'10': 5,'valet': 6,'dama': 7,'korol': 8,'tuz': 9}
        self.spades = dict(map(lambda x: x[0] + '_piki', self.card_type))     #
        self.club = dict(map(lambda x: x[0] + '_kresti', self.card_type))       # map применяет к каждому элементу списка переданную функцию lambda
        self.hearts = dict(map(lambda x: x[0] + '_chervy', self.card_type))     #
        self.diamonds = dict(map(lambda x: x[0] + '_bubi', self.card_type))   #
        # self.cards = dict(self.spades.items() + self.club.items() + self.hearts.items() + self.diamonds.items())
        # random.shuffle(self.cards) # random.shuffle - перемешивает лист в случайном порядке
        # return self.cards

    def gen_cards(self): # раздает карты, не больше 6 в начальной руке. выход: два списка с уникальными картами у каждого игрока

        self.player_cards = []
        for card in range(6):
            player_card = random.choice(self.cards)  # random.choice - возвращает случайный элемент списка
            self.player_cards.append(player_card)  # добавляет в список игрока(в руку игрока) карту
            self.cards.remove(player_card) # удаляет из общего числа карт сгенерированную карту

        self.comp_cards = []
        for card in range(6):
            comp_card = random.choice(self.cards)
            self.comp_cards.append(comp_card)    # как и у игрока
            self.cards.remove(comp_card)

        self.player_cards.sort()
        self.comp_cards.sort()
        return print('Ваши карты: ', self.player_cards), print('Карты компьютера: ', self.comp_cards)

    def kozyr(self): # выбирает козырь(карту) из оставшихся после раздачи карт в колоде. выход: выводит карту козырь
        self.kozyr_card = self.cards[0]       #
        self.cards.append(self.kozyr_card)    # кладет козыря в конец колоды
        self.cards.remove(self.cards[0])      #
        return print('Козырь: ', self.kozyr_card)

    def get_mast(self, card):    # узнает масть карты
        list = self.card.rsplit('_')
        self.mast = list[1]
        return self.mast

    def cards_value_sort(self, hand): # функция, сортирующая карты по старшенству, hand - список карт в руке (рука)
        for card in hand:
            if Durak.get_mast(card) == Durak.get_mast(self.kozyr_card):
                self.strong_dict = {}


Durak.all_cards(Durak)
#




# def whos_first_turn(self): # определяет, кто ходит первый


# def find_smallest_card(self): # находит самую слабую карту


#     def find_mast(self): # ищет правильную масть для отбивания карты
#
#
#     def card_value(self): # узнает карты, которые старше той, что необходимо побить. выход: список доступных карт
#
#
#     def take_card(self): # добавляет карту в список того игрока, который должен брать.
#                          # вход: список card_value.
#                          # выход: новая генерация руки взявшего карты игрока
#
#
#     def throw_card(self): # определяет, какие карты можно подкинуть.
#                           # вход: table
#                           # выход: список карт
#
# # ПОЧТИ КАЖДАЯ ФУНКЦИЯ ИМЕЕТ ВАРИАЦИЮ: ДЛЯ ИГРОКА И ДЛЯ КОМПА


