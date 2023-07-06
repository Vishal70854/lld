```
Elevator design:

ElevatorCar: Represents an elevator car that moves between floors and carries passengers. It has attributes such as carNumber, currentFloor, direction, status, internalButtons and passengers. It has behaviors such as addInternalButton, addPassenger, removePassenger, move, stop and resume.
ElevatorController: Represents an elevator controller that controls the movement of the elevator cars and handles the requests from the floors. It has attributes such as building, elevatorCars and requests. It has behaviors such as addElevatorCar, addRequest, processRequests, selectCar and handlePassengers.
Floor: Represents a floor in the building that has external buttons and passengers waiting for the elevator. It has attributes such as floorNumber, externalButtons and passengers. It has behaviors such as addExternalButton, addPassenger and removePassenger.
InternalButton: Represents an internal button inside an elevator car that allows passengers to select their destination floor. It has attributes such as floorNumber, car and status. It has a behavior such as press.
ExternalButton: Represents an external button on a floor that allows passengers to request an elevator in a certain direction. It has attributes such as floorNumber, direction and status. It has a behavior such as press.
Building: Represents a building that contains floors and an elevator controller. It has attributes such as name, address, numberOfFloors, floors and controller. It has a behavior such as addFloor.
Passenger: Represents a person who uses the elevator system to go from one floor to another. It has attributes such as name, origin, destination and direction. It has behaviors such as enter and exit.

```

```mermaid
classDiagram
    ElevatorCar "1" -- "0..*" InternalButton : has
    ElevatorCar "1" -- "0..*" Passenger : carries
    ElevatorController "1" -- "0..*" ElevatorCar : controls
    ElevatorController "1" -- "1" Building : belongs to
    Floor "1" -- "0..*" ExternalButton : has
    Floor "1" -- "0..*" Passenger : waits on
    Building "1" -- "0..*" Floor : contains
    InternalButton "1" -- "1" ElevatorCar : belongs to
    ExternalButton "1" -- "1" Floor : belongs to
    Passenger -- ElevatorCar : enters / exits 
    Passenger -- Floor : enters / exits 
    
    class ElevatorCar {
        carNumber: int
        currentFloor: int
        direction: string or None
        status: string
        addInternalButton(button: InternalButton): void
        addPassenger(passenger: Passenger): void
        removePassenger(passenger: Passenger): void
        move(): void
        stop(): void
        resume(): void
    }
    class ElevatorController {
        building: Building
        elevatorCars: list of ElevatorCar
        requests: list of tuples (floorNumber, direction)
        addElevatorCar(car: ElevatorCar): void
        addRequest(floorNumber: int, direction: string): void
        processRequests(): void
        selectCar(floorNumber: int, direction: string): ElevatorCar or None
        handlePassengers(car: ElevatorCar): void 
    }
    class Floor {
        floorNumber: int
        externalButtons: list of ExternalButton
        passengers: list of Passenger
        addExternalButton(button: ExternalButton): void
        addPassenger(passenger: Passenger): void
        removePassenger(passenger: Passenger): void
    }
    class InternalButton {
        floorNumber: int
        car: ElevatorCar
        status: string or None
        press(): void 
    }
    class ExternalButton {
        floorNumber: int
        direction: string
        status: string or None
        press(): void 
    }
    class Building {
        name: string
        address: string
        numberOfFloors: int
        floors: list of Floor
        controller: ElevatorController
        addFloor(floor: Floor): void
    }
    class Passenger {
        name: string
        origin: int
        destination: int
        direction: string or None
        enter(car: ElevatorCar): void
        exit(car: ElevatorCar): void 
    }
```
