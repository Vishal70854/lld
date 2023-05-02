### Class
```
Building
Floor
ExternalButton
ExternalButtonDispatcher
OddEvenDispatcher
FixedFloorDispatcher
ElevatorController
Elevator
Display
InternalButton
InternalButtonDispatcher

```

### Methods/Functions
```

```

## Class diagram of Elevator system
```mermaid
classDiagram
    class Building{
        -List[Floor] floor
    }
    Building *-- Floor : has a

    class Floor{
        -int id
    }
    Floor *-- ExternalButton : has a

    class ExternalButton{
        -ExternalButtonDispatcher obj
        -bool press(floor, direction)
    }
    ExternalButton *-- ExternalButtonDispatcher : has a

    class ExternalButtonDispatcher{
        List[ElevatorCount] elvCount
        -bool submitRequest(floor, direction)
    }
    ExternalButtonDispatcher *-- ElevatorController : has a

    class OddEvenDispatcher{
        # some algo
    }
    OddEvenDispatcher <|-- ExternalButtonDispatcher : is a

    class FixedFloorDispatcher{
        #some algo
    }
    FixedFloorDispatcher <|-- ExternalButtonDispatcher : is a

    class InternalButton{
        -InternalButtonDispatcher obj
        - bool pressButton(floor, direction)
    }
    InternalButton *-- InternalButtonDispatcher : has a
    
    class InternalButtonDispatcher{
        -List[ElevatorController] lst
        -bool SubmitRequest(id)
    }
    InternalButtonDispatcher *-- ElevatorController : has a

    class Elevator Controller{
        -Elevator elevator
        # min heap algo
        # max heap algo
        # Queue
        - bool acceptNewRequest(floor, direciton)
        - bool control()
    }
    ElevatorController *-- Elevator : has a

    class Elevator{
        -int id
        -Display display
        - int currentFloor
        -Direction direction
        -Status status
        -InternalButton internalbtn
        -Door door
        -bool move(int destination, int direction)
    }
    Elevator *-- Display : has a
    Elevator *-- Direction : has a
    Elevator *-- Status : has a
    Elevator *-- InternalButton : has a
    Elevator *-- Door : has a

    class Display{
        - int floor
        - Direction direction

    }
    Display *-- Direction : has a
    class Direction{
        <<enum>>
    }
    class Status{
        <<enum>>
    }
    class Door{
        <<enum>>
    }


```