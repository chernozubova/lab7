class Plane:
    def __init__(self, name):
        """Инициализация атрибутов класса"""
        self.__name = name
        self.__flights = []

    @property
    def name(self):
        """Уровень доступности атрибута"""
        return self.__name

    @property
    def flights(self):
        """Уровень доступности атрибута"""
        return self.__flights

    def __str__(self):
        "Вывод информации об объекте"
        return f"Самолет авиакомпании: {self.name}"

    def add_flight(self, flight):
        "Добавляет новый рейс в список"
        self.__flights.append(flight)


class Flight:
    def __init__(self, origin, destination, plane):
        """Инициализация атрибутов класса"""
        self.__origin = origin
        self.__destination = destination
        self.__plane = plane
        self.__tickets = []

    @property
    def origin(self):
        """Уровень доступности атрибута name"""
        return self.__origin

    @property
    def destination(self):
        """Уровень доступности атрибута"""
        return self.__destination

    @property
    def plane(self):
        """Уровень доступности атрибута"""
        return self.__plane

    @property
    def tickets(self):
        """Уровень доступности атрибута"""
        return self.__tickets

    def __str__(self):
        "Вывод информации об объекте"
        return f"Рейс из {self.origin} в {self.destination} на самолете авиакомпании {self.plane.name}"

    def add_ticket(self, ticket):
        "Добавляет новый билет в список"
        self.__tickets.append(ticket)


class Ticket:
    def __init__(self, passenger, seat, flight):
        """Инициализация атрибутов класса"""
        self.__passenger = passenger
        self.__seat = seat
        self.__flight = flight

    @property
    def passenger(self):
        """Уровень доступности атрибута"""
        return self.__passenger

    @property
    def seat(self):
        """Уровень доступности атрибута"""
        return self.__seat

    @property
    def flight(self):
        """Уровень доступности атрибута"""
        return self.__flight

    def __str__(self):
        "Вывод информации об объекте"
        return f"Билет - Пассажир: {self.passenger} Место: {self.seat}"

def create_plane():
    "Создаёт авиакомпанию, запрашивая названия у пользователя"
    name = input("Введите авиакомпанию самолета: ")
    return Plane(name)


def create_flight(plane):
    "Создаёт рейс, запрашивая пункт отправления и пункт назначения у пользователя"
    origin = input("Введите пункт отправления: ")
    destination = input("Введите пункт назначения: ")
    return Flight(plane, origin, destination)


def create_ticket(flight):
    "Создаёт билет, запрашивая имя пассажира и место пассажира у пользователя"
    passenger = input("Введите имя пассажира: ")
    seat = input("Введите место: ")
    return Ticket(passenger, seat, flight)
def menu():
    plane = None
    flight = None
    ticket = None

    while True:
        print("\nМеню:")
        print("1. Создать самолет")
        print("2. Создать рейс")
        print("3. Создать билет")
        print("4. Вывести информацию о самолете")
        print("5. Вывести информацию о рейсе")
        print("6. Вывести информацию о билете")
        print("7. Выход из программы")

        point = input("Выберите пункт меню: ")

        if point == "1":
            plane = create_plane()
            print("Самолет создан")
        elif point == "2":
            if plane:
                flight = create_flight(plane)
                print("Рейс создан")
            else:
                print("Сначала создайте самолет")
        elif point == "3":
            if flight:
                ticket = create_ticket(flight)
                print("Билет создан")
            else:
                print("Сначала создайте рейс")
        elif point == "4":
            if plane:
                print(plane)
            else:
                print("Сначала создайте самолет")
        elif point == "5":
            if flight:
                print(flight)
            else:
                print("Сначала создайте рейс")
        elif point == "6":
            if ticket:
                print(ticket)
            else:
                print("Сначала создайте билет")
        elif point == "7":
            print("Программа завершена")
            break
        else:
            print("Выберите верный пункт меню")


if __name__ == "__main__":
    menu()