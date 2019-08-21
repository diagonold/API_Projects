import requests
# We will get familiar with this module as we go through this course.
# For now we will be learning how to use API that are already available

# GET requests
# Get requests takes in a URL and will return a value after.
# This return value is stored in requests
# Without the right endpoint, we will receive only the html response
# request_1 is the counter-example

# What are endpoints?
# endpoints are the location of the resouces we need, by hitting the right end point
# we can retrieve the data we ned

# Here we give a url without any appropriate end point
request_1 = requests.get("http://api.open-notify.org/")
# request.text can help us access important data
print(request_1.text)

# status code can help tell us a bit about the response
# code 200: everything okay
# code 404: resource was not found
print(request_1.status_code)

# Here we give a proper endpoint
# In this endpoint, we look at the number of astronomers in the space
people = requests.get("http://api.open-notify.org/astros.json")
# Sadly, this data is returned in json format. 
print(people.text)
# Luckily, requests has a built in json decode method that will help us read
# the data more like a familiary dictoonary of key-value pairs
people_json = people.json()
print(people_json)

# Let's  try printint the number of people in space
print("Number of people in space: {}".format(people_json["number"]))
# Let's try printing the name of the people and the craft that they are at in space
for person in people_json["people"]:
    print("{} is in spacecraft called {}".format(person["name"], person["craft"]))



# Practicing on the other endpoints
location = requests.get("http://api.open-notify.org/iss-now.json")
# Let us first print out what we get with location.text
print(location.text)
# I do not fully understand the difference between a json file and a dictionary
location_dict = location.json()
print(location_dict)
# Though they look alike a json file cannot be accessed like a dictionary
# Thus we need to call this .json() method to turn json into a dictionary
# Else, we cannot use key-pair value
print("lngitude is {} and latitude is  {}".format(\
    location_dict["iss_position"]["longitude"], location_dict["iss_position"]["latitude"]))