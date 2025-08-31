# Smartphone class with inheritance

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

# Smartphone inherits from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # call parent constructor
        self.storage = storage
        self.battery = battery
    
    def call(self, number):
        return f"Calling {number}..."
    
    def charge(self):
        return f"{self.info()} is charging."

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S23", "256GB", "4500mAh")
print(phone1.info())          # prints brand + model
print(phone1.call("123-456")) # calling method
print(phone1.charge())        # charging method
