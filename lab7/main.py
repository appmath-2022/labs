import markov_chains

matrix = markov_chains.read()
vector_numerical = markov_chains.numerical_solution(matrix)
vector_analytical = markov_chains.analytical_solution(matrix)

for i in range(len(vector_numerical)):
    print(vector_numerical[i].round(6), end=' ')

print('\n')
for i in range(len(vector_analytical)):
    print(vector_analytical[i].real.round(6), end=' ')

