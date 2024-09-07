def merge(f1, f2, f3):
    with open(f1, 'r') as f1:
            l = f1.readlines()
    # print(l)

    with open(f2, 'r') as f2:
        l2 = f2.readlines()
    # print(l2)
    l3 = l + l2

    with open(f3, 'w') as f3:
        f3.write('\n'.join(set(l3)))


# i1 = input("write the name of first file to be merged:")
# i2 = input("write the name of second file to be merged:")
# i3 = input("write the name of  file in which u want to store merged file:")
merge('new.txt', 'repo__rt.txt', 'a_.txt' )