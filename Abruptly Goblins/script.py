gamers = []

def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamers)
    else:
        print("Gamer missing critical information")

kimberly = {'name': "Kimberly Warner", 'availability': ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)
Tom = {'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}
add_gamer(Tom, gamers)
Joyce = {'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}
add_gamer(Joyce, gamers)
Michelle ={'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}
add_gamer(Michelle, gamers)
Stephen ={'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}
add_gamer(Stephen, gamers)
Joanne ={'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}
add_gamer(Joanne, gamers)
Latasha ={'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}
add_gamer(Latasha, gamers)
Crystal ={'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}
add_gamer(Crystal, gamers)
James ={'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}
add_gamer(James, gamers)
Michel ={'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}
add_gamer(Michel, gamers)
print(gamers)



add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

print(gamers)

def build_daily_frequency_table():
    return {"Monday": 0,
            "Tuesday" : 0,
            "Wednesday" : 0,
            "Thursday" : 0,
            "Friday" : 0,
            "Saturday" : 0,
            "Sunday" : 0,
            }

count_availability = build_daily_frequency_table

def calculate_availability(gamers_list,available_frequency):
    available_frequency =[]
    for gamer in gamers_list:
        for day in gamer['availability']:
            available_frequency[day] += 1

calculate_availability(gamers, count_availability)
print(count_availability)
