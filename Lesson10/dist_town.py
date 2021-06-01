number_towns = int(input())
comp_town = {}
towns = []
dist_towns = {}
curr_for_dist = {}
pred_for_dist = {}

for i in range(number_towns):
    town, *companies = input().split()
    towns.append(town)
    for company in companies:
        comp_town[company] = town

for k in range(number_towns):
    for j in range(number_towns):
        curr_for_dist[towns[j]] = int(input())
        pred_for_dist.update(curr_for_dist)
        dist_towns[towns[k]] = pred_for_dist
        pred_for_dist = pred_for_dist.copy()
        curr_for_dist.clear()

number_comp = int(input())
dist_for_town = {}
max_dist = 1
for c in range(number_comp):
    comp_curr = input()
    town_comp_curr = comp_town.get(comp_curr, None)
    dist_for_town = dist_towns[town_comp_curr]
    max_dist = max(dist_for_town, key=dist_for_town.get)
    print(max_dist)
