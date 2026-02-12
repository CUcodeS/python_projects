"""
COMP.CS.100 Programming 1 code template
Susanna Kupari, 151625787
susanna.kupari@tuni.fi

User can drive a car in this program.
"""

from math import sqrt


def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(tank_size, gas_to_fill_up, gas_in_tank):
    """
    This function has three parameters which are all FLOATs:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently

    The parameters have to be in this order.
    The function returns one FLOAT that is the amount of gas in the
    tank AFTER the filling up.

    The function does not print anything and does not ask for any
    input.
    """
    current_gas = gas_to_fill_up + gas_in_tank
    if current_gas <= tank_size:
        return float(current_gas)

    elif current_gas > tank_size:
        while current_gas <= tank_size:
            gas_to_fill_up -= 1
        return float(current_gas)

    else:
        return float(current_gas)



def drive(current_x, current_y, target_x, target_y, gas_in_tank, consumption):
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car

    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate

    The return values have to be in this order.
    The function does not print anything and does not ask for any
    input.
    """

    # It might be usefull to make one or two assisting functions
    # to help the implementation of this function.

    if target_x == current_x or target_y == current_y:
        location_p = drive_straight(current_x, current_y, target_x, target_y,
                                  gas_in_tank, consumption)
        return location_p

    else:
        location_s = drive_sideways(current_x, current_y, target_x, target_y,
                                    gas_in_tank, consumption)
        return location_s


def drive_straight(current_x, current_y, target_x, target_y, gas_in_tank,
                   consumption):

    while current_x != target_x or current_y != target_y and gas_in_tank != 0:
        if gas_in_tank >= consumption / 100.0:
            if target_x > current_x:
                current_x += 1
            if target_x < current_x:
                current_x -= 1
            if target_y > current_y:
                current_y += 1
            if target_y < current_y:
                current_y -= 1

            gas_in_tank -= consumption / 100.0

        else:
            break

    return float(gas_in_tank), float(current_x), float(current_y)


def drive_sideways(current_x, current_y, target_x, target_y, gas_in_tank,
                   consumption):
    length_of_hypo = sqrt(abs(current_x - target_x) ** 2 + abs(current_y - target_y ** 2))
    whole_trip_gas = length_of_hypo * (consumption / 100)
    gas_after_trip = gas_in_tank - whole_trip_gas

    while current_x != target_x or current_y != target_y and gas_in_tank != 0:
        print(current_x, current_y)
        if gas_in_tank >= consumption / 100:
            if target_x >= target_y:
                if target_x > current_x:
                    current_x += 1
                if target_x < current_x:
                    current_x -= 1
                if target_y > current_y:
                    current_y += abs((current_y - target_y) / (current_x - target_x))
                if target_y < current_y:
                    current_y -= abs((current_y - target_y) / (current_x - target_x))
            else:
                if target_x > current_x:
                    current_x += abs((current_x - target_x) / (current_y - target_y))
                if target_x < current_x:
                    current_x -= abs((current_x - target_x) / (current_y - target_y))
                if target_y > current_y:
                    current_y += 1
                if target_y < current_y:
                    current_y -= 1
            gas_in_tank -= length_of_hypo / max(target_x, target_y) * consumption / 100

        else:
            break

    return float(gas_in_tank), float(current_x), float(current_y)


def read_number(prompt, error_message="Incorrect input!"):
    """
    This function reads input from the user.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()
