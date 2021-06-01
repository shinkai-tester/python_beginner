#sorted_top_listik1 = sorted(top_listik.items(), key = lambda kv:(-kv[1], kv[0]))
#sorted_top_listik = sorted(top_listik, key = lambda x: (-top_listik[x], x))


#list = [{'id':'1234','name':'Jason'},
#        {'id':'2345','name':'Tom'},
#        {'id':'3456','name':'Art'}]
#tom_index = next((index for (index, d) in enumerate(lst) if d["name"] == "Tom"), None)

#address = "123 north anywhere street"

#for word, initial in {"NORTH":"N", "SOUTH":"S" }.items():
#    address = address.replace(word.lower(), initial)
#print(address)

number_towns = int(input())
town_comp = {}
dist_towns = {}

for i in range(number_towns):
    town, *companies = input().split()
    town_comp[town] = companies
print(list(town_comp)[0])

