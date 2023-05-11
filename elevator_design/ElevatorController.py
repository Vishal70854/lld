from heapq import heapify, heappush, heappop
from Direction import Direction
from ElevatorCar import ElevatorCar

class ElevatorController:

  def __init__(self, elevatorCar : ElevatorCar):
    self.elevatorCar = elevatorCar
    self.minHeap = heapify([])
    self.maxHeap = heapify([]) 

  # internal request method
  def submitInternalRequest(self, currFloorNo : int, destFloorNo : int, elevatorCar: ElevatorCar):
    if elevatorCar.elevatorDirection.UP.name:
      heappush(self.minHeap, currFloorNo)
    else:  # push in max heap
      heappush(self.maxHeap, -1 * currFloorNo)

    self.controlElevator()

  # external request method
  # def submitExternalRequest(self, currFloorNo: int, direction: Direction):
  #   if direction == Direction.UP:  # push in min heap
  #     heappush(self.minHeap, currFloorNo)
  #   else:  # push in max heap
  #     heappush(self.maxHeap, -1 * currFloorNo)

  def controlElevator(self):
    self.currentFloor = self.elevatorCar.currFloorNo
    self.flag = True
    
    while self.flag:
      # MOVE UP USING MIN HEAP
      while len(self.minHeap) > 0:
        self.floorValFromHeap = heappop(self.minHeap)
        if self.currentFloor == self.floorValFromHeap:
          print(f"Going Up! We have reached {self.floorValFromHeap} floor")

        elif self.currentFloor < self.floorValFromHeap:
          self.elevatorCar.move(Direction.UP, self.floorValFromHeap)
        else:
          heappush(self.minHeap, self.floorValFromHeap)

      while len(self.maxHeap) > 0:
        # MOVE DOWN USING MAXHEAP
        self.floorValFromHeap = (-1 * heappop(self.maxHeap))
        if self.currentFloor == self.floorValFromHeap:
          print(f"Going Down! We have reached {self.floorValFromHeap} floor")

        elif self.currentFloor > self.floorValFromHeap:
          self.elevatorCar.move(Direction.UP, self.floorValFromHeap)
        else:
          heappush(self.maxHeap, -1 * self.floorValFromHeap)

      # no request in elevator
      if not self.minHeap and not self.maxHeap:
        self.flag = False
