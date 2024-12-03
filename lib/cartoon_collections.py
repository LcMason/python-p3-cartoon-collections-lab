planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
calls = ["puff", "go", "two"]
snacks = ["crackers", "gouda", "thyme"]

def roll_call_dwarves(names):
    pass
    for index, name in enumerate(names, start=1):
        print(f"{index}. {name}")


def summon_captain_planet(planeteer_calls):
    pass
    return [call.capitalize() + "!" for call in planeteer_calls]
    # result = summon_captain_planet(planeteer_calls)
    # print(result)



def long_planeteer_calls(calls):
    pass
    return any(len(call) > 4 for call in calls)
   

def find_the_cheese(strings):
    pass
    cheeses = ["cheddar", "gouda", "camembert"]
    for item in strings:
        if item in cheeses:
            return item
    return None

