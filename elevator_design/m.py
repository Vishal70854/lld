from Floor import Floor
from Building import Building
from ElevatorCreator import ElevatorCreator
fl = []
floor1 = Floor(1)
print(floor1.floorNo)

floor2 = Floor(2)
fl.append(floor1)
fl.append(floor2)

building = Building(fl)
print(building.getAllFloors(ElevatorCreator.getAllElevators()))
