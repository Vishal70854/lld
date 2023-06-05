from direction import Direction


class ExternalButtonDispatcher:

  def __init__(self, listofElevatorController):
    self.listofElevatorController = listofElevatorController

    def submitExternalRequest(self, floorNo: int, direction: Direction):
      for elevator in self.listOfController:
        if elevator.id == floorNo:
          elevator.submitExternalRequest(floorNo, direction)
