population = list(map(int, input().split(', ')))
minimum_wealth = int(input())

for index, wealth in enumerate(population):
    if wealth < minimum_wealth:
        max_population = population.index(max(population))
        needed_wealth = minimum_wealth - wealth
        population[max_population] -= needed_wealth
        population[index] += needed_wealth

has_needed_wealth = [0 for wealth in population if wealth >= minimum_wealth]

if len(has_needed_wealth) == len(population):
    print(population)
else:
    print("No equal distribution possible")