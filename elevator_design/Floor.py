# from ExternalButtonDispatcher import ExternalButtonDispatcher
import direction 


class Floor:

  def __init__(self, floorNo: int):
    self.floorNo = floorNo
    # self.extBtnDsp = ExternalButtonDispatcher()  # object

  # def pressButton(self, direction: direction.Direction):
  #   self.extBtnDsp.submitExternalRequest(self.floorNo, direction)


f = Floor(1)
# print(f)