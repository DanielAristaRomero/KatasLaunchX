def main():
    try:
      configuration = open('config.txt')
    except FileNotFoundError as err:
      print("got a problem trying to read the file:", err)
    except OSError as err:
      if err.errno == 2:
         print("Couldn't find the config.txt file!")
      elif err.errno == 13:
         print("Found config.txt but couldn't read it")

def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            argument / 10
        except TypeError:
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

water_left("3", "200", None)
