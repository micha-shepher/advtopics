from unittest import TestCase

from chapter2.organism import Human


class TestHuman(TestCase):
    def test_eat(self):
        h = Human(sex='Female')
        h.eat(food='Rashugullah')
        h.move((4, 3.3))
        h.birth(name='Marjorie')

    def test_dispose(self):
        self.fail()

    def test_procreate(self):
        self.fail()

    def test_breath(self):
        self.fail()
