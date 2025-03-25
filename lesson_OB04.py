from abc import ABC, abstractmethod


# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."


class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."


class Axe(Weapon):
    def attack(self):
        return "Боец рубит топором."


# Шаг 3: Класс бойца
class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print(f"{self.name} выбирает новое оружие: {self.weapon.attack()}")

    def attack(self, monster):
        print(self.weapon.attack())
        monster.take_damage()


# Шаг 4: Класс монстра
class Monster:
    def __init__(self, health=1):
        self.health = health

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            print("Монстр побежден!")
        else:
            print("Монстр ранен, но еще жив!")


# --- Тестирование игры ---

# Создаем бойца с мечом
fighter = Fighter("Герой", Sword())
monster = Monster()

# Атака мечом
fighter.attack(monster)

# Меняем оружие на лук и атакуем
fighter.change_weapon(Bow())
fighter.attack(monster)

# Добавляем новое оружие (топор) и снова атакуем
fighter.change_weapon(Axe())
fighter.attack(monster)
