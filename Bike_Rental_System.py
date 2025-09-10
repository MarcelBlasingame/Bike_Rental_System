import datetime

class BikeRental:
    def __init__(self, mountain_bikes, road_bikes, touring_bikes):
        self.inventory = {
            "Mountain": mountain_bikes,
            "Road": road_bikes,
            "Touring": touring_bikes
        }
        self.daily_revenue = 0
        self.daily_bikes_rented = 0

    def display_inventory(self):
        print("\nCurrent Inventory:")
        for bike_type, count in self.inventory.items():
            print(f"{bike_type} Bikes: {count}")

    def rent_bike(self, bike_type, num_bikes, rental_basis):
        if bike_type not in self.inventory:
            print("Invalid bike type.")
            return None
        if num_bikes > self.inventory[bike_type]:
            print(f"Not enough {bike_type} bikes available.")
            return None

        self.inventory[bike_type] -= num_bikes
        self.daily_bikes_rented += num_bikes

        now = datetime.datetime.now()
        print(f"You have rented {num_bikes} {bike_type} bike(s) on a {rental_basis} basis.")
        return now

    def return_bike(self, rental_time, bike_type, num_bikes, rental_basis, coupon_code):
        if rental_time is None:
            print("You did not rent any bikes.")
            return

        self.inventory[bike_type] += num_bikes
        now = datetime.datetime.now()
        rental_period = (now - rental_time).total_seconds() / 3600  # in hours

        if rental_basis == "hourly":
            rate = 5
        elif rental_basis == "daily":
            rate = 20 * 24  # daily rate converted to hourly
        elif rental_basis == "weekly":
            rate = 60 * 24 * 7  # weekly rate converted to hourly
        else:
            print("Invalid rental basis.")
            return

        total_price = (rental_period / (24 if rental_basis in ["daily", "weekly"] else 1)) * rate * num_bikes

        # Apply family discount if applicable
        if 3 <= num_bikes <= 5:
            print("Family discount applied: 25% off.")
            total_price *= 0.75

        # Apply coupon discount if applicable
        if coupon_code.endswith("***BBP"):
            print("Coupon discount applied: 10% off.")
            total_price *= 0.9

        self.daily_revenue += total_price

        print("\nInvoice:")
        print(f"Customer rented {num_bikes} {bike_type} bike(s) on a {rental_basis} basis.")
        print(f"Rental Period: {rental_period:.2f} hours")
        print(f"Total Price: ${total_price:.2f}")

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.rental_time = None
        self.bike_type = ""
        self.num_bikes = 0
        self.rental_basis = ""

    def request_bike(self):
        self.bike_type = input("Enter bike type (Mountain, Road, Touring): ").title()
        try:
            self.num_bikes = int(input("Enter number of bikes to rent: "))
        except ValueError:
            print("Invalid input. Enter a number.")
            return None

        self.rental_basis = input("Enter rental basis (hourly, daily, weekly): ").lower()
        if self.rental_basis not in ["hourly", "daily", "weekly"]:
            print("Invalid rental basis.")
            return None
        return self.bike_type, self.num_bikes, self.rental_basis

    def return_bike(self):
        coupon_code = input("Enter coupon code (if any): ")
        return self.bike_type, self.num_bikes, self.rental_basis, coupon_code

# Main application
def main():
    print("Welcome to the Bike Rental Shop!")
    mountain_bikes = int(input("Enter initial inventory for Mountain Bikes: "))
    road_bikes = int(input("Enter initial inventory for Road Bikes: "))
    touring_bikes = int(input("Enter initial inventory for Touring Bikes: "))

    shop = BikeRental(mountain_bikes, road_bikes, touring_bikes)

    while True:
        print("\nNavigation Menu:")
        print("1. New Customer Rental")
        print("2. Rental Return")
        print("3. Show Inventory")
        print("4. End of Day")
        print("5. Exit Program")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            customer_id = input("Enter customer ID: ")
            customer = Customer(name, customer_id)

            request = customer.request_bike()
            if request:
                bike_type, num_bikes, rental_basis = request
                rental_time = shop.rent_bike(bike_type, num_bikes, rental_basis)
                if rental_time:
                    customer.rental_time = rental_time

        elif choice == "2":
            if 'customer' not in locals():
                print("No active rentals to return.")
                continue

            return_details = customer.return_bike()
            if return_details:
                bike_type, num_bikes, rental_basis, coupon_code = return_details
                shop.return_bike(customer.rental_time, bike_type, num_bikes, rental_basis, coupon_code)

        elif choice == "3":
            shop.display_inventory()

        elif choice == "4":
            print("\nEnd of Day Report:")
            print(f"Total Bikes Rented: {shop.daily_bikes_rented}")
            print(f"Total Revenue: ${shop.daily_revenue:.2f}")

        elif choice == "5":
            print("Thank you for using the Bike Rental Shop application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

