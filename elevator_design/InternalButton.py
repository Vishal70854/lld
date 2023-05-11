from ElevatorCar import ElevatorCar
from InternalButtonDispatcher import InternalButtonDispatcher


class InternalButton:

  def __init__(self):
    self.intBtnDsp = InternalButtonDispatcher()
    self.availableButtons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  def pressButton(self, destFloorNo: int, car):
    if destFloorNo in self.availableButtons:
      self.intBtnDsp.submitInternalRequest(destFloorNo, car)
    else:
      print("Invalid Button. Kindly press from 1 to 10")
