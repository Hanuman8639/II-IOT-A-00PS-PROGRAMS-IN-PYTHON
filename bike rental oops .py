import datetime

class Bike:
    def __init__(self, bike_id, bike_type, is_available=True):
        self.bike_id = bike_id
        self.bike_type = bike_type  # e.g., 'standard', 'electric', 'mountain'
        self.is_available = is_available

    def __str__(self):
        return f"Bike ID: {self.bike_id}, Type: {self.bike_type}, Available: {self.is_available}"

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.rented_bikes = []

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Rented Bikes: {[bike.bike_id for bike in self.rented_bikes]}"

class RentalSystem:
    def __init__(self):
        self.bikes = {}  # bike_id: Bike object
        self.customers = {}  # customer_id: Customer object
        self.rentals = {}  # rental_id: {'customer_id': ..., 'bike_id': ..., 'rent_time': ...}
        self.next_rental_id = 1

    def add_bike(self, bike_id, bike_type):
        if bike_id not in self.bikes:
            self.bikes[bike_id] = Bike(bike_id, bike_type)
            print(f"Bike {bike_id} ({bike_type}) added to the system.")
        else:
            print(f"Bike {bike_id} already exists.")

    def add_customer(self, customer_id, name):
        if customer_id not in self.customers:
            self.customers[customer_id] = Customer(customer_id, name)
            print(f"Customer {name} (ID: {customer_id}) added to the system.")
        else:
            print(f"Customer {customer_id} already exists.")

    def rent_bike(self, customer_id, bike_id):
        customer = self.customers.get(customer_id)
        bike = self.bikes.get(bike_id)

        if not customer:
            print(f"Customer {customer_id} not found.")
            return False
        if not bike:
            print(f"Bike {bike_id} not found.")
            return False
        if not bike.is_available:
            print(f"Bike {bike_id} is currently not available.")
            return False

        bike.is_available = False
        customer.rented_bikes.append(bike)
        rental_id = self.next_rental_id
        self.rentals[rental_id] = {
            'customer_id': customer_id,
            'bike_id': bike_id,
            'rent_time': datetime.datetime.now()
        }
        self.next_rental_id += 1
        print(f"Bike {bike_id} rented by customer {customer.name} (Rental ID: {rental_id}).")
        return True

    def return_bike(self, rental_id):
        rental_info = self.rentals.get(rental_id)
        if not rental_info:
            print(f"Rental ID {rental_id} not found.")
            return False

        customer_id = rental_info['customer_id']
        bike_id = rental_info['bike_id']
        rent_time = rental_info['rent_time']

        customer = self.customers[customer_id]
        bike = self.bikes[bike_id]

        bike.is_available = True
        customer.rented_bikes.remove(bike)
        del self.rentals[rental_id]

        return_time = datetime.datetime.now()
        rental_duration = return_time - rent_time
        print(f"Bike {bike_id} returned by customer {customer.name}.")
        print(f"Rental duration: {rental_duration}.")
        # Calculate cost based on duration here if needed
        return True

    def display_available_bikes(self):
        print("\nAvailable Bikes:")
        for bike in self.bikes.values():
            if bike.is_available:
                print(bike)

    def display_rented_bikes(self):
        print("\nRented Bikes:")
        for rental_id, info in self.rentals.items():
            customer_name = self.customers[info['customer_id']].name
            bike_info = self.bikes[info['bike_id']]
            print(f"Rental ID: {rental_id}, Customer: {customer_name}, Bike: {bike_info.bike_id}, Rented at: {info['rent_time']}")

# Example Usage
if __name__ == "__main__":
    rental_system = RentalSystem()

    rental_system.add_bike("B001", "standard")
    rental_system.add_bike("B002", "electric")
    rental_system.add_bike("B003", "mountain")

    rental_system.add_customer("C001", "Alice")
    rental_system.add_customer("C002", "Bob")

    rental_system.display_available_bikes()

    rental_system.rent_bike("C001", "B001")
    rental_system.rent_bike("C002", "B002")
    rental_system.rent_bike("C001", "B002") # Attempt to rent an unavailable bike

    rental_system.display_available_bikes()
    rental_system.display_rented_bikes()

    rental_system.return_bike(1) # Alice returns B001

    rental_system.display_available_bikes()
    rental_system.display_rented_bikes()
