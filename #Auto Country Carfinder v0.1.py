#Auto Country Carfinder v0.1

allowedVehiclesList = ["Ford F-150", "Chevrolet Silverado", "Telsa CyberTruck", "Toyota Tundra", "Nissan Titan"]

print("**********************************")
print("AutoCountry Vehicle Finder v0.1")
print("**********************************\n")

print("Please Enter the following number below from the following menu:\n")
print("1. PRINT all Authorized Vehicles")
print("2. Exit\n")

response = int(input("Enter here: "))

while(True):
      
    if (response == 1):
        print("\n")
        print(f'The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
        print("\n")
        for answer in allowedVehiclesList:
             print(answer)
        print("\n")
        print("**********************************")
        print("AutoCountry Vehicle Finder v0.1")
        print("**********************************\n")
        print("Please Enter the following number below from the following menu:\n")
        print("1. PRINT all Authorized Vehicles")
        print("2. Exit\n")
        response = int(input("Enter here: "))
        print("\n")
        continue;

    if(response == 2):
        print(f'Thank you for using the AutoCountry Vehicle Finder, good-bye!')
        break;



