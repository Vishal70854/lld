# from internalButton import InternalButton
import internalButton
import display, status, direction


class ElevatorCar:

  def __init__(self):
    self.id = 0
    self.currFloorNo = 0
    self.elevatorDirection = direction.Direction.UP.name
    self.elevatorState = status.Status.IDLE.name
    self.display = display.Display()
    self.intBtn = internalButton.InternalButton()

  def showDisplay(self):
    self.display.showDisplay()

  def setDisplay(self):
    self.display.setDisplay(self.currFloorNo, self.elevatorDirection)

  def pressButton(self, destFloorNo: int):
    self.intBtn.pressButton(destFloorNo, self)

  def move(self, direction: direction.Direction, destFloorNo: int):
    self.startFloor = self.currFloorNo

    if direction == direction.Direction.UP.name:  # move up
      for i in range(self.startFloor, destFloorNo + 1):
        self.currFloorNo = self.startFloor  # should be i
        self.setDisplay()
        self.showDisplay()

        if (i == destFloorNo):
          return True

    else:  # move down
      for i in range(self.startFloor, destFloorNo - 1):
        self.currFloorNo = self.startFloor
        self.setDisplay()
        self.showDisplay()

        if (i == destFloorNo):
          return True
    return False
