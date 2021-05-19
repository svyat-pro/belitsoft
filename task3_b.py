
lst = ['a', 'b', 'c', 'c', 'a']

def find_first_duplicate(par):
    num_set = set()
    no_duplicate = -1

    for i in range(len(par)):

        if par[i] in num_set:
            return par[i]
        else:
            num_set.add(par[i])

    return no_duplicate

print(find_first_duplicate(lst))

