import requests
def fn1(url,j_son):
    response=requests.post(url,json=j_son)
    return response.status_code

url = "https://jsonplaceholder.typicode.com/posts"
weather={'city':'New York','temp':28,'humidity':60,'condition':'Sunny'}