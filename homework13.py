# დავალება 1


import requests


def get_user(user_id: int) -> dict | None:

    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    users = response.json()

    for user in users:

        if user["id"] == user_id:

            return {
                "name": user["name"],
                "email": user["email"],
                "city": user["address"]["city"],
                "company": user["company"]["name"]
            }

    return None


print(get_user(1))
print(get_user(15))