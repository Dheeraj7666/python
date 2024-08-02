class Vehicle:
    def __init__(self, vehic_id, make, model, year, category):
        self.vehicle_id = vehic_id
        self.category = category
        self.year = year
        self.model = model
        self.make = make

    def __repr__(self):
        return f"({self.vehicle_id}, {self.make}, {self.model}, {self.year}, {self.category})"

class VehicleRentalSystem:
    def __init__(self):
        self.vehicles = []
        self.vehicle_ids = set()

    def add_vehicle(self, vehicle):
        if vehicle.vehicle_id not in self.vehicle_ids:
            self.vehicles.append(vehicle)
            self.vehicle_ids.add(vehicle.vehicle_id)
            print(f"Vehicle {vehicle.vehicle_id} added.")
        else:
            print(f"Vehicle {vehicle.vehicle_id} already exists.")

    def remove_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                self.vehicles.remove(vehicle)
                self.vehicle_ids.remove(vehicle_id)
                print(f"Vehicle {vehicle_id} removed.")
                return
        print(f"Vehicle {vehicle_id} not found.")

    def search_vehicles(self, search_term):
        search_term_lower = search_term.lower()
        search_results = []
        for vehicle in self.vehicles:
            if search_term_lower in vehicle.make.lower() or search_term_lower in vehicle.model.lower():
                search_results.append(vehicle)
            return search_results

    def categorize_vehicles(self):
        categorized_vehicles = {}
        for vehicle in self.vehicles:
            categorized_vehicles.setdefault(vehicle.category, []).append(vehicle)
        return categorized_vehicles

    def list_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle)

car = VehicleRentalSystem()

def choice_method(choice):
    if choice == 1:
        vehicle_id = int(input("Enter vehicle ID: "))
        make = input("Enter make: ")
        model = input("Enter model: ")
        year = int(input("Enter year: ")) 
        category = input("Enter category: ")
        vehicle = Vehicle(vehicle_id, make, model, year, category)
        car.add_vehicle(vehicle)
        enter_choice()  
    
    elif choice == 2:
        vehicle_id = int(input("Enter vehicle ID to remove: "))
        car.remove_vehicle(vehicle_id)
        enter_choice()  
        
    elif choice==3:
        search_term = input("Enter search term (make or model): ")
        search_results = car.search_vehicles(search_term)
        for vehicle in search_results:
            print(vehicle)
        enter_choice()  
    
    elif choice ==4:
        car.list_vehicles()
        enter_choice()  
        
    elif choice ==5:
        categorized_vehicles = car.categorize_vehicles()
        for category, vehicles in categorized_vehicles.items():
            print(f"{category}: {vehicles}")
        enter_choice()  

    elif choice==6:
        print("exiting...")
        exit()
        
    elif choice == 7 :
        print("exiting")
        v = vehicle()
        v.get_file()
        exit()
    else:
        print("invalid choice")
        enter_choice()

def enter_choice():
    print("\nVehicle Rental System")
    print("1. Add Vehicle")
    print("2. Remove Vehicle")
    print("3. Search Vehicles")
    print("4. List All Vehicles")
    print("5. Categorize Vehicles")
    print("6. Exit")
    choice = int(input("enter choice : "))
    choice_method(choice)  

enter_choice()
choice = int(input("enter choice : "))
choice_method(choice)








