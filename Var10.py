from abc import ABC, abstractmethod

#4.	10.	Корабль, пароход, парусник, корвет. 

class Sheep(ABC):
    @abstractmethod
    def go():
        pass

class Sailboat(Sheep):
    def __init__(self, color):
        self.color = color

    def go(self):
        print(f'Цвет вашего паруса: {self.color}\n')

class Steamship(Sheep):
    def __init__(self, size):
        self.size = size

    def go(self):
        print(f'Размер парохода: {self.size} метров в длинну\n')

class Corvette(Sheep):
    def __init__(self, armor):
        self.armor = armor
        
    def go(self):
        print(f'Толщина брони: {self.armor}мм. \n')

test = Sailboat('Cиний')
exam = Steamship(150)
finalexam = Corvette(50)

test.go()
exam.go()
finalexam.go()

    # Стихотворение, стиль изложения, рифма, проза 

class Style(ABC):
    @abstractmethod
    def read():
        pass

class Rythm(Style):
    def __init__(self, type):
        self.type = type

    def read(self):
        print(f'Тип рифмы: {self.type}\n')

class Poem(Style):
    def __init__(self, topic):
        self.topic = topic

    def read(self):
        print(f'Суть стихотворения: {self.topic} \n')

class Proze(Style):
    def __init__(self, stihi):
        self.stihi = stihi
        
    def read(self):
        print(f'Количество стихов в прозе: {self.stihi}\n')

rythm = Rythm("Перекрёсная")
poem = Poem("О любви")
proze = Proze(12)

rythm.read()
poem.read()
proze.read()