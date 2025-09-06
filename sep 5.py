class Crop:
    def __init__(self, name, season, temp_range, rainfall_range=None):
        self.name = name
        self.season = season  # 'Kharif' or 'Rabi'
        self.temp_range = temp_range
        self.rainfall_range = rainfall_range

    def display(self):
        print("CROP DETAILS")
        print(f"Name: {self.name}")
        print(f"Season: {self.season}")
        print(f"Temperature Range: {self.temp_range[0]}°C to {self.temp_range[1]}°C")
        if self.rainfall_range:
            print(f"Rainfall Range: {self.rainfall_range[0]}mm to {self.rainfall_range[1]}mm")
        print("-" * 30)


def main():
    crops_data = {}   # dictionary to store crops with ID

    while True:
        print("Crop Management System")
        print("1. Add a Crop")
        print("2. View a Crop")
        print("3. Show List of Crops")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            crop_id = input("Enter Crop ID: ")
            if crop_id in crops_data:
                print("Crop with this ID already exists!")
            else:
                name = input("Enter Crop Name: ")
                season = input("Enter Season (Kharif/Rabi): ")
                min_temp = float(input("Enter Minimum Temperature: "))
                max_temp = float(input("Enter Maximum Temperature: "))
                crops_data[crop_id] = Crop(name, season, (min_temp, max_temp))
                print("Crop Added Successfully!")

        elif choice == '2':
            crop_id = input("Enter Crop ID: ")
            if crop_id in crops_data:
                crops_data[crop_id].display()
            else:
                print("Crop not found!")

        elif choice == '3':
            if not crops_data:
                print(" No crops available!")
            else:
                print(" List of Crop IDs:")
                for cid in crops_data:
                    print(f"- {cid} ({crops_data[cid].name})")

        elif choice == '4':
            print(" Exiting Crop Management System")
            break

        else:
            print("Invalid Choice! Please try again.")


# Run the program
main()
