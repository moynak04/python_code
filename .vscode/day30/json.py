import json

website = "Google"
email = "moynak@gmail.com"
password = "Google@123"

new_data = {
    website: {
        "email": email,
        "password": password
    }
}

try:
    with open("data.json", "r") as data_file:
        data = json.load(data_file)

except FileNotFoundError:
    with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)

else:
    data.update(new_data)

    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)