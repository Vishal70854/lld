# Use Case Diagram for Book My Show
```
##Actors
-> User
-> Admin
```

```plantuml
@startuml
left to right direction
actor User
actor Admin

rectangle BookMyShow{
    usecase "Search a movie"  as search
    usecase "Book a movie" as book
    usecase "Review a  movie" as review
    usecase "Check availability" as availability
    usecase "Cancel booking" as cancel
    usecase pay
    usecase UPI
    usecase Cash
    usecase "Add a movie" as add
    usecase "Remove a movie" as remove
    usecase "Add a city" as addcity
    usecase "Add a theatre" as addtheatre


    book .> availability : includes
    UPI .> pay : extends
    Cash .> pay : extends

    User --> book
    User --> review
    User --> search
    User --> availability
    User --> cancel

    Admin --> add
    Admin --> remove
    Admin --> addcity
    Admin --> addtheatre
    
}
@enduml
```

# Another simpler way to make use case diagram as shown below:

```plantuml
@startuml
left to right direction
actor User
actor Admin

rectangle BookMyShow{
    User --> (Book a Movie) 
    User --> (Review a Movie)
    User --> (Search a Movie)
    User --> (Cancel a Movie)
    User --> (pay)
    User --> (UPI)
    User --> (Cash)

    (Book a Movie) .> (availability) : includes
    
    (UPI) .> (pay) : extends
    (Cash) .> (pay) : extends

    Admin --> (Add a Movie)
    Admin --> (Remove a Movie)
    Admin --> (Add a City)
    Admin --> (Add a Theatre)
    
}
@enduml
```

# Class Diagram of Book My Show
```
# Class
Cities
Theatre
Halls
Movie
Seats
Shows
Tickets
Coupon
```

```mermaid
classDiagram
    class City{
        - String name;
        -String state;
        -Theatre List<Theatre> theatre;
    }
    City --o Theatre : has a

    class Theatre{
        - String name;
        - String address;
        - Halls List<Halls> halls;
        - Shows List<Shows> shows;
    }
    Theatre --* Halls : has a
    Theatre --o Shows : has a
    class Halls{
        - String name;
        - Seats List<Seats> seats;
        - Features features;
        - Shows List<Shows> shows;
    }
    Halls --* Seat : has a
    Halls --o Shows : has a
    Halls --* Features : has a

    class Seat{
        - String seatno;
        - SeatType type;
    }

    class Shows{
        - Movie movie;
        - DateTime startTime;
        - int duration;
        - String language;
        - Features features;
        - ShowSeats List<ShowSeats> showseats
    }
    Shows --o Movie : has a
    Shows --* ShowSeats : has a
    Shows --o Features : has a

    class Movie{
        - String name;
        - int duration;
        - List<String> language;
        - double rating;
        - List<String> genre;
    }

    class ShowSeats{
        - Shows shows;
        - Seat seat;
        - BookingStatus status;
    }
    ShowSeats --o TicketStatus : has a

    class Ticket{
        - double amount;
        - List<ShowSeats> showseats;
        - TicketStatus status;
        - Payment payment;
        - Coupon coupon;
    }
    Ticket --o ShowSeats : has a

    class Payment{
        - PaymentType ptype;
        - double cost;
        - PaymentStatus status;
        - Ticket ticket;
    }
    Payment --o Ticket : has a

    class Features{
        <<enumeration>>
        DOLBY
        3D
        2D
    }
    class TicketStatus{
        <<enumeration>>
        BOOKED
        PENDING
        CANCELLED
    }
```