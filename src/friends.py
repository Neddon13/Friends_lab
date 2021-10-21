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

def remove_friend(dictionary_name, friend_name):
    dictionary_name["friends"].remove(friend_name)

def total_money(list_of_people):
    total_monies = 0
    for person in list_of_people:
        total_monies = total_monies + person["monies"]
    return total_monies

def l_money(ler_dictionary, lee_dictionary, loan_amount):
    # lender = lender - loan
    ler_dictionary["monies"] = ler_dictionary["monies"] - loan_amount
    # lendee = lendee + loan
    lee_dictionary["monies"] = lee_dictionary["monies"] + loan_amount

def all_favourite_foods(list_of_people):
    list_of_favs = []
    for person in list_of_people:
        for snack in person["favourites"]["snacks"]:
            list_of_favs.append(snack)
    return list_of_favs

def find_no_friendends(people):
    no_friends = []
    for person in people:
        if len(person['friends']) == 0:
            no_friends.append(person)
    return no_friends
