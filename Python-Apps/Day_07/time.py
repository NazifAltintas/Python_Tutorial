user_response = input("Enter a positive integer (seconds):")
given_seconds = int(user_response)
# Calculate the days
days = given_seconds//(24*60*60)
seconds_1 = given_seconds % (24*60*60)    # remaining seconds after we get days
# Calculate the hours
hours = seconds_1//(60*60)          # get the hours out of seconds_1
seconds_2 = seconds_1 % (60*60)     # remaining seconds after we get hours
# Calculate the minutes
minutes = seconds_2 // 60           # get the minutes
# Finally calculate the remaining seconds after we get the minutes
seconds = seconds_2 % 60
print(days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")