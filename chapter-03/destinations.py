def checkDestination(dest, list):
    for i in range(len(list)):
        if list[i][0] == dest:
            return True
    return False


def destinations(list):
    end = None
    for i in range(len(list)):
        if not checkDestination(list[i][1], list):
            end = list[i][1]
            break
    return end


def destCity2(paths):
    has_outgoing = set()
    for i in range(len(paths)):
        has_outgoing.add(paths[i][0])

    for i in range(len(paths)):
        candidate = paths[i][1]
        if candidate not in has_outgoing:
            return candidate
    return ""


print(destCity2([["New York", "Lima"], ["London", "New York"], ["Lima", "Sao Paolo"]])
      )


print(destinations([["New York", "Lima"], [
      "London", "New York"], ["Lima", "Sao Paolo"]]))
