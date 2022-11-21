# Import pysonDb
from pysondb import db

# Bind the db location to a variable
collectionEmploye = db.getDb("db/employees.json")
collectionParking = db.getDb("db/parkingInfos.json")


def GetStaffByPlate(immatriculation: str):
    return collectionEmploye.getByQuery({"immatriculation": immatriculation})


def GetStaffByFullName(prenom, nom):
    return collectionEmploye.getByQuery({"prenom": prenom, "nom": nom})


def GetPlacesTaken():
    return collectionParking.getById(354048534950785646)['placesTaken']


def GetMaxPlaces():
    return collectionParking.getById(354048534950785646)['maxPlaces']


def GetParkingCapacity():
    return GetMaxPlaces() - GetPlacesTaken()


def CheckPassPayed(immatriculation: str):
    staff = GetStaffByPlate(immatriculation)
    return staff[0]['stationnement']


def TakeParkingSpot():
    places = GetPlacesTaken()
    if places < GetMaxPlaces():
        placesModified = places + 1
        return collectionParking.updateByQuery({"placesTaken": places}, {"placesTaken": placesModified}, )
    else:
        return "The parking is full"


def EmptyParkingSpot():
    places = GetPlacesTaken()
    if places > 0:
        placesModified = places - 1
        return collectionParking.updateByQuery({"placesTaken": places}, {"placesTaken": placesModified}, )
    else:
        return "Error: the parking lot is empty"


plaque = "y594by"

# print(GetStaffByPlate(plaque))
# print(GetPlaceOccupied())
# TakeParkingSpot()
