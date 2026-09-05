def calculate_flight_time(weight_grams): 
    #AI suggested docstring
    """Calculate the flight time based on the weight of the drone in grams. Uses the formula: flight_time = 180 - (0.1 * weight_grams). If the calculated flight time is less than 0, it returns 0. """
    flight_time = 180 - (0.1 * weight_grams)

    if flight_time < 0:
        flight_time = 0
    return flight_time


#copilot suggested code
def flight_time_table(max_weight_grams, step_grams): 
    #AI suggested docstring
    """Generate a flight time table for weights from 0 to max_weight_grams in increments of step_grams. Uses the calculate_flight_time function to compute flight times for each weight. Prints the results in a formatted table."""
    print("Weight (grams) | Flight Time (seconds)")
    print("----------------------------------------")
    for weight in range(0, max_weight_grams + 1, step_grams):
        flight_time = calculate_flight_time(weight)
        #AI orignially limited weight to <15
        print(f"{weight} | {flight_time:.2f}")

#AI suggested code
weightG = float(input("Enter the weight of the payload in grams: "))
flight_timeG = calculate_flight_time(weightG)
print(f"The flight time for a payload of {weightG} grams is {flight_timeG:.2f} seconds.")

#AI suggested code
maxWeight = int(input("Enter the maximum weight for the flight time table in grams: "))
stepWeight = int(input("Enter the step weight for the flight time table in grams: "))
flight_time_table(maxWeight, stepWeight)