# Assign value 100 to variable cars 
cars = 100
# Assign value 4.0 (floating point) to variable space_in_a_car
space_in_a_car = 4.0
# Assign valuse 30 to variable drivers
drivers = 30
# Assign 90 to variable passengers
passengers = 90
# Assign value from results of (cars - drivers) to variable cars_not_driven
cars_not_driven = cars - drivers
# Assign value of drivers to variable cars_driven
cars_driven = drivers
# Assign value from result of (cars_driven * space_in_a_car) to variable
# carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# Assign value from result of (passengers / cars_driven) to variable
# average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

# These 6 below print statements perform arithmetic with the values stored in
# the above variables and print the results to the screen
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
