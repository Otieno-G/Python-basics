#TABLE TRIP

pickup_location = "Karen"
destination = "Kenyatta"
fare_cost = float(100)
trip_status = "Completed"
vehicle_id = "KDU 324K"
deliveries = 8
delivery_cost = float(200)
total_passengers = 14
fuel_cost = 100
driver_pay = 1000
conductor_pay = 500
car_service_cost = 200
vehicle_model = "Isuzu"

total_fare = fare_cost * total_passengers
total_delivery_cost = deliveries * delivery_cost
earnings = (fare_cost * total_passengers) + (deliveries * delivery_cost)
expenses = fuel_cost + driver_pay + conductor_pay + delivery_cost
profit = earnings - expenses
delivery_earning = delivery_cost * deliveries


