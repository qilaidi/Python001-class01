from abc import ABCMeta, abstractmethod
from enum import Enum


class Zoo(object):
    animal_list = set()

    def __init__(self, name):
        self.name = name

    def add_animal(self, animal):
        self.animal_list.add(animal)
        self.__setattr__(animal.__class__.__name__, self.animal_list)


class Animal(metaclass=ABCMeta):
    Animal_Size = Enum("Animal_Size", "微 小 中等 大 巨")
    Animal_Type = Enum("Animal_Type", "食肉 食草 杂食")
    Animal_Character = Enum("Animal_Character", "凶猛 温顺 冷漠")

    @property
    def is_aggressive(self):
        if self.Animal_Type[self.animal_type].value == 1 and \
                self.Animal_Character[self.animal_character].value == 1 and \
                self.Animal_Size[self.animal_size].value >= 3:
            return True
        return False

    @abstractmethod
    def __init__(self, name, animal_type, animal_size, animal_character):
        self.name = name
        self.animal_size = animal_size
        self.animal_type = animal_type
        self.animal_character = animal_character


class Cat(Animal):
    meow = "meow"

    def __init__(self, name, cat_type, cat_size, cat_character):
        super().__init__(name, cat_type, cat_size, cat_character)

    @property
    def is_pet(self):
        if not self.is_aggressive:
            return True
        return False


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    print(have_cat)
