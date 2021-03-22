class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def update(self, **kwargs):
        if kwargs.get('name'):
            self.__name = kwargs['name']
        if kwargs.get('age'):
            self.__age = kwargs['age']

    @property
    def name(self):
        return self.__name

    def get_info(self):
        return "{}, age: {}".format(self.__name, self.__age)


class Note:

    def __init__(self):
        self.__note_list = list()

    def add_person(self, person):
        self.__note_list.append(person)

    def remove_person(self, index):
        if 0 <= index <= len(self.__note_list) - 1:
            self.__note_list.remove(self.__note_list[index])

    def update_person(self, index, **kwargs):
        if 0 <= index <= len(self.__note_list) - 1:
            person = self.__note_list[index]
            person.update(**kwargs)

    def get_info_note(self):
        result = list()
        for i in self.__note_list:
            result.append(i.get_info())
        return result


class Position(Person):
    def result(self, position):
        print(self.name, "Position :", position)


note = Note()

position1 = Position('Danil', 20)
position2 = Position('Ivan', 22)
position3 = Position('Irina', 24)
position4 = Position('Andrey', 26)

note.add_person(position1)
note.add_person(position2)
note.add_person(position3)
note.add_person(position4)

print(note.get_info_note())

position1.result("Manager")
position2.result("Director")
position3.result("Accountant")
position4.result("Employee of the month")

note.remove_person(3)
print(note.get_info_note())

note.update_person(2, name='Julia', age=20)
position1.result("Manager")
position2.result("Director")
position3.result("Accountant")
position4.result("Employee of the month")

print(note.get_info_note())


class Computer:
    def __init__(self, processor, motherboard, RAM, SSD, video_card, power_supply):
        self.processor = processor
        self.motherboard = motherboard
        self.RAM = RAM
        self.SSD = SSD
        self.video_card = video_card
        self.power_supply = power_supply

    def On(self):
        print("Computer on")

    def Off(self):
        print("Computer off")


class Processor():
    def __init__(self, frequncy, temperature, voltage):
        self.frequncy = frequncy
        self.temperature = temperature
        self.voltage = voltage

    def data_processing(self):
        print("Processor processes data ")


class Motherboard:
    def __init__(self, form_factor, socket, overlocking):
        self.form_factor = form_factor
        self.socket = socket
        self.overlocking = overlocking

    def compound(self):
        print("Motherboard connects all the components of the PC")


class RAM:
    def __init__(self, memory_type, module_size, frequency):
        self.memory_type = memory_type
        self.module_size = module_size
        self.frequency = frequency

    def temporary_data_storage(self):
        print("RAM temporarily stores data")


class SSD:
    def __init__(self, volume, connection_interface, memory_type):
        self.volume = volume
        self.connection_interface = connection_interface
        self.memory_type = memory_type

    def data_storage_on_ssd(self):
        print("SSD permanently stores computer data")


class Video_card:
    def __init__(self, graphics_core, memory_bus_width, video_card_interface):
        self.graphics_core = graphics_core
        self.memory_bus_width = memory_bus_width
        self.video_card_interface = video_card_interface

    def video_card(self):
        print("Video card card converts the graphic image")


class Power_supply:
    def __init__(self, power, efficiency, dimensions):
        self.power = power
        self.efficiency = efficiency
        self.dimensions = dimensions

    def voltage_supply(self):
        print("power_supply voltage drops to processor, motherboard, ssd")


# My Project (Uno)
# class Deck():
#
#
# class Card:
#     def __init__(self, color, value, cost):
#         self.color = color
#         self.value = value
#         self.cost = cost
#
#
# class Deck(Card):
#
#
# class Player:
#     def __int__(self, sticker, bouncer, number_of_cards):
#         self.sticker = sticker
#         self.bouncer = bouncer
#         self.number_of_cards = number_of_cards
#
#
# class Distribution(Card):
#     def __init__(self, number_of_cards):
#
#
# class Move(Card, Player):