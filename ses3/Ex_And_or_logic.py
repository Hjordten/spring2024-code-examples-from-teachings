# Ex: And / or logic
# You are programming a room reservation system for a hotel. The system should check if a room can be reserved based on the following criteria:
#
# The room can be reserved if it is not already booked and the number of guests does not exceed the room’s capacity.
#
# There are two types of rooms: standard and deluxe.
#
# A standard room can accommodate up to 2 guests, while a deluxe room can accommodate up to 4 guests.
#
# The reservation request will provide the room type (either “standard” or “deluxe”) and the number of guests.
#
# The system should return True if the reservation can be made and False otherwise.
#
# Your task is to write a Python function that takes the room number and the number of guests as inputs and returns whether the reservation can be made.
#
# You should have some kind of datastructure for storing if the room is awaliable or not.
#
# Again, you should write this in a straight forward approach, and in a python one-liner aaproach.
#
# Solution: When you are done, copy/paste this exercise description + your solution into ChatGpt, asking it for feed back on how you solved the problem and where you could improve your solution.

# Initialize a dictionary to track room availability
room_availability = {
    1: True,  # Room  1 is available
    2: False  # Room  2 is booked
    # Add other rooms as needed
}

# Function to check room availability
def can_reserve_room(room_number, room_type, num_guests):
    # Check if the room is available and if the number of guests fits the room type
    if room_availability.get(room_number, False) and (
        (room_type == "standard" and num_guests <=  2) or
        (room_type == "deluxe" and num_guests <=  4)
    ):
        return True
    return False

# Example usage
print(can_reserve_room(1, "standard",  2))  # Returns True if room  1 is a standard room and has  2 guests
print(can_reserve_room(2, "deluxe",  4))  # Returns False because room  2 is booked


def can_reserve_room(room_number, room_type, num_guests):
    return room_availability.get(room_number, False) and ((room_type == "standard" and num_guests <=  2) or (room_type == "deluxe" and num_guests <=  4))
