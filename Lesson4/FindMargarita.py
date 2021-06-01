for i in range(25):
    for j in range(25):
        for k in range(25):
            for l in range(25):
                Behemoth = i * 9
                Korovyev = j * 6
                Hella = k * 3
                Azazello = l
                if Behemoth + Korovyev + Hella + Azazello == 121:
                    print('Бегемот: ', i)
                    print('Коровьев: ', j)
                    print('Гелла: ', k)
                    print('Азазелло: ', l)
                    print('-----')