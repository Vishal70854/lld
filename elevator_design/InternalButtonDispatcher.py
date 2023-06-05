# from ElevatorCar import ElevatorCar
from typing import List
from elevatorController import ElevatorController

class InternalButtonDispatcher:

  def __init__(self, elevatorControllerList : List[ElevatorController]):
    self.elevatorControllerList = elevatorControllerList

  def submitInternalRequest(self, destFloorNo: int, elevatorCar):
    for elevator in self.elevatorControllerList:
      if elevator.id == destFloorNo:
        # call ElevatorController class method
        elevator.submitInternalRequest(elevator.currentFloor, destFloorNo, elevatorCar)
