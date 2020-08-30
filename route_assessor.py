paths = [
        [2, 4], 
        [3, 4, 5], 
        [4, 3, 4],
        [],
        ]

route = [1, 4]

been_to = []

def find_route_recursive(current_position, target_position):
    try:
        paths[target_position - 1] == True
    except IndexError:
        return "Target City Does Not Exist"
    if current_position == target_position:
        return True
    for x in been_to:
        if x == current_position:
            return False
    been_to.append(current_position)
    index = current_position - 1
    next_destinations = paths[index]
    for x in next_destinations:
        if find_route_recursive(x, target_position) == True:
            return True
    return False

print(find_route_recursive(route[0], route[1]))
