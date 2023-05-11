from Direction import Direction


class Display:

  def __init__(self, currFloorNo: int):
    self.currFloorNo = currFloorNo
    self.direction = Direction.UP.name

  def setDisplay(self, currFloorNo: int, direction: Direction):
    self.currFloorNo = currFloorNo
    self.direction = direction

  def showDisplay(self):
    print(f'Current floor is {self.currFloorNo}')
    print(f'Current Direction is {self.direction}')
