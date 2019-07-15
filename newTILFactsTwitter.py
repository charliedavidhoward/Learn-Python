#Background

#If you finished the previous project which compared the karma of two new comments, hopefully you learned a thing or two about receiving data from Reddit's API. Now you're going to take this a step further, and even have the opportunity to make a basic twitter bot.

#Goal

#Create a program that receives data from the /r/todayilearned subreddit, and looks for new facts that have been posted. Each time the program comes across a new fact, the fact should be printed into the command line. However, phrases like "TIL ", "TIL that", etc should be removed so the only thing that is printed is the fact.

#>>New TIL API data here<<

#There are a couple things to note about this since you'll more than likely be using a loop to check for new posts. According to Reddit's API Access Rules Page
#, the API pages are only updated once every thirty seconds, so you'll have to have your code pause for at least thirty seconds before it tries to find more posts. Secondly, if for some reason you decide to try to get data sooner than every thirty seconds, make sure to not send more than thirty requests per minute. That is the maximum you are allowed to do.

#Subgoal Ideas

#There is actually a lot you can do once your program starts receiving facts. Instead of simply printing the facts, here are some ideas for what you can do with them. If you currently do not feel like you can accomplish these ideas, feel free to come back later when you have more experience.

#    Print the link to the source of the fact too.

#    Try to further clean up the fact by adding punctuation to the end if it is missing, capitalize the first word, etc.

#    Write the facts to a separate text file so you end up with a giant compilation of random facts.

#    Create a bot that posts the facts to twitter. This may sound hard, but it's actually pretty simple by using the "Python Twitter Tools
#    " module and following the guide posted here
#    . Remember, the maximum amount of characters you can use in a tweet is only 140, so you'll have to filter out facts that are longer than that.

import requests
import re
import json
from twython import Twython
import time

# obtain the data from the TIL subreddit
url = "https://www.reddit.com/r/todayilearned/new/.json"
r = requests.get(url, headers={"User-agent": "python_tutorial"})
r_data = r.json()

# place the twitter API credentials into a dictionary
# (use your credentials here)
credentials = {}
credentials['CONSUMER_KEY'] = "YOUR_KEY"
credentials['CONSUMER_SECRET'] = "YOUR_SECRET_KEY"
credentials['ACCESS_TOKEN'] = "YOUR_ACCESS_TOKEN"
credentials['ACCESS_SECRET'] = "YOUR_ACCESS_SECRET"

with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

twitter = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'],
                  creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])

# compile a regex to strip the string of 'TIL' or 'TIL [T/t]hat' and other non-word characters
regex = re.compile("^TIL( that | That )*[^\w\d]*")

# loop through the TIL file, pulling out the titles
for i in r_data['data']['children']:
    if regex.match(i['data']['title']):
        regex_object = regex.match(i['data']['title'])
        post = i['data']['title'].replace(regex_object.group(), "").lstrip().capitalize()
        # limit the post to 140 characters
        if len(post) > 140:
            post = post[:137] + '...'
        twitter.update_status(status=post)
        time.sleep(30)

