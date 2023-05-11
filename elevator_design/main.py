from Floor import Floor
from Building import Building
from ElevatorCreator import ElevatorCreator


class Main:

  def __init__(self):
    self.floorList = []

    self.floor1 = Floor(1)
    self.floor2 = Floor(2)
    self.floor3 = Floor(3)
    self.floor4 = Floor(4)
    self.floor5 = Floor(5)

    self.floorList.append(self.floor1)
    self.floorList.append(self.floor2)
    self.floorList.append(self.floor3)
    self.floorList.append(self.floor4)
    self.floorList.append(self.floor5)

    self.building = Building(self.floorList)

  def createElevators(self):
    self.createElevator = ElevatorCreator()
    self.elevatorControllerList = self.createElevator.getAllElevators()
    print(self.elevatorControllerList)


obj = Main()
obj.createElevators()
