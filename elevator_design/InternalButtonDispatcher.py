# from elevatorCar import ElevatorCar
from typing import List
import elevatorController

class InternalButtonDispatcher:

  def __init__(self, elevatorControllerList : List[elevatorController.ElevatorController]):
    self.elevatorControllerList = elevatorControllerList

  def submitInternalRequest(self, destFloorNo: int, elevatorCar):
    for elevator in self.elevatorControllerList:
      if elevator.id == destFloorNo:
        # call ElevatorController class method
        elevator.submitInternalRequest(elevator.currentFloorNo, destFloorNo, elevatorCar)
