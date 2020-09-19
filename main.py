print('Basic Physics Calculator')

# Read in the values from the user, the input function returns a string
distance_m_str = input('Enter the Distance (m): ')
time_s_str = input('Enter the time (s): ')

# Casting to floats
distance_m = float(distance_m_str)
time_s = float(time_s_str)

# Calculate the speed
speed_ms = distance_m / time_s

# Use formatted strings to print out the various values
print(f"You travelled {distance_m} metres in {time_s} seconds, your speed was {speed_ms} m/s")

# Just so we know that the program reached the end
print('Done')