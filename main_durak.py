import random

class Durak:
    def __init__(self): # инициализатор класса
        self.table = []
        self.bito = []   # атрибуты класса
        self.koloda = []


    def all_cards(self): # генерирует все существующие карты в колоде. выход: целая колода (36 карт)
        self.card_type = ['6','7','8','9','10','valet','dama','korol','tuz']
        self.spades = list(map(lambda x: x + '_piki', self.card_type))       #
        self.club = list(map(lambda x: x + '_kresti', self.card_type))       # map применяет к каждому элементу списка переданную функцию lambda
        self.hearts = list(map(lambda x: x + '_chervy', self.card_type))     #
        self.diamonds = list(map(lambda x: x + '_bubi', self.card_type))     #
        self.cards = self.spades + self.club + self.hearts + self.diamonds
        random.shuffle(self.cards) # random.shuffle - перемешивает лист в случайном порядке
        return self.cards

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
        return print(self.mast)

    # def cards_values_rules(self): # функция, определяющая страшенство карт



Durak.all_cards(Durak)
Durak.gen_cards(Durak)
Durak.kozyr(Durak)
print('Введите карту ')
card = list(input())
Durak.get_mast(Durak, card)




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


