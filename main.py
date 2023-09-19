speed_limit = int(input("Enter speed limit: "))
driver_speed = int(input("Enter driver speed: "))
speed_difference = driver_speed - speed_limit

if speed_difference >= 41:
    print("$300 ticket")
elif speed_difference >= 21:
    print("$150 ticket")
elif speed_difference >= 6:
    print("$75 ticket")
elif speed_difference <= -10:
    print("$50 ticket")
else:
    print("No ticket")
