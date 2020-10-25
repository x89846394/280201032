car1_velocity = 80
car2_velocity = 70
distance_between_cars = 490

t = (distance_between_cars - 150) / (car1_velocity + car2_velocity)

print(f"The distance between cars will be 150km {int(t * 60)} minutes later.")
