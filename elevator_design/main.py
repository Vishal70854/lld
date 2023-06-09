import floor 
import building
# from getElevatorList import obj1

class Main:

  def __init__(self):
    self.floorList = []

    self.floor1 = floor.Floor(1)
    self.floor2 = floor.Floor(2)
    self.floor3 = floor.Floor(3)
    self.floor4 = floor.Floor(4)
    self.floor5 = floor.Floor(5)

    self.floorList.append(self.floor1)
    self.floorList.append(self.floor2)
    self.floorList.append(self.floor3)
    self.floorList.append(self.floor4)
    self.floorList.append(self.floor5)

    self.building = building.Building(self.floorList)
    print('floor', self.floorList)
    
    print('building', self.building)


obj = Main()

