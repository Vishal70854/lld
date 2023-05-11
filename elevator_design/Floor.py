from ExternalButtonDispatcher import ExternalButtonDispatcher
from Direction import Direction


class Floor:

  def __init__(self, floorNo: int):
    self.floorNo = floorNo
    self.extBtnDsp = ExternalButtonDispatcher()  # object

  def pressButton(self, direction: Direction):
    self.extBtnDsp.submitExternalRequest(self.floorNo, direction)

