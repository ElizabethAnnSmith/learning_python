# Tutorial exercise

# Create two new vehicles call car1 and car2
# Car1 should be a red convertible worth $60,000.00 and named 'Fer'
# Car2 should be a blue van worth $10,000.00 and named 'Jump'

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car2 = Vehicle()

car1.name = "Fer"
car2.name = "Jump"

car1.kind = "convertible"
car2.kind = "van"

car1.color = "red"
car2.color = "blue"

car1.value = 60000.00
car2.value = 10000.00


print(car1.description())
print(car2.description())
