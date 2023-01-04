# Python polymorphism example
from abc import ABC, abstractmethod


class Organism(ABC):
    @abstractmethod
    def eat(self, *args, **kwargs):
        """ get energy for survival, abstract method, must be overridden """
        raise NotImplementedError

    @abstractmethod
    def dispose(self, *args, **kwargs):
        """ dispose of toxic material """
        raise NotImplementedError

    @abstractmethod
    def procreate(self, *args, **kwargs):
        """ create next generation """
        raise NotImplementedError

    @abstractmethod
    def breath(self, *args, **kwargs):
        """ obtain oxygen and emit co2 for metabolism """
        raise NotImplementedError


class Plant(Organism):
    """ A plant is an organism that performs photosynthesis"""

    def eat(self):
        print('I only drink water and absorb minerals.')

    def dispose(self):
        print("Don't need to do that like them dirty animals")

    def procreate(self):
        print("need some bees to achieve that")

    def breath(self):
        print("I do that at night. During the day I make oxygen and sugar!")


    def photo_synthesis(self):
        """ create sugar by combining light, h2o and co2 """
        print("I make sugar to build cellulose for growth, and tempt animals to spread my seeds."
              "I also contribute free oxygen to the atmosphere, you owe me your existence!")


class Animal(Organism):
    """ An animal is an organism who has a gender and can move around """

    def __init__(self, *arg, **kwargs):
        if 'sex' in kwargs:
            self._sex = kwargs['sex']
        else:
            self._sex = 'unknown'

    @property
    def sex(self):
        """ male or female property """
        return self._sex

    @sex.setter
    def sex(self, value: str):
        self._sex = value

    def eat(self, **kwargs):
        if 'food' in kwargs:
            print(f"ate {kwargs['food']}")
        else:
            print("ate something!")

    def breath(self):
        print('it is stuffy here')

    def dispose(self):
        print('I needed that...')

    def procreate(self):
        print('Whfeew, that was nice.')

    def move(self, location=(0, 0)):
        print(f"moved to location {location}")
        """ actively change location """


class Vertebrate(Animal):
    """ a vertebrate is an animal with a spine (except for some people I know)"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._spine = True

    @property
    def spine(self):
        """I do have a spine"""
        return True

class Carnivor(Vertebrate):
    """A carnivor is an animal that consumes meat """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._food = 'Meat'

    def eat(food="furry thing"):
        print(f"sorry, killing {food}s is necessary for my health.")


class Herbivor(Vertebrate):
    """a herbivor enjoys munching grass"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._food = 'Grass'

    def eat(food="green shoots"):
        print(f"don't have to kill no {food}, but might need to chew my cud")


class Mammal(Vertebrate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pregnancy(self):
        """ carry offspring in females """
        if not self.sex == 'Female':
            raise TypeError("Males can't get pregnant")

    def birth(self, name='Baby', number=1):
        """ emit embryo from womb """
        if not self.sex == 'Female':
            raise TypeError("Males don't got no womb")

    def nurse(self):
        """ feed young using milk """
        if not self.sex == 'Female':
            raise TypeError("Males don't got no udders")


class Primate(Mammal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._thumb = 'Opposing'

    @property
    def opposing_thumb(self):
        """ unique to primates """
        return True

    def climb(self):
        """ opposing thumbs makes climbing easy """
        print("Luv them leafy tall things! Everything seems better from my point of view.")


class Human(Primate):
    @property
    def think(self):
        """ property of humans """
        print("Cogito ergo sum.")

    def program(self, stuff: str = 'OOP', lang: str = 'Python'):
        """ write some software """
        print(f"luv programming {stuff} using {lang}")

    def cook(self, food='big mac', alternative='pizza'):
        """ use fire to soften food """
        print(f"Contemplating a {food}, or maybe {alternative}????")
