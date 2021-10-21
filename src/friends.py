def get_name(dictionary_name):
    return dictionary_name["name"]

def get_favourite_tv_show(dictionary_name):
    return dictionary_name["favourites"]["tv_show"]

def likes_to_eat(dictionary_name, food_type):
    likes = False
    for snack in dictionary_name["favourites"]["snacks"]:
        if snack == food_type:
         likes = True
    return likes

def add_friend(dictionary_name, friend_name):
    dictionary_name["friends"].append(friend_name)



