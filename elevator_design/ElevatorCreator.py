from ElevatorCar import ElevatorCar
from ElevatorController import ElevatorController


class ElevatorCreator:

  def __init__(self):
    self.elevatorControllerList = []  # list of Elevators

    # create an elevatorCar object
    self.elevatorcreator1 = ElevatorCar()
    self.elevatorcreator1.id = 1
    self.controller1 = ElevatorController(self.elevatorcreator1)

    # create an elevatorCar object
    self.elevatorcreator2 = ElevatorCar()
    self.elevatorcreator2.id = 2
    self.controller2 = ElevatorController(self.elevatorcreator2)

    # add list of elevatorController in elevatorControllerList
    self.elevatorControllerList.append(self.controller1)
    self.elevatorControllerList.append(self.controller2)

  def getAllElevators(self):
    return self.elevatorControllerList
  
el = ElevatorCreator()
print(el.getAllElevators())