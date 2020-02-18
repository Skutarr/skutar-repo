class Wizard:
    wizard_name = "wizard_name" # инкапсуляция _set(пробел перед
                                #   переменной/методом еще не нужно использовать в других объектах)
                                #  если же используются два нижних __set, то говорит о запрете исполь-
                                #   зования строки/метода
                                #   но можно юзать если igor._Wizard__set
                                #   но по факту в питоне этого особо нет

    specialty = "common_wizard"  # конструктор по-умолчанию
    magic_skill = "summon_servant"
    mp_lvl = 20

    def __init__(self, wizard_name, specialty, magic_skill, mp_lvl):  # конструктор с парамметром
        self.wizard_name = wizard_name
        self.specialty = specialty
        self.magic_skill = magic_skill
        self.mp_lvl = mp_lvl

    def set(self, wizard_name, specialty, magic_skill, mp_lvl):
        self.wizard_name = wizard_name
        self.specialty = specialty
        self.magic_skill = magic_skill
        self.mp_lvl = mp_lvl


    def info(self):
        print("wizard_name - " + " " + self.wizard_name + "\n" +
              "specialty - " + " " "\t" + self.specialty + "\n" +
              "magic_skill - " + " " + self.magic_skill + "\n" +
              "mp_lvl - " + " " + str(self.mp_lvl))

class Pyromancer(Wizard):  # наследование
      fire_skill = "fireball"


igor = Wizard("Igor_simpleMag", "first_class_summoner", "frog_summon", 25) # либо установить параметры через конструктор
# igor.set("Igor_simpleMag", "first_class_summoner", "frog_summon", 25) # либо через сеттер
igor.info()
