weight = [0.1, 0.49, 0.9]
inp = 1.95
goal_pred = [8.4, 0.24, 1.1]
alpha = 0.1


def nn(inp, weight):
    output = [0,0,0]

    for i in range(len(weight)):
        output[i] += inp * weight[i]

    return output

for i in range(3):
    pred = nn(inp, weight)
    delta = [0,0,0]
    error = [0,0,0]
    weight_delta = [0, 0, 0]

    for j in range(len(goal_pred)):
        delta[j] = pred[j] - goal_pred[j]
        error[j] = delta[j] ** 2
        weight_delta[j] = inp * delta[j]


    print("Iteration: ", i)
    print("Prediction: ", pred)
    print("Error: ", error)
    print("Weight: ", weight)
    print("Weight_delta: ", weight_delta, "\n")

    for k in range(len(weight)):
        weight[k] -= weight_delta[k] * alpha