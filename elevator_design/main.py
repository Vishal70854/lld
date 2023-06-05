from floor import Floor
from building import Building
# from getElevatorList import obj1

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
    print('floor', self.floorList)
    
    print('building', self.building)

  # def createElevators(self):
  #   self.createElevator = obj1
  #   print('obj', obj1)
  #   self.elevatorControllerList = obj1.getAllElevators()
  #   print('elevatorList',self.elevatorControllerList)


obj = Main()
# obj.createElevators()

