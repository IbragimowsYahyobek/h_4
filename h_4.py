class Vehicle:
    def move(self):
        return "Транспортное средство движется"

    def fuel(self):
        return "Тип топлива: неизвестен"
    
class Car(Vehicle):
    def move(self):
        return "Машина едет по дороге"

    def fuel(self):
        return "Тип топлива: бензин"
    
class Bicycle(Vehicle):
    def move(self):
        return "Велосипед движется по дороге"

    def fuel(self):
        return "Тип топлива: человеческая сила"

class Boat(Vehicle):
    def move(self):
        return "Лодка плывет по воде"

    def fuel(self):
        return "Тип топлива: дизельное топливо"

def main():
    vehicles = [Car(), Bicycle(), Boat()]
 
    for vehicle in vehicles:
        print(vehicle.move())
        print(vehicle.fuel())
if __name__ == "__main__":
    main()