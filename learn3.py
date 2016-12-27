#!/Users/administrator/anaconda/bin/python

weight1 = 0.5
weight2 = 0.5
weight3 = -0.7
goal = 1.45
input1 = 1.0
input2 = 0.4
input3 = -1.0
alpha = 0.1


for iteration in range(20):
    prediction = (input1 * weight1) + (input2 * weight2) + (input3 * weight3)
    error = (goal - prediction) ** 2
    derivative = (input1 * (prediction - goal)) + (input2 * (prediction - goal)) + (input3 * (prediction - goal))
    weight1 = weight1 - (alpha * derivative)
    weight2 = weight2 - (alpha * derivative)
    weight3 = weight3 - (alpha * derivative)
    
    print("Error:" + str(error) + " Prediction:" + str(prediction))
