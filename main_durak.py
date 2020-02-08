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
        new_list = self.kozyr[0].rsplit('_')
        self.mast = new_list[1]
        for card in self.cards:
            if self.mast in card[0]:
                card[1] = card[1] + 9
        return self.cards

    def get_mast(self, card):    # узнает масть карты
        new_list = card.rsplit('_')
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
        if len(self.player_cards) > 0 and len(self.comp_cards) > 0 and self.turn: # not self.table - проверяет, пустой ли список(стол)
            print("-------Ваш ход-------")
            bool_card = ""
            while not bool_card:
                tmp_card = str(input('Выберите карту'))
                for card in self.player_cards:
                    if tmp_card == card[0]:
                        tmp_card = card
                        bool_card = tmp_card
                        print('Карта найдена')
                        self.table.append(tmp_card)
                        self.player_cards.remove(card)
                        print('На столе: ', self.table[0][0])
                        return print('Ваши карты: ', list((item[0] for item in self.player_cards))), print('Карты помпьютера: ', list((item[0] for item in self.comp_cards)))
                        self.turn = False
            # if tmp_card in tmp_list:
            #     result = re.search(tmp_card, (item[0] for item in self.player_cards))
            #     self.player_cards.remove(result)
            #     self.table.append(result.group(0))
            # return print('На столе: ', self.table)

        elif len(self.player_cards) > 0 and len(self.comp_cards) > 0 and self.turn == False:
            print('--------Ход компьютера--------')
            print()
            tmp_card = random.choice(self.comp_cards)
            self.table.append(tmp_card)
            self.comp_cards.remove(tmp_card)
            return print('На столе: ', self.table[0][0])
            self.turn = True


    def comp_turn(self):
        if len(self.comp_cards) > 0 and len(self.player_cards) > 0 and self.turn == False and len(self.table) == 0: # выполняется, если начинает ходить компьютер
            print('--------Ход компьютера--------')
            print()
            tmp_card = random.choice(self.comp_cards)
            self.table.append(tmp_card)
            self.comp_cards.remove(tmp_card)
            return print('На столе: ', self.table[0][0])
            self.turn = True

        elif len(self.comp_cards) > 0 and self.turn and len(self.table) != 0: # если ходил игрок, а компьютер отбивается
            c_avble_cards_to_beat = [] # список с картами из руки, которыми можно побить
            changed_table = []   # список [[масть, сила].....[масть, сила]...]
            changed_table = copy.deepcopy(self.table)
            for i in range(len(changed_table)):
                changed_table[i][0] = self.get_mast(Durak, changed_table[i][0])

            for i in range(len(self.comp_cards)):
                if self.get_mast(Durak, self.comp_cards[i][0]) == changed_table[0][0] and self.comp_cards[i][1] > changed_table[0][1] and len(changed_table) == 1:
                    c_avble_cards_to_beat.append(self.comp_cards[i])

            if not c_avble_cards_to_beat:
                print('Компьюетр берет карту ')
                self.comp_cards.append(self.table)
                print(self.comp_cards)

            self.beat_cards = []
            if len(c_avble_cards_to_beat) > 0:
                self.beat_cards.append(random.choice(c_avble_cards_to_beat))
                print('Карты, которыми побили ', self.beat_cards[0][0])
                print('На столе               ', self.table[0][0])

            if len(self.avble_player_cards) > 0: # self.avble_player_cards - карты, которые может подкинуть игрок
                # (!!!!!!НЕ ЗАБЫТЬ ИСП. В ФУНКЦИИ ИГРОКА!!!!!)
                tmp_card = input('Если хотите подкинуть выберите карту, либо введите bito')





            # avaliable_cards_to_beat = copy.deepcopy(self.comp_cards)
            # for i in range(len(self.comp_cards)):
            #     if self.get_mast(Durak, self.comp_cards[i][0]) != changed_table[0][0] and avaliable_cards_to_beat[i][1] < changed_table[0][1]:
            #         avaliable_cards_to_beat.remove(avaliable_cards_to_beat[i])
            #         print(len(avaliable_cards_to_beat))
            # print(avaliable_cards_to_beat)





Durak.all_cards(Durak)
Durak.gen_kozyr_list(Durak)
Durak.gen_cards(Durak)
Durak.whos_first_turn(Durak)
Durak.game_start(Durak)
Durak.comp_turn(Durak)





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


