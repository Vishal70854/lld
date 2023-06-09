import direction 

class ExternalButtonDispatcher:

  def __init__(self, listofElevatorController):
    self.listofElevatorController = listofElevatorController

    def submitExternalRequest(self, floorNo: int, direction: direction.Direction):
      for elevator in self.listOfController:
        if elevator.id == floorNo:
          elevator.submitExternalRequest(floorNo, direction)
