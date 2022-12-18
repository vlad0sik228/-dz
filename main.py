class Animals:
    group = 'dog'

    def __init__(self):
        self.nazvanie = 'Nazvanie'
        self.cacoi = 'Cacoi'
        self.semeistvo = 'Semeistvo'
        self.nazvanie = "Dog"
        self.cacoi = "Планцентарный млекопитающий хищник"
        self.semeistvo = "Псовые"
        print('Создался объект')

dog1 = Animals()

print(dog1.nazvanie)
print(dog1.cacoi)
print(dog1.semeistvo)

class Dog:
    group = 'Bobik'

    def __init__(self):
        self.name = 'Klichka'
        self.vid = 'Vid'
        self.cacoi = 'Cacoi'
        self.name = "Bobik"
        self.vid = "Pydel"
        self.cacoi = "Igriviy"

dog2 = Animals()
print(dog2.name)
print(dog2.vid)
print(dog2.cacoi)

