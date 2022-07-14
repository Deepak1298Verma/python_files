data = {
    "ApartmentBuilding":{
        "Address":{
            "HouseNumber": 5,
            "Street": "DataStreet",
            "ZipCode": 5100
        },
        "Apartments":[
            {
                "Number": 1,
                "Price": 500,
                "Residents": [
                    {
                        "Name": "Bob"
                    },
                    {
                        "Name": "Alice",
                        "Age": 42
                    }
                ]
            },
            {
                "Number": 2,
                "Price": 750,
                "Residents": [
                    {
                        "Name": "Jane",
                        "Age": 43
                    },
                    {
                        "Name": "William",
                        "Age": 42
                    }
                ]
            },
            {
                "Number": 3,
                "Price": 1000,
                "Residents": []
            }
        ]      
    }
}


# first_resident = data["ApartmentBuilding"]["Apartments"][0]["Residents"][0]["Name"]
# print(first_resident)

resident_names = []

apartments = data["ApartmentBuilding"]["Apartments"]

for i in apartments:
    price = apartments["Price"]
    for j in price:
        resident_names.append(j)
print(resident_names)








for apartment in apartments:
    resident = apartment["Residents"]
    for residents in resident:
        name = residents["Name"]
        resident_names.append(name)
# print(resident_names)

for apartment in apartments:
    resident = apartment["Residents"]
    for residents in resident:
        age = resident.get('age',"N/a")
        resident_names.append(age)
# print(resident_names)

