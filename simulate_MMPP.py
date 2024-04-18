import numpy as np
import matplotlib.pyplot as plt

def simulate_markov_process(n_steps, transition_matrix, initial_state):
    current_state = initial_state
    states = [current_state]
    for _ in range(n_steps - 1):
        next_state = np.random.choice(len(transition_matrix[current_state]), p=transition_matrix[current_state])
        states.append(next_state)
        current_state = next_state
    return states

def simulate_poisson_process(rate_values, time_step):
    counts = []
    for rate in rate_values:
        count = np.random.poisson(rate * time_step)
        counts.append(count)
    return counts

# Example transition matrix for a simple 2-state Markov chain
transition_matrix = np.array([[0.9, 0.1], 
                               [0.2, 0.8]])

# Number of time steps to simulate
n_steps = 100

# Initial state
initial_state = 0

# Simulate the Markov process for the rate
markov_states = simulate_markov_process(n_steps, transition_matrix, initial_state)

# Simulate the Poisson process for a given period (e.g., 1 time unit per step)
time_step = 1
poisson_counts = simulate_poisson_process(markov_states, time_step)

# Plot the Poisson counts
plt.plot(range(n_steps), poisson_counts, marker='o', linestyle='-')
plt.xlabel('Time Step')
plt.ylabel('Poisson Counts')
plt.title('Simulated Poisson Process')
plt.grid(True)
plt.show()
