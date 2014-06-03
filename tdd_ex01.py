import unittest
from random import randint as r

total_character_count = 0

class CreatureCharacter(object):
    def __init__(self):
        self.id = total_character_count
        self.alive = True
        self.str = 1
        self.hlt = 1


class DiceSet(object):
    def __init__(self, min_, max_):
        self.min_ = min_
        self.max_ = max_

    def roll(self):
        return r(self.min_,self.max_)


class AttackRound(object):
    def __init__(self, attacker, target):
        target.hlt -= attacker.str
        if target.hlt <= 0:
            target.alive = False


class NewCreatureStatTests(unittest.TestCase): # fixture
    def setUp(self):
        self.p = CreatureCharacter()
    
    def test_alive(self):
        self.assertTrue(self.p.alive)

    def test_str(self): # str is 'strength'
        self.assertTrue(self.p.str == 1)

    def test_hlt(self):
        self.assertTrue(self.p.hlt == 1)


class DiceRollTests(unittest.TestCase):
    def setUp(self):
        self.ds_1d6 = DiceSet(1,6)

    def test_min(self):
        self.assertTrue(self.ds_1d6.min_ == 1)
    
    def test_max(self):
        self.assertTrue(self.ds_1d6.max_ == 6)
    
    def test_range(self):
        self.assertTrue(self.ds_1d6.roll() in range(1,6))


class AttackTests(unittest.TestCase):
    def setUp(self):
        self.a = CreatureCharacter()
        self.t = CreatureCharacter()
        self.rnd = AttackRound(self.a,self.t)

    def test_target_alive(self):
        self.assertTrue(self.t.alive == False)

    def test_target_hlt(self):
        self.assertTrue(self.t.hlt == 0)

    def test_attacker_alive(self):
        self.assertTrue(self.a.alive == True)

    def test_attacker_hlt(self):
        self.assertTrue(self.a.hlt == 1)

def main():
    unittest.main()

if __name__ == '__main__':
    main()



