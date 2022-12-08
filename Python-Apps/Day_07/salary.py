user_response=input("Type an Integer:")
x = int(user_response)
total_amount = 0
if x < 0 or x > 168:
    print("INVALID")
elif x <= 40:
    total_amount = x * 8
    print("YOU MADE", total_amount, "DOLLARS THIS WEEK")
elif x <= 50:
    total_amount = (40 * 8) + ((x - 40) * 9)
    print("YOU MADE", total_amount, "DOLLARS THIS WEEK")
else:
    total_amount = (40 * 8) + (10*9)+((x-50) * 10)
    print("YOU MADE", total_amount, "DOLLARS THIS WEEK")