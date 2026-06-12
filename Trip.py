#TABLE TRIP

pickup_location = "Karen"
destination = "Kenyatta"
fare_cost = float(100)
trip_status = "Completed"
vehicle_id = "KDU 324K"
deliveries = 8
delivery_cost = float(200)
total_passengers = 14
fuel_cost =float(1000)
driver_pay =float(600)
conductor_pay = float(500)
car_service_cost = float(200)
vehicle_model = "Isuzu"

total_fare = fare_cost * total_passengers
total_delivery_cost = deliveries * delivery_cost
earnings = (fare_cost * total_passengers) + (deliveries * delivery_cost)
expenses = fuel_cost + driver_pay + conductor_pay + delivery_cost
profit = earnings - expenses
delivery_earning = delivery_cost * deliveries

print( "TRIP DETAILS ")
print("Vehicle Model   :",vehicle_model)
print("Trip Id         :",trip_id)
print("Passenger Id    :",passenger_id)
print("Pickup Location :",pickup_location)
print("Destination     :",destination)
print("Fare cost       :",fare_cost)
print("Trip  Status    :",trip_status)
print("Earning         :",earnings)
print("Expenses        :",expenses)
print("Profit          :",profit)


#Amounts made per day
trips = 6
delivery_trips = 4
fueling_times = 3
total_earnings = trips * total_fare + delivery_trips * total_delivery_cost
total_expenses = fueling_times * fuel_cost + trips * driver_pay + trips * conductor_pay + car_service_cost
total_profit = total_earnings - expenses
total_driver_pay = trips * driver_pay
total_conductor_pay = trips * conductor_pay
total_fueling_cost = fueling_times * fuel_cost
total_service_cost = 1 * car_ service_cost
total_fare = (fare_cost * total_passengers) * trips
total_delivery_cost = (deliveries * delivery_cost) * delivery_trips


print("   MONDAY RECEIPT ")
print("Vehicle   Id               :",vehicle_id)
print("Total     Earnings         :ksh",total_earnings)
print("Total     Expenses         :ksh",total_expenses)
print("Total     Profit           :ksh",:total_profit)
print("Total     Driver  Pay      :ksh",:total_driver_pay)
print("Total     Conductor  Pay   :ksh",:total_conductor_pay)
print("Total     Fueling  Cost    :ksh",:total_fueling_cost)
print("Total     Service  Cost    :ksh",:total_service_cost)
ptint("Total     Fare             :ksh",:total_fare)
print("Total     Delivery  Cost   :ksh",:total_delivery_cost)
print("Super     Metro  Sacco Ltd")

#This python script shows me everything concerning the trip ,the cost incurred and the amount made in a day by the vehicle 

