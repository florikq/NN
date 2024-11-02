weight = [0.1, 0.49, 0.9]
inp = [8.4, 0.24, 1.1]
goal_pred = 1.5
alpha = 0.01


def nn(inp, weight):
    output = 0

    for i in range(len(weight)):
        output += weight[i] * inp[i]

    return output


for i in range(30):
    pred = nn(inp, weight)
    delta = pred - goal_pred
    error = delta ** 2
    weight_delta = [0, 0, 0]

    for j in range(len(weight_delta)):
        weight_delta[j] = inp[j] * delta

    print("Iteration:  ", i)
    print("Prediction: ", pred)
    print("Error: ", error)
    print("Weight: ", weight)
    print("Weight_delta: ", weight_delta, "\n")
    print()

    for k in range(len(weight)):
        weight[k] -= weight_delta[k] * alpha