"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 151625787
Name:       Susanna Kupari
Email:      susanna.kupari@tuni.fi


Project 3: User inputs a filename and program handles it with different actions
that are given by user. File includes cities, destinations of cities and
distances between city and destination. User can investigate the contents of
the file by entering "display". By giving command "add" user can add new
connexion to file. Action "remove" removes the given connexion from file if it
exists. "Neighbour" command asks user to input a city and prints a table of
cities which has direct connexion to departure city. Also distances between
departure city and destination city are given. Command "route" asks user to
input departure and destination cites and finds the route between these cites
if there aren't direct connexion. By entering empty line program running ends.
"""


def get_all_cities(distance_data):
    """
    Function creates a list of all departures and destinations in
    <distance_data> and returns it.

    :param distance_data: dict{str:{str:int}}, includes all connexion data
    :return: list[str], returns a list of all cities in <distance_data>
    """
    all_cities = []

    for town in distance_data:
        all_cities.append(town)

    # Key is a departure city in distance_data. Function gets the payload of
    # key and stores it to variable <city>. Because <city> is also a dictionary
    # function stores the payload of <city> to variable <city_key> and adds it
    # to list if it is not there already.
    for key in distance_data:
        city = distance_data.get(key)
        for city_key in city.keys():
            if city_key not in all_cities:
                all_cities.append(city_key)

    return all_cities


def calculate_route(distance_data, departure, destination):
    """
    Function calls function <find_route()> to find route for departure and
    destination cities. Return value is a list of cities which is returned for
    calling function. Function calculates the total number of kilometers of the
    route and returns the value.

    :param distance_data: dict{str:{str:int}}, includes all connexion data
    :param departure: str, given departure city for route
    :param destination: str, given destination city for route
    :return: list[str], int, list of all route connexions and total number of
             kilometers of the route.
    """

    route = find_route(distance_data, departure, destination)

    sum_kilometers = 0
    index = 0

    if departure == destination:
        sum_kilometers = 0

    # If departure and destination cities are not same city function sums the
    # distance between all cities (<sum_kilometers>). <Index> is the index
    # number of the city in list. By getting one distance after another and
    # summing it to <sum_kilometers> total amount of kilometers of route is
    # obtained. <Index> raises while it is smaller than length of list route -1
    # so the error list index out of range is avoided.
    else:
        while index < len(route) - 1:
            sum_kilometers += int(
                distance_data[route[index]][route[index + 1]])
            index += 1

    return route, sum_kilometers


def print_route(distance_data):
    """
    Function calls function <get_all_cities to get all departures and
    destinations in <distance_data> and prints the found route between given
    connexion and calls function <calculate_route()> to sum the kilometers
    between all connexions. Error messages are printed if <departure> is not
    found or if there are no route between <departure> and <distance>.

    :param distance_data: dict{str:{str:int}}, includes all connexions
    """

    departure = input("Enter departure city: ")
    # By calling function <get_all_cities()> program makes sure that entered
    # cities exist in <distance_data>.
    if departure in get_all_cities(distance_data):
        destination = input("Enter destination city: ")
        if destination in get_all_cities(distance_data):

            route, sum_kilometers = \
                calculate_route(distance_data, departure, destination)

            if len(route) > 0:
                print(f"{'-'.join(route)} ({sum_kilometers} km)")

            else:
                print(f"No route found between '{departure}' and"
                      f" '{destination}'.")

        else:
            print(f"No route found between '{departure}' and '{destination}'.")

    else:
        print(f"Error: '{departure}' is unknown.")


def find_neighbours(distance_data):
    """
    Function asks user to enter city and calls functions <fetch_neighbours()>
    and <distance_to_neighbour()> to find and print a table that includes
    destinations that have direct connexion to entered city and distances
    between cities. Error message is printed if <city> is not in
    <distance_data>.

    :param distance_data: dict{str:{str:int}}, includes all connexions
    """
    city = input("Enter departure city: ")
    # Again program checks if city exists in <distance_data>.
    if city in get_all_cities(distance_data):

        if city in distance_data:
            destinations_in_list = fetch_neighbours(distance_data, city)
            for destination in destinations_in_list:
                kilometers = \
                    distance_to_neighbour(distance_data, city, destination)
                print(f"{city:<14}{destination:<14}{kilometers:>5}")

        else:
            return

    else:
        print(f"Error: '{city}' is unknown.")


def check_distance():
    """
    Function asks user to input distance between departure and destination
    cities. Function changes the datatype to integer and returns it. If it is
    not possible to change datatype function prints error message and returns
    None.

    :return: int | None, returns distance as integer or None.
    """
    distance = input("Distance: ")

    try:
        distance = int(distance)

    except ValueError:
        print(f"Error: '{distance}' is not an integer.")
        distance = None

    return distance


def remove_connexion(distance_data):
    """
    Function asks user to input departure and destination cities. If they are
    not in <distance_data> error messages are printed. If connexion is found
    function removes it from <distance_data>. Otherwise, error message is
    printed.

    :param distance_data: dict{str:{str:int}}, includes all connexions
    """
    departure = input("Enter departure city: ")
    if departure in distance_data:
        destination = input("Enter destination city: ")

        if destination in distance_data[departure]:
            distance_data[departure].pop(destination)

        else:
            print(f"Error: missing road segment between "
                  f"'{departure}' and '{destination}'.")

    else:
        print(f"Error: '{departure}' is unknown.")


def add_connexion(distance_data):
    """
    Function ask user to input departure and destination cities and calls
    function <check_distance()> to add connexion and given distance to
    <distance_data>. If distance is integer connexion is added to
    <distance_data>. Otherwise, program running returns to main function.

    :param distance_data: dict{str:{str:int}}, includes all connexions
    """
    departure = input("Enter departure city: ")
    destination = input("Enter destination city: ")

    distance = check_distance()

    # if <distance> is integer function running continues.
    if distance is not None:

        # Cities are added in the same way as in function
        # <create_data_structure()>.
        if departure not in distance_data:

            destination_data = {}

            destination_data[destination] = distance
            distance_data[departure] = destination_data

        else:
            distance_data[departure][destination] = distance

    else:
        return


def print_distances(distance_data):
    """
    Function prints a table of all connexions in <distance_data>.

    :param distance_data: dict{str:{str:int}}, includes all connexions
    """

    for departures in sorted(distance_data):
        for destinations in sorted(distance_data[departures]):
            km = distance_data[departures][destinations]
            print(f"{departures:<14}{destinations:<14}{km:>5}")


def create_data_structure(file):
    """
    Function creates a dictionary that has departure city as key and another
    dictionary as payload. This another dictionary has destination city as key
    and distance between departure and destination cities as payload. This
    another dictionary contains all direct connexions to departure city.
    Function returns the created dictionary in alphabetical order.

    :param file: str, is a file that includes connexion data.
    :return: dict, returns created dictionary of connexions
    """

    departure_data = {}

    for line in sorted(file):
        line = line.rstrip()
        parts = line.split(";")

        # <parts[0]> is departure city that is key of dict <departure_data>.
        if parts[0] not in departure_data:

            destination_data = {}

            # <destination_data> is inner dict and <parts[1]> is the key
            # (destination city) and parts[2] is the payload (distance) of it.
            destination_data[parts[1]] = parts[2]
            # Inner dict is added to <departure_data[departure]> as payload.
            departure_data[parts[0]] = destination_data

        else:
            # New destination (parts[1]) is added to departure city (parts[0]).
            departure_data[parts[0]][parts[1]] = parts[2]

    return departure_data


def find_route(data, departure, destination):
    """
    This function tries to find a route between <departure>
    and <destination> cities. It assumes the existence of
    the two functions fetch_neighbours and distance_to_neighbour
    (see the assignment and the function templates below).
    They are used to get the relevant information from the data
    structure <data> for find_route to be able to do the search.

    The return value is a list of cities one must travel through
    to get from <departure> to <destination>. If for any
    reason the route does not exist, the return value is
    an empty list [].

    :param data: dict{str:{str:int}}, A data structure of an unspecified type
           (you decide) which contains the distance information between the
           cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: list[str], a list of cities the route travels through, or
           an empty list if the route can not be found. If the departure
           and the destination cities are the same, the function returns
           a two element list where the departure city is stored twice.
    """

    if departure not in data:
        return []

    elif departure == destination:
        return [departure, destination]

    greens = {departure}
    deltas = {departure: 0}
    came_from = {departure: None}

    while True:
        if destination in greens:
            break

        red_neighbours = []
        for city in greens:
            for neighbour in fetch_neighbours(data, city):
                if neighbour not in greens:
                    delta = deltas[city] + distance_to_neighbour(data, city, neighbour)
                    red_neighbours.append((city, neighbour, delta))

        if not red_neighbours:
            return []

        current_city, next_city, delta = min(red_neighbours, key=lambda x: x[2])

        greens.add(next_city)
        deltas[next_city] = delta
        came_from[next_city] = current_city

    route = []
    while True:
        route.append(destination)
        if destination == departure:
            break
        destination = came_from.get(destination)

    return list(reversed(route))


def read_distance_file(file_name):
    """
    Reads the distance information from <file_name> and stores it
    in a suitable data structure (you decide what kind of data
    structure to use). This data structure is also the return value,
    unless an error happens during the file reading operation.

    :param file_name: str, The name of the file to be read.
    :return: dict | None: A data structure containing the information
             read from the <file_name> or None if any kind of error happens.
             The data structure to be chosen is completely up to you as long
             as all the required operations can be implemented using it.
    """

    try:
        file = open(file_name, mode="r", encoding="utf-8")

        data_structure = create_data_structure(file)

    except IOError:
        return None

    return data_structure


def fetch_neighbours(data, city):
    """
    Returns a list of all the cities that are directly
    connected to parameter <city>. In other words, a list
    of cities where there exist an arrow from <city> to
    each element of the returned list. Return value is
    an empty list [], if <city> is unknown or if there are no
    arrows leaving from <city>.

    :param data: dict{str:{str:int}}, A data structure containing the distance
           information between the known cities.
    :param city: str, the name of the city whose neighbours we
           are interested in.
    :return: list[str], the neighbouring city names in a list.
             Returns [], if <city> is unknown (i.e. not stored as
             a departure city in <data>) or if there are no
             arrows leaving from the <city>.
    """

    citykeys = []

    if city in data:
        for destinations in data[city]:
            citykeys.append(destinations)

        return citykeys

    else:
        return citykeys


def distance_to_neighbour(data, departure, destination):
    """
    Returns the distance between two neighbouring cities.
    Returns None if there is no direct connection from
    <departure> city to <destination> city. In other words
    if there is no arrow leading from <departure> city to
    <destination> city.

    :param data: dict{str:{str:int}}, A data structure containing the distance
           information between the known cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: int | None, The distance between <departure> and
           <destination>. None if there is no direct connection
           between the two cities.
    """

    if destination not in data[departure]:
        return None

    else:
        return int(data[departure][destination])


def main():
    input_file = input("Enter input file name: ")

    distance_data = read_distance_file(input_file)

    if distance_data is None:
        print(f"Error: '{input_file}' can not be read.")
        return

    while True:
        action = input("Enter action> ")

        if action == "":
            print("Done and done!")
            return

        elif "display".startswith(action):

            print_distances(distance_data)

        elif "add".startswith(action):

            add_connexion(distance_data)

        elif "remove".startswith(action):

            remove_connexion(distance_data)

        elif "neighbours".startswith(action):

            find_neighbours(distance_data)

        elif "route".startswith(action):

            print_route(distance_data)

        else:
            print(f"Error: unknown action '{action}'.")


if __name__ == "__main__":
    main()
