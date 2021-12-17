import numpy as np
#Importing data from the csv file
taxis = np.genfromtxt('nyc_taxis.csv' , delimiter = ',' , skip_header = True)
#Getting the taxi speed by dividing the distance and time(trip length) columns
taxi_speed = taxis[: , 7] / (taxis[: ,8] / 3600)
#Finding the mean speed of taxis 
mean_speed = taxi_speed.mean( )
print(mean_speed)
print(' ')
#Getting the total rides in the month of February
feb_rides = taxis[taxis[: , 1] == 2, 1]
print(feb_rides.shape[0])
print(' ')
#Calculate the number of rides where the passengers have tipped more than $50
great_tips = taxis[taxis[: , -3] > 50 , -3]
print(great_tips.shape[0])
print(' ')
#Calculate the number of rides where the drop has been to the JFK airport 
#The JFK airport drops are denoted by 2 in the table's drop-off location column
JFK_dropoffs = taxis[taxis[: , 6] == 2, 6]
print(JFK_dropoffs.shape[0])
print(' ')