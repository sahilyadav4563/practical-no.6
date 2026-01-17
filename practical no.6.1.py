from abc import ABC, abstractmethod
class HotelBooking(ABC):

    @abstractmethod
    def book_room(self):
        pass

class OnlineHotelBooking(HotelBooking):

    def book_room(self):
        print("Hotel room booked successfully")
        print("Guest Name  : Aman")
        print("Room Type   : Deluxe")
        print("Room Number : 205")


if __name__ == "__main__":
    booking = OnlineHotelBooking()
    booking.book_room()
print("F129")
