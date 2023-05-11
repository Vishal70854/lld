class Building:

  def __init__(self, floorlist):
    self.floorlist = floorlist

  def addFloors(self, floor):
    self.floorlist.append(floor)

  def removeFloors(self, floor):
    self.floorlist.remove(floor)

  def showFloors(self):
    return self.floorlist
