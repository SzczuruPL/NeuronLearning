import random

# Funkcja aktywacji (można dostosować do innych funkcji)
def activation_function(summation):
    return 1 if summation >= 0 else 0

# Inicjalizacja losowych wag oraz wartości uczenia
w1 = random.uniform(-1, 1)
w2 = random.uniform(-1, 1)
w3 = random.uniform(-1, 1)
learning_rate = random.uniform(0, 0.7)

print(f"Wagi: {w1}, {w2}, {w3}. Wartość uczenia: {learning_rate}")

# Dane wejściowe (można dostosować)
data = [
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

# Inicjalizacja listy deltas
deltas = [1] * 4

# Uczenie neuronu
print("\nUczenie neuronu:\n")
while any(delta != 0 for delta in deltas):
    deltas = []
    for i in range(4):
        x1, x2, x3 = data[i]
        desired_output = [0, 1, 1, 1]
        summation = w1 * x1 + w2 * x2 + w3 * x3
        y = activation_function(summation)
        delta = y - desired_output[i]
        w1 -= learning_rate * delta * x1
        w2 -= learning_rate * delta * x2
        w3 -= learning_rate * delta * x3
        print(f"Wejścia: {x1}, {x2}, {x3} => Wynik: {delta}")
        deltas.append(delta)
