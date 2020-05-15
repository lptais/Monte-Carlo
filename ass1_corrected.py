import numpy as np

#monte carlo variables
initial_capital = 100000
annual_inv = 10000
mean = .138
std_dev = .21

#vectors
return_year = [0]*30
return_1000=[0]*1000

for j in range (1000):

    rand_return_30 = 1+np.random.normal(mean,std_dev,30)
    return_year[0] = initial_capital*rand_return_30[0]+annual_inv
    return_year[1] = return_year[0]*rand_return_30[1]+annual_inv
    
    
    for i in range(1,29):
        if i<=30:
            ending_value = return_year[i]*rand_return_30[i]+annual_inv
            return_year[i+1] = ending_value
    
    return_1000[j]=return_year[29]
#average value for 1000 iteractions
average=sum(return_1000)/len(return_1000)

#prints
print("Possible value, year 1 is:",return_year[0]) #1 year
print("Possible value, year 2 is:",return_year[1]) # 2 years
print("Possible value, year 30 is:",return_year[29]) #30 years
print("Average value of 1000 iterations:", average) #1000 iterations