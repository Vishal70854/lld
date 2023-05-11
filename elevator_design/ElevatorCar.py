from InternalButton import InternalButton
from Display import Display
from Status import Status
from Direction import Direction


class ElevatorCar:

  def __init__(self):
    self.id = 0
    self.currFloorNo = 0
    self.elevatorDirection = Direction.UP.name
    self.elevatorState = Status.IDLE.name
    self.display = Display()
    self.intBtn = InternalButton()

  def showDisplay(self):
    self.display.showDisplay()

  def setDisplay(self):
    self.display.setDisplay(self.currFloorNo, self.elevatorDirection)

  def pressButton(self, destFloorNo: int):
    self.intBtn.pressButton(destFloorNo, self)

  def move(self, direction: Direction, destFloorNo: int):
    self.startFloor = self.currFloorNo

    if direction == Direction.UP.name:  # move up
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
