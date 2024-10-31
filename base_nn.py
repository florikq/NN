inp = 5
weight = 1
alpha = 0.1
real_out = 4


def nn(inputs, weights):
    return inputs * weights


for _ in range(3):
    pred = nn(inp, weight)
    if pred > real_out:
        weight -= alpha
    elif pred < real_out:
        weight += alpha

    print("Weight:", weight, " Prediction:", pred, "\n----")
