def print_seconds_per_day():
  hours = 24
  minutes = hours * 60
  seconds = minutes * 60
  print(seconds)

print_seconds_per_day()

def print_seconds_per_day(days):
  hours = days * 24
  minutes = hours * 60
  seconds = minutes * 60
  print(seconds)

print_seconds_per_day(7)

def convert_days_to_seconds(days):
  hours = days * 24
  minutes = hours * 60 
  seconds = minutes * 60
  return seconds

total_second = convert_days_to_seconds(12)
milliseconds = total_second * 1000
print(milliseconds)