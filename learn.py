#!/Users/administrator/anaconda/bin/python 

weight = 0.5
goal   = 0.8
input  = 0.5
alpha  = 3.889

for iteration in range(20):
   prediction = input * weight
   error = (goal - prediction) ** 2
   derivative = input * (prediction - goal)
   weight = weight - (alpha * derivative)

   print("Predic-Error:" + str(error) + " Prediction:" + str(prediction))


