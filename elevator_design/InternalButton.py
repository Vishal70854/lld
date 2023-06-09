# from ElevatorCar import ElevatorCar
import internalButtonDispatcher
import elevatorCreator

class InternalButton:

  def __init__(self):
    self.elevatorList = elevatorCreator.ElevatorCreator()
    self.intBtnDsp = internalButtonDispatcher.InternalButtonDispatcher(self.elevatorList.getAllElevators())
    self.availableButtons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  def pressButton(self, destFloorNo: int, elevatorCar ):
    if destFloorNo in self.availableButtons:
      self.intBtnDsp.submitInternalRequest(destFloorNo, elevatorCar)
    else:
      print("Invalid Button. Kindly press from 1 to 10")
