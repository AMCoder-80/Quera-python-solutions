def calculator(n, m, li):
    new_list = list()
    for i in range(n//m + n%m):
        new_list.append(sum(li[i*m:i*m+m]))
    total = new_list[0]
    for i in range(1, len(new_list)):
        if i % 2:
            total -= new_list[i]
        else:
            total += new_list[i]
    return total
