import math

def get_MSRE(predicted, observed):

    sume = 0  
    n = len(predicted) 

    if n >= 1 and n <= 1000:
        for i in range (0,n):
            if predicted[i] >= (-10**9) and predicted[i]<=(10**9):
                difference = predicted[i] - observed[i]  
                squared_difference = difference**2  
                sume = sume + squared_difference
                MSE = sume/n  
                MSRE = math.sqrt(MSE)
        return MSRE

         




predicted = [4, 25, 0.75, 11]
observed = [3, 21, -1.25, 13]


print(get_MSRE(predicted, observed))



