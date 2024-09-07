# # l is th elist of elements
l = input('Enter the list of elements separated by comma: ').split(',')
# # d is dictionary in which key is the element from list and value is number of occurrence of that element
d = {}
d = {i : d[i]+1 if i in d.keys() else 1 for i in l }


##dictionary comprehension method

# d = {i : l.count(i) for i in l}


##first method


    # for i in l:
    #     if i in d.keys():
    #         d[i] += 1
    #     else:
    #         d[i] = 1

print(d)






# 2nd method


# d = dict.fromkeys(l,0)
# for keys in d:
#     d[keys] = l.count(keys)
# print(d)







