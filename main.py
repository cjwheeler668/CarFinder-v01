#Menu
def menu():
  print("*******************************")
  print("AutoCountry Vehicle Finder v0.1")
  print("*******************************")
  print("Plese enter the following number bellow from the following menu: ")
  print("[1] PRINT all Authorized Vehicles")
  print("[2] Exit")

#Print menu
menu()
#Give option to choose
option = int(input("Enter your option: "))
#Option 1 is chosen
if option == 1:
  #Array of authorized vehicles
  AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
  print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
  #Prints the array
  for AllowedVehicles in AllowedVehiclesList:
    print(AllowedVehicles)
  #Gives menu option to choose
  menu()
  option = int(input("Enter your option: "))
#Option 2 is chosen
elif option == 2:
  print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
