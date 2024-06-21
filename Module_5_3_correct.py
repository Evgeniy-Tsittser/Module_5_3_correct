class Building():
    def __init__(self):
        self.number_of_floors = 5
        self.building_type = 'degree'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors and self.building_type == other.building_type


number_of_floors = Building()
building_type = Building()
print(number_of_floors == building_type)
