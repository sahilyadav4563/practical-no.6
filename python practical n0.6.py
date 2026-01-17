from abc import ABC, abstractmethod

# Abstract class
class TrainTicket(ABC):

    @abstractmethod
    def book_ticket(self):
        pass
class OnlineBooking(TrainTicket):

    def book_ticket(self):
        print("Train ticket booked successfully")
        print("Passenger Name : Rahul")
        print("Train Number   : 12345")
        print("Seat Number    : A12")

if __name__ == "__main__":
    ticket = OnlineBooking()
    ticket.book_ticket()
print("sahil yadav")
