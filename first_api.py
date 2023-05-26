import requests


def make_get_request(url, status_code=200):
    response = requests.get(url)
    assert response.status_code == status_code
    return response.json()


def make_post_request(url, data, status_code=201):
    response = requests.post(url, data=data)
    assert response.status_code == status_code
    return response.json()


reqres_url = "https://reqres.in"
get_api = "/api/users?page=2"
post_api = "/api/users"
my_data = {
    "name": "Areg",
    "job": "Student"
}

post = make_post_request(url=reqres_url + post_api, data=my_data)
get = make_get_request(url=reqres_url + get_api)

print(post)
# print(post['name'], post['job'])
print("\n")
print(get["data"])
# print(get["data"][0]["email"])
