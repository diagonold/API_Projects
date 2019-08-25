# In this  script, we will get familiar on how to use datamuse API
# https://www.datamuse.com/api/
# It is a word finding query engine
# What the hell is that?
#   Basivally something that helps you find words when you give 
#   a set of constraint
# Its uses?
#   The great thins is it that there is a wide variety of constraint
#   from meaning, spelling, sound and vocabulary
#   Applications that requires autocomplete on text inputs, search of relevancy ranking
#   assistive writing apps, word games and more

import requests

# Remember that API are created by other programmers, 
#   thus they create their own way of defining things
# In the case of datamuse, they declare the endpoint 
#   by placing a "?" a question mark
# eg. https://api.datamuse.com/words?rel_rhy=jingle

# I am not sure why they created the paramter with a dictionary
# This is the more pythonic way of doing this.
# We can also the use the "words?" to mark an endpoint 
#   but this way is much better
parameter = {"rel_rhy":"jingle"}
request  = requests.get('https://api.datamuse.com/words', parameter)

# Now let us print thei first 3 words that rhymes with jingle
# Here we request the json file
#  but can actually be treated like a dictionary
rhyme_json = request.json()
for i in rhyme_json[0:3]:
    print(i["word"])


# Let us try another one instead of using rhymes
#   we use the spelled like parameter
# When using the sp, which means spelled like constraint, 
#   there is a need for wildcards
# We have yet to master regular expression, we know some from linux wildcards
# * any letter for any amount of character
# ? any letter for 1 character
# [<some characters>] means this character is anyone of the letters inside the []
parameter_spelling = { "sp" :"h??e"}
request_1 = requests.get("https://api.datamuse.com/words", parameter_spelling)
request_1_spelling = request_1.json()
for word in request_1_spelling[1:10]:
    print("{} is spelled like hole".format(word["word"]))


# Let us use datamuse one more time
# we can use the adjectives, we give a noun and search for adjectives
# that describes that noun
# they are given a score too , the highest score of relevance is give at the top
parameter_adj = {"rel_jjb": "love"}
request_2 = requests.get("https://api.datamuse.com/words", parameter_adj)
# Printing the status code is a great way to check if your request is okay
# Remember 200 menas okay, 404 means no connection
request_2_adj = request_2.json()
print(request_2.status_code)
for word in request_2_adj[1:20]:
    print("love is {}".format(word["word"]))