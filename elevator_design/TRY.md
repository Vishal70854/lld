```
Parking lot design:

ParkingLot: Represents a parking lot that contains parking floors and parking gates. It has attributes such as name, address, parkingFloors, entryGates and exitGates. It has behaviors such as addParkingFloor, addEntryGate, addExitGate, getAvailableSpots, issueTicket and processPayment.
ParkingFloor: Represents a parking floor that contains parking spots. It has an attribute such as floorNumber and parkingSpots. It has behaviors such as addParkingSpot and getAvailableSpots.
ParkingSpot: Represents a parking spot that can fit a certain type of vehicle and can be occupied or free. It has attributes such as spotNumber, spotType, status and ticket. It has behaviors such as isFree, canFit, occupy and free.
ParkingTicket: Represents a parking ticket that is issued to a vehicle when it enters the parking lot and is used to calculate the amount to be paid when it exits. It has attributes such as ticketID, spot, vehicle, entryTime, entryGate, entryOperator and invoice.
Invoice: Represents an invoice that is generated from a parking ticket and shows the amount to be paid based on the duration and the spot type. It has attributes such as invoiceID, exitTime, ticket, amount, payment and paymentStatus. It has a behavior such as calculateAmount.
Payment: Represents a payment that is made by the vehicle owner using a certain type of payment method. It has attributes such as amount, ticket, type, status and time. It has a behavior such as process.
Vehicle: Represents a vehicle that enters and exits the parking lot. It has attributes such as licensePlate and vehicleType.
ParkingGate: Represents a parking gate that allows vehicles to enter or exit the parking lot. It has attributes such as gateNumber and currentAttendant. It has behaviors such as assignAttendant and open.
ParkingAttendant: Represents a person who works at a parking gate and issues or collects tickets from vehicles. It has attributes such as name and email.

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
