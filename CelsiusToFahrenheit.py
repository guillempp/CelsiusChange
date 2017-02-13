degrees = input("Hou much Celsius degrees did you like to convert? ")

def to_fahrenheit(degrees):
  return degrees * 1.8 + 32

fah = to_fahrenheit(degrees)
print "This will be ",fah,"Fahrenheit degrees"
