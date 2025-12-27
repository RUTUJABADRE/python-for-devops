import requests
import json

api_url = "https://jsonplaceholder.typicode.com/"


def get_data(placeholder):
    final_url = f"{api_url}{placeholder}"
    print("Final url is : ", final_url)
    if placeholder == "posts":
        response = requests.get(final_url)
        data = response.json()
        print("data for posts placeholder : ", data[0])
        first_row = data[0]
    # Save to JSON file
    with open("data.json", "w") as file:
        json.dump(first_row, file, indent=4)

    print("\n✅ Data saved to data.json")

placeholder = input("Enter the place holder for you wish to use eg. (posts, comments, albums, photos, users etc)")
get_data(placeholder)