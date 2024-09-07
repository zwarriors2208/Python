d = {'harry potter' : {'author': 'aman', 'genre': 'fantasy', 'year': 345  }}
ip = input('enter namr')
def search(s):
    for books in d.keys():
        temp = d[books]
        if temp['author'] == s or temp['genre'] == s:
            print("the name of book is :", books , "\nthe details of book are :", temp)
            break
        else:
            continue
search(ip)