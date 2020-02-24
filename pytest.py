from main_durak import Durak
import pytest



class TestDurak:

    def setup(self):
        self.durak_game = Durak()
        print('Test started')

    def teardown(self):
        print('Test finished')

    def test_cards_num(self):
        durak_game = Durak()
        durak_game.all_cards()
        assert len(durak_game.cards) == 36

