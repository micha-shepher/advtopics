from unittest import TestCase

from chapter2.organism import Human


class TestHuman(TestCase):
    def test_eat(self):
        h = Human(sex='Female')
        h.eat(food='Rashugullah')
        h.move((4, 3.3))
        h.birth(name='Marjorie')

    def test_dispose(self):
        h = Human(sex='Male')
        self.assertEqual(h.sex, 'Male')
        h.breath()
        h.climb()
        h.dispose()

    def test_opposingThumb(self):
        h = Human(sex='Male')

        self.assertEqual(h.opposing_thumb, True)

    def test_female_stuff(self):
        h = Human(sex='Female')
        h.pregnancy()
        h.birth(name='Edward', number=1)
        h.nurse()
        h.sex = 'Male'

        with self.assertRaises(TypeError):
            h.pregnancy()

        with self.assertRaises(TypeError):
            h.birth()

        with self.assertRaises(TypeError):
            h.nurse()


    def test_procreate(self):
        self.assertTrue(True)

    def test_breath(self):
        self.assertTrue(True)
