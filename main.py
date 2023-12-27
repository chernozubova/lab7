class Plane:
    def __init__(self, name):
        self.__name = name
        self.__flights = []

    @property
    def name(self):
        return self.__name

    @property
    def flights(self):
        return self.__flights

    def __str__(self):
        return f"Самолет авиакомпании: {self.name}"

    def add_flight(self, flight):
        self.__flights.append(flight)


class Flight:
    def __init__(self, origin, destination, plane):
        self.__origin = origin
        self.__destination = destination
        self.__plane = plane
        self.__tickets = []

    @property
    def origin(self):
        return self.__origin

    @property
    def destination(self):
        return self.__destination

    @property
    def plane(self):
        return self.__plane

    @property
    def tickets(self):
        return self.__tickets

    def __str__(self):
        return f"Рейс из {self.origin} в {self.destination} на самолете авиакомпании {self.plane.name}"

    def add_ticket(self, ticket):
        self.__tickets.append(ticket)


class Ticket:
    def __init__(self, passenger, seat, flight):
        self.__passenger = passenger
        self.__seat = seat
        self.__flight = flight

    @property
    def passenger(self):
        return self.__passenger

    @property
    def seat(self):
        return self.__seat

    @property
    def flight(self):
        return self.__flight

    def __str__(self):
        return f"Билет - Пассажир: {self.passenger} Место: {self.seat}"

def create_plane():
    name = input("Введите авиакомпанию самолета: ")
    return Plane(name)


def create_flight(plane):
    origin = input("Введите пункт отправления: ")
    destination = input("Введите пункт назначения: ")
    return Flight(plane, origin, destination)


def create_ticket(flight):
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
            pass
        elif point == "2":
            pass
        elif point == "3":
            pass
        elif point == "4":
            pass
        elif point == "5":
            pass
        elif point == "6":
            pass
        elif point == "7":
            pass
        else:
            pass
