weight = 1
goal_pred = 5
inp = 4
alpha = 0.01

for _ in range(50000):
    pred = inp * weight
    error = (pred - goal_pred) ** 2
    direction_and_amount = (pred - goal_pred) * inp
    weight -= direction_and_amount * alpha

    print("Error: ", error, "Prediction: ", pred, "Weight: ", weight, "\n ----")
