import requests
import json
import time
# -------------------------
# Jinja2
# -------------------------
from jinja2 import Environment, FileSystemLoader
template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))

# -------------------------
# Headers
# -------------------------
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

# -------------------------
# Marvel API Keys
# Write this up after
# -------------------------

apiTS = "uatu"
marvelAPIkey = "225578a89fc76f3d20fbffda5d17a88d"
marvelMD5hash = "0b70457b1a50ceef71816e06a81966a8"

# # -------------------------
# # All Characters
# # -------------------------

# person_template = env.get_template('character.j2')
# people = requests.request("GET", f"http://gateway.marvel.com/v1/public/characters?ts={ apiTS }&apikey={ marvelAPIkey }&hash={ marvelMD5hash }&limit=100", headers=headers)
# peopleJSON = people.json()
# peopleList = peopleJSON['data']['results']
# numberOfPages =  peopleJSON['data']['total'] / 100
# offset = 100
# while numberOfPages > 0:
#     people = requests.request("GET", f"http://gateway.marvel.com/v1/public/characters?ts={ apiTS }&apikey={ marvelAPIkey }&hash={ marvelMD5hash }&limit=100&offset={ offset }", headers=headers)
#     peopleJSON = people.json()
#     peopleList.extend(peopleJSON['data']["results"])
#     offset = offset + 100
#     numberOfPages = numberOfPages - 1
#     time.sleep(0.5)

# # -------------------------
# # Single Character
# # -------------------------

# for person in peopleList:
#     singlePersonJSON = person

# # -------------------------
# # Person Template
# # -------------------------

#     parsed_all_output = person_template.render(singlePerson = singlePersonJSON)

# # -------------------------
# # Save Characters File
# # -------------------------

#     with open(f"Marvel/Characters/{ singlePersonJSON['name'].replace('/','') }.md", "w") as fh:
#         fh.write(parsed_all_output)                
#         fh.close()

# # -------------------------
# # All Events
# # -------------------------

# event_template = env.get_template('event.j2')
# marvelEvent = requests.request("GET", f"http://gateway.marvel.com/v1/public/events?ts={ apiTS }&apikey={ marvelAPIkey }&hash={ marvelMD5hash }&limit=100", headers=headers)
# marvelEventJSON = marvelEvent.json()
# marvelEventList = marvelEventJSON['data']['results']
# numberOfPages =  marvelEventJSON['data']['total'] / 100
# offset = 100
# while numberOfPages > 0:
#     marvelEvent = requests.request("GET", f"http://gateway.marvel.com/v1/public/events?ts={ apiTS }&apikey={ marvelAPIkey }&hash={ marvelMD5hash }&limit=100&offset={ offset }", headers=headers)
#     marvelEventJSON = marvelEvent.json()
#     marvelEventList.extend(marvelEventJSON['data']["results"])
#     offset = offset + 100
#     numberOfPages = numberOfPages - 1
#     time.sleep(0.5)

# # -------------------------
# # Single Event
# # -------------------------

# for event in marvelEventList:
#     singleEventJSON = event

# # -------------------------
# # Person Template
# # -------------------------

#     parsed_all_output = event_template.render(singleEvent = singleEventJSON)

# # -------------------------
# # Save Event File
# # -------------------------

#     with open(f"Marvel/Events/{ singleEventJSON['title'].replace('/','') }.md", "w") as fh:
#         fh.write(parsed_all_output)                
#         fh.close()

# # -------------------------
# # All Creators
# # -------------------------

# creator_template = env.get_template('creator.j2')
# creator = requests.request("GET", f"http://gateway.marvel.com/v1/public/creators?ts={ apiTS }&apikey={ marvelAPIkey }&hash={ marvelMD5hash }&limit=100", headers=headers)
# creatorJSON = creator.json()
# creatorList = creatorJSON['data']['results']
# numberOfPages =  creatorJSON['data']['total'] / 100
# offset = 100
# while numberOfPages > 0:
#     creator = requests.request("GET", f"http://gateway.marvel.com/v1/public/creators?ts={ apiTS }&apikey={ marvelAPIkey }&hash={ marvelMD5hash }&limit=100&offset={ offset }", headers=headers)
#     creatorJSON = creator.json()
#     creatorList.extend(creatorJSON['data']["results"])
#     offset = offset + 100
#     numberOfPages = numberOfPages - 1
#     time.sleep(10)
#     print(f"Number pages left { numberOfPages }")

# # -------------------------
# # Single Creator with First and Last Name
# # -------------------------

# print("Finished Building Creator List")

# for creator in creatorList:
#     if creator['firstName']:
#         if creator['lastName']:
#             singleCreatorJSON = creator

# # -------------------------
# # Person Template
# # -------------------------

#             parsed_all_output = creator_template.render(singleCreator = singleCreatorJSON)

# # -------------------------
# # Save Event File
# # -------------------------

#             with open(f"Marvel/Creators/{ singleCreatorJSON['firstName'] }_{ singleCreatorJSON['lastName'] }.md", "w") as fh:
#                 fh.write(parsed_all_output)                
#                 fh.close()

# -------------------------
# All Series
# -------------------------

series_template = env.get_template('series.j2')
start_year=2022
series = requests.request("GET", f"http://gateway.marvel.com/v1/public/series?ts={ apiTS }&apikey={ marvelAPIkey }&hash={ marvelMD5hash }&limit=100&startYear={ start_year }", headers=headers)
seriesJSON = series.json()
seriesList = seriesJSON['data']['results']
numberOfPages =  seriesJSON['data']['total'] / 100
offset = 100
while numberOfPages > 0:
    series = requests.request("GET", f"http://gateway.marvel.com/v1/public/series?ts={ apiTS }&apikey={ marvelAPIkey }&hash={ marvelMD5hash }&limit=100&startYear={ start_year }&offset={ offset }", headers=headers)
    seriesJSON = series.json()
    seriesList.extend(seriesJSON['data']["results"])
    offset = offset + 100
    numberOfPages = numberOfPages - 1
    time.sleep(10)
    print(f"Number pages left { numberOfPages }")

# -------------------------
# Single Creator with First and Last Name
# -------------------------

for series in seriesList:
    singleSeriesJSON = series

# -------------------------
# Person Template
# -------------------------

    parsed_all_output = series_template.render(singleSeries = singleSeriesJSON)

# -------------------------
# Save Event File
# -------------------------

    with open(f"Marvel/Series/{ start_year }/{ singleSeriesJSON['title'].replace('/',' ') }.md", "w") as fh:
        fh.write(parsed_all_output)                
        fh.close()  