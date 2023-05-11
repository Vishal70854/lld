from ElevatorCar import ElevatorCar


class InternalButtonDispatcher:

  def __init__(self, elevatorControllerList):
    self.elevatorControllerList = elevatorControllerList

  def submitInternalRequest(self, destFloorNo: int, elevatorCar: ElevatorCar):
    for elevator in self.listofElevatorController:
      if elevator.id == destFloorNo:
        # call ElevatorController class method
        elevator.submitInternalRequest(elevator.currentFloor, destFloorNo,
                                       elevatorCar)
