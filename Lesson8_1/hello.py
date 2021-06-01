def hello_to_all_friends(name, *friends, name_of_best_friend='Best friend', name_of_girlfriend='Girlfriend'):
    print('Hello, %s!' % name)
    print('Hello, Best Friend: %s!' % name_of_best_friend)
    print('Hello, Girlfriend: %s!' % name_of_girlfriend)
    for friend in friends:
        print('Hello, %s!' % friend)
    return len(friends)


f = hello_to_all_friends('Stepan')
print(f)