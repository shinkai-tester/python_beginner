import random

number_towns = int(input())
town_comp = {}
dist_towns = {}
towns = []
lst_dict = []


def get_key(val, dic):
    for key, value in dic.items():
        if val in value:
            return key
    return "key doesn't exist"


for i in range(number_towns):
    town, *companies = input().split()
    town_comp[town] = companies

for k in range(number_towns):
    for j in range(number_towns):
        dist = int(input())
        towns = list(town_comp.keys())
        dist_towns[dist] = towns[k], towns[j]
        dict_towns_copy = dist_towns.copy()
        lst_dict.append(dict_towns_copy)
        dist_towns.clear()

number_comp = int(input())
curr_lst_dict = []
keys = []
wk_values = []

for a in range(number_comp):
    company_curr = input()
    town_comp_curr = get_key(company_curr, town_comp)
    for d in lst_dict:
        for k, v in d.items():
            if town_comp_curr in v:
                curr_lst_dict.append(d)
    for e in curr_lst_dict:
        for n in e.keys():
            keys.append(n)
    wrong_key = max(keys)
    wk_values = set([item for t in list(filter(None, [d.get(wrong_key, None) for d in curr_lst_dict])) for item in t])
    wk_values.discard(town_comp_curr)
    print(random.choice(tuple(wk_values)))
    curr_lst_dict.clear()
    keys.clear()
    wk_values.clear()
