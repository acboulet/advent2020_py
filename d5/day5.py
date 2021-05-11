import numpy as np
from math import ceil

def process(file_name):
    """
    Purpose:
        Adds every ticket from a txt file into a list
    Pre:
        :param file_name: name of .txt file
    Return:
        List of all tickets in the original file
    """
    in_file = open(file_name, "r")
    tickets = []
    for line in in_file:
        tickets.append(line.strip())
    return tickets

def challenge_1(ticket):
    """
    Purpose:
        Calculates the seat ID for a given ticket
    Pre:
        :param ticket: Ticket string on Boarding pass
    Return:
        Seat ID calculation of the ticket
    """
    row = halve_value("row", ticket)
    col = halve_value("col", ticket)
    return row * 8 + col

def halve_value(seat, ticket):
    """
    Purpose:
        Used by seat_ID() to caculate row/col locations by keeping lower or upper half of
        potential locations.
    Pre:
        :param seat: Whether you are calculating for the "row" or "col"
    Return:
        The seat location within the row or column
    """
    if seat == "row":
        start, end, low, high, bot= 0, 127, 0, 6, "F"
    else:
        start, end, low, high, bot = 0, 7, 7, 9, "L"

    for n in range(low, high):
        if ticket[n] == bot:
            end = (start + end)//2
        else:
            start = ceil((end + start) / 2)
    if ticket[high] == bot:
        return start
    else:
        return end

def challenge_2(ticket_list):
    """
    Purpose:
        Find the seat_ID that is not present in the given list of tickests
    Pre:
        :param ticket_list: List of tickets with missing ticket
    Return:
        Seat ID for your ticket (int), which is the missing ticket
    """
    # Calculate the seat_ID for every ticket, and place in a sorted list
    plane = []
    for ticket in ticket_list:
        plane.append(challenge_1(ticket))
    plane.sort()
    # Check that every seat_ID is sequential, and return the empty spot
    for n in range(len(plane)):
        if plane[n+1] - plane[n] !=1:
            return (plane[n] +1)


if __name__ == "__main__":
    tickets_ex = process("d5/day5_input.txt")
    max_seat_ID = 0
    for ticket in tickets_ex:
        new_seat_ID = challenge_1(ticket)
        if new_seat_ID > max_seat_ID:
            max_seat_ID = new_seat_ID
    print(max_seat_ID)

    print(challenge_2(tickets_ex))
