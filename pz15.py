#task 1

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}, Місто: {self.city}"

p = Person("Іван", 20, "Львів")
print(p.info())

#task 2

class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Рік: {self.year}, Колір: {self.color}"

    def repaint(self, new_color):
        self.color = new_color

c = Car("Toyota", "Camry", 2020, "Чорний")
c.repaint("Білий")
print(c.info())

#task 3

class BankAccount:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостатньо коштів")
        self.balance -= amount

    def check_balance(self):
        return self.balance

b = BankAccount("Іван", "UA12345678", 1000)
b.deposit(500)
b.withdraw(300)
print("Баланс:", b.check_balance())
