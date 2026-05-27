import random

def roulette_wheel_selection(populasi, fitness_populasi):
    total_fitness = sum(fitness_populasi)
    if total_fitness == 0:
        idx = random.randrange(len(populasi))
        return populasi[idx], idx

    probabilitas = [fitness / total_fitness for fitness in fitness_populasi]

    kumulatif_prob = []
    kumulatif = 0
    for p in probabilitas:
        kumulatif += p
        kumulatif_prob.append(kumulatif)

    r = random.random()
    for i, kum_prob in enumerate(kumulatif_prob):
        if r <= kum_prob:
            return populasi[i], i

    return populasi[-1], len(populasi)-1