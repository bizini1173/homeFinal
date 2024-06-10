class Counter:
    def __init__(self):
        self.value = 0

    def add(self):
        self.value += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.commands = []

    def sound(self):
        pass

    def teach_commands(self, new_commands):
        self.commands.extend(new_commands)
        print(f"{self.name} выучил новые команды: {', '.join(new_commands)}")

class Dog(Animal):
    def sound(self):
        return "Гав"

class Cat(Animal):
    def sound(self):
        return "Мяу"

class Bird(Animal):
    def sound(self):
        return "Чирик"

class AnimalRegistry:
    def __init__(self):
        self.animals = {}
        self.counter = None

    def add_animal(self, name, species, age, commands=None):
        if not all((name, species, age)):
            raise ValueError("Все поля должны быть заполнены")
        
        if not self.counter:
            raise RuntimeError("Работа с объектом счетчика должна происходить в блоке try-with-resources")

        animal = None
        if species.lower() == 'собака':
            animal = Dog(name, species, age)
        elif species.lower() == 'кошка':
            animal = Cat(name, species, age)
        elif species.lower() == 'птица':
            animal = Bird(name, species, age)
        else:
            print(f"Неизвестный вид животного: {species.capitalize()}")  # Выводим вид с заглавной буквы
            return

        if commands:
            animal.teach_commands(commands)

        self.animals[name] = animal
        self.counter.add()

    def display_animals(self):
        if self.animals:
            print("Реестр домашних животных:")
            for name, animal in self.animals.items():
                species_rus = {
                    Dog: 'Собака',
                    Cat: 'Кошка',
                    Bird: 'Птица'
                }
                print(f"Имя: {name}, Вид: {species_rus[type(animal)]}, Возраст: {animal.age}, Команды: {', '.join(animal.commands) if animal.commands else 'Нет команд'}")
        else:
            print("Реестр домашних животных пуст.")

def main():
    try:
        with Counter() as counter:
            registry = AnimalRegistry()
            registry.counter = counter

            while True:
                print("\nМеню:")
                print("1. Добавить новое животное")
                print("2. Показать всех животных")
                print("3. Выйти из программы")
                choice = input("Выберите действие: ")

                if choice == '1':
                    name = input("Введите имя животного: ")
                    print("Выберите вид животного:")
                    print("1. Собака")
                    print("2. Кошка")
                    print("3. Птица")
                    species_choice = input("Ваш выбор: ")
                    if species_choice == '1':
                        species = 'собака'
                    elif species_choice == '2':
                        species = 'кошка'
                    elif species_choice == '3':
                        species = 'птица'
                    else:
                        print("Неверный ввод. Вид животного не определен.")
                        continue
                    age = input("Введите возраст животного: ")
                    commands = input("Введите команды через запятую (если есть): ").split(',')
                    registry.add_animal(name, species, age, commands)
                    registry.display_animals()
                elif choice == '2':
                    registry.display_animals()
                elif choice == '3':
                    print("Программа завершена.")
                    break
                else:
                    print("Неверный ввод. Пожалуйста, выберите существующий пункт из меню.")
    except RuntimeError as e:
        print("Ошибка:", e)
    except ValueError as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()
