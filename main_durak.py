import random
import copy
import re

class Durak:
    def __init__(self): # инициализатор класса

        self.bito = []   # атрибуты класса
        self.koloda = []



    def all_cards(self): # генерирует все существующие карты в колоде. выход: целая колода (36 карт)
        self.card_type = [['6', 1], ['7', 2], ['8', 3], ['9', 4], ['10', 5], ['valet', 6], ['dama', 7], ['korol', 8], ['tuz', 9]] # self.card_type[i][1] - "сила" карты

        self.spades = copy.deepcopy(self.card_type)
        for i in range(len(self.spades)):
            self.spades[i][0] = self.spades[i][0] + '_piki'

        self.club = copy.deepcopy(self.card_type)
        for i in range(len(self.club)):
            self.club[i][0] = self.club[i][0] + '_kresti'

        self.hearts = copy.deepcopy(self.card_type)
        for i in range(len(self.hearts)):
            self.hearts[i][0] = self.hearts[i][0] + '_chervi'

        self.diamonds = copy.deepcopy(self.card_type)
        for i in range(len(self.diamonds)):
            self.diamonds[i][0] = self.diamonds[i][0] + '_bubi'

        # self.spades = list(map(lambda x: x + '_piki', self.card_type))
        # self.club = list(map(lambda x: x[0] + '_kresti', self.card_type))
        # self.hearts = list(map(lambda x: x[0] + '_chervi', self.card_type))
        # self.diamonds = list(map(lambda x: x[0] + '_bubi', self.card_type))
        self.cards = self.spades + self.club + self.hearts + self.diamonds
        random.shuffle(self.cards)
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

        return print('Ваши карты: ', list((item[0] for item in self.player_cards))), print('Карты помпьютера: ', list((item[0] for item in self.comp_cards))), print('Козырь: ', self.kozyr[0])

    # def kozyr(self): # выбирает козырь(карту) из оставшихся после раздачи карт в колоде. выход: выводит карту козырь
    #     self.kozyr_card = self.cards[0]       #
    #     self.cards.append(self.kozyr_card)    # кладет козыря в конец колоды
    #     self.cards.remove(self.cards[0])      #
    #     return print('Козырь: ', self.kozyr_card)

    def gen_kozyr_list(self): # пересоздает список с картами, имеющие масть козыря, изменяя силу карт
        kozyr_card = random.choice(self.cards)
        self.kozyr = kozyr_card
        self.cards.append(kozyr_card)  # кладет козыря в конец колоды
        self.cards.remove(self.cards[0])

        new_list = self.kozyr[0].rsplit('_')
        self.mast = new_list[1]
        for card in self.cards:
            if self.mast in card[0]:
                card[1] = card[1] + 9
        return self.cards

    def get_mast(self, card):    # узнает масть карты
        new_list = self.card.rsplit('_')
        self.mast = new_list[1]
        return self.mast

    def whos_first_turn(self):
        player_smallest_card = min(item[1] for item in self.player_cards) # цикл перебора вторых элементов подсписков(силы)
        comp_smallest_card = min(item[1] for item in self.comp_cards)
        if player_smallest_card < comp_smallest_card:
            self.turn = True
        else:
            self.turn = False
        return self.turn

    def game_start(self):
        self.table = []
        if len(self.player_cards) > 0 and len(self.comp_cards) > 0 and self.turn == True: # not self.table - проверяет, пустой ли список(стол)
            print("-------Ваш ход-------")
            tmp_card = str(input('Выберите карту'))
            for card in self.player_cards:
                if tmp_card == str(card[0]):
                    result = card[0]
                # else: result = 'У вас нет такой карты'
            # if tmp_card in tmp_list:
            #     result = re.search(tmp_card, (item[0] for item in self.player_cards))
            #     self.player_cards.remove(result)
            #     self.table.append(result.group(0))
            # return print('На столе: ', self.table)
            return print(result)

        else:
            print('Ход компьютера')
            print()
            tmp_card = random.choice(self.comp_cards)
            self.table.append(tmp_card)
            self.comp_cards.remove(tmp_card)
            return print('На столе: ', self.table[0][0])


    # def game(self):
    #     count = 0
    #     if len(self.player_cards) > 0 & len(self.comp_cards) > 0 & count == 0:
    #         print("Ваш ход")
    #         self.table = input()
    #         print('Карты на столе ', self.table)
    #     else:
#
Durak.all_cards(Durak)
Durak.gen_kozyr_list(Durak)
Durak.gen_cards(Durak)
Durak.whos_first_turn(Durak)
Durak.game_start(Durak)





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


