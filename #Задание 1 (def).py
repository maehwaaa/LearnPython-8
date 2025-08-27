#Задание 1
pets = {}

name = input("Введите имя питомца: ")
species = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner = input("Введите имя владельца: ")

def vozrast(age: int) -> str:
    """Возвращает правильное слово для возраста: год / года / лет."""
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif age % 10 in [2, 3, 4] and not (age % 100 in [12, 13, 14]):
        return "года"
    else:
        return "лет"
    
pets[name] = {
    "Вид питомца": species,
    "Возраст питомца": f"{age} {vozrast(age)}",
    "Имя владельца": owner
}

print(pets)

