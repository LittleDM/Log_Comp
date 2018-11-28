# 3. Create scenarios that describe a solution(a) and how to test those solutions (b).

# a: Describe the solution

# If you see something in your path (Premise A = True)
# Then
# Identify object as a vehicle or human or animal or thing
# Calculate object’s distance = X1 
# and
# Calculate our car’s velocity = V 
# and
# Calculate distant required to stop our car = Y1

# If Y1 < X1 then stop on your lane (Premise B = False)
# If Y1 >= X1 then change lanes (Premise B = True) to avoid object

# If you change lanes (Premise B = True)
# And there is nothing in that lane (Premise C = False)
# Then
# avoid the object in the previous lane 
# and 
# return to your previous lane

# If there is something in that lane (Premise C = True)
# Then we have a dilemma.

# Software solution:
# Identify the object in the new lane as a vehicle or human or animal or thing
# If the object in the previous lane is a thing
# then
# Stop the car in the previous lane
# Else
# If the object in the new lane is a thing
# Then
# Stop the car in the new lane
# Else
# If both objects are not things
# Then
# Stop the car
# And
# Change direction to the nearest side of the road 
# Where
# There are no pedestrians and no parked vehicles
# else
# If there are pedestrians and parked vehicles 
# Then
# Change direction to parked vehicles
# else
# If there are pedestrians and no parked vehicles
# Then
# Stay in the lane
# Where
# Object ahead is a vehicle and you have the same direction
# Else
# If object ahead is a vehicle and not in the same direction
# Else
# If no object ahead is a vehicle
# Then
# Calculate object’s distance in new lane = X2 
# And
# Calculate our car’s velocity = V 
# and
# Calculate distant required to stop our car = Y2

# If Y2 < X2 then stop the car in the new lane
# else
# Calculate the size and location of each object
# Calculate the size of our car
# Calculate the size of the road
# Avoid both objects
# Else 
# Stay in lane 
# where 
# The object is animal and smallest of both
# Else
# If no animals in both lanes
# then

# If Y1 – X1 < = Y2 – X2 then stop on previous lane
# Else
# Stop in the new lane.

# Notes:
# The gist of the above software solution that I try to communicate is that if we finally get down to the unavoidable ethical dilemma which human to hit with our car, I instruct the car to hit the human where the impact will be as minor as possible, judging by the minimum difference between 'the required distance to stop the car in relation to our velocity' and 'the distance between the object and our car'.

# b: Test the solution

# Since we are after a solution based on deductive logic (hopefully!) then if we run the scenario and we get either Premise A or Premise B or Premise C as False we have a solution to our ethical dilemma. In any other case, it must be that all premises are True therefore we have an ethical dilemma which we solve with the use of our software solution, namely the worst case scenario is hitting the human where the impact will be as minor as possible.