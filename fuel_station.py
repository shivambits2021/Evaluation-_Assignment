class FuelStation:
    def __init__(self, diesel: int, petrol: int, electric: int):
        self.slots = {
            "diesel": diesel,
            "petrol": petrol,
            "electric": electric
        }
        self.used_slots = {
            "diesel": 0,
            "petrol": 0,
            "electric": 0
        }

    def fuel_vehicle(self, fuel_type: str) -> bool:
        if fuel_type in self.slots and self.used_slots[fuel_type] < self.slots[fuel_type]:
            self.used_slots[fuel_type] += 1
            return True
        return False

    def open_fuel_slot(self, fuel_type: str) -> bool:
        if fuel_type in self.slots and self.used_slots[fuel_type] > 0:
            self.used_slots[fuel_type] -= 1
            return True
        return False


# Initialize the fuel station with slots
fuel_station = FuelStation(diesel=2, petrol=2, electric=1)

# Test cases
print(fuel_station.fuel_vehicle("diesel"))  # True (1 slot now open for diesel)
print(fuel_station.fuel_vehicle("petrol"))  # True (1 slot now open for petrol)
print(fuel_station.fuel_vehicle("diesel"))  # True (0 slots now open for diesel)
print(fuel_station.fuel_vehicle("electric"))  # True (0 slots now open for electric)
print(fuel_station.fuel_vehicle("diesel"))  # False (0 slots open for diesel)
print(fuel_station.open_fuel_slot("diesel"))  # True (1 slot now open for diesel)
print(fuel_station.fuel_vehicle("diesel"))  # True (0 slots now open for diesel)
print(fuel_station.open_fuel_slot("electric"))  # True (1 slot now open for electric)
print(fuel_station.open_fuel_slot("electric"))  # False (only 1 slot available at fuel station)
