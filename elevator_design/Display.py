# from direction import Direction
import direction


class Display:

  def __init__(self, currFloorNo: int):
    self.currFloorNo = currFloorNo
    self.direction = direction.Direction.UP.name

  def setDisplay(self, currFloorNo: int, direction: direction.Direction):
    self.currFloorNo = currFloorNo
    self.direction = direction

  def showDisplay(self):
    print(f'Current floor is {self.currFloorNo}')
    print(f'Current Direction is {self.direction}')
  
# testing 
# d = Display(1)
# d.showDisplay()
