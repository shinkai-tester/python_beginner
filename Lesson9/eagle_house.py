cities = set(input().split())
ox_cities = set(input().split())
lion_cities = set(input().split())
eagle_ox_cities = set(input().split())
lion_eagle_cities = set(input().split())
eagle_ox_lion_cities = eagle_ox_cities.union(lion_eagle_cities)
diff_lion_ox = lion_cities.difference(eagle_ox_lion_cities).union(ox_cities.difference(eagle_ox_lion_cities))
eagle_cities = ' '.join(sorted([i for i in cities if i not in diff_lion_ox]))
if len(eagle_cities) == 0:
    print('Нет таких городов')
else:
    print(eagle_cities)
