# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.


class Train:
    seats=50
    going="new delhi"
    trainName="Indian Railways."
    def bookTicket(self):
        print(f"there are {self.seats} no of seats in the train running under {self.trainName} going towards {self.going}")

user1=Train()
user1.bookTicket()