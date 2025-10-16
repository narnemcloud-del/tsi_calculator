players = [
{"name":"LeBron James","ppg":27.0,"assists":7.4,"rebounds":7.5,"steals":1.5,"blocks":0.7,"ts%":0.590,"years":22},
{"name":"Stephen Curry","ppg":24.8,"assists":6.4,"rebounds":4.7,"steals":1.6,"blocks":0.2,"ts%":0.625,"years":16},
{"name":"Kevin Durant","ppg":27.3,"assists":4.3,"rebounds":7.0,"steals":1.1,"blocks":1.1,"ts%":0.620,"years":17},
{"name":"Giannis Antetokounmpo","ppg":23.4,"assists":4.9,"rebounds":9.8,"steals":1.2,"blocks":1.3,"ts%":0.611,"years":12},
{"name":"Nikola Jokic","ppg":20.8,"assists":6.6,"rebounds":10.7,"steals":1.2,"blocks":0.7,"ts%":0.638,"years":10},
{"name":"Luka Doncic","ppg":28.7,"assists":8.6,"rebounds":9.0,"steals":1.1,"blocks":0.4,"ts%":0.571,"years":7},
{"name":"Jayson Tatum","ppg":23.1,"assists":3.5,"rebounds":7.2,"steals":1.1,"blocks":0.7,"ts%":0.573,"years":8},
{"name":"Jimmy Butler","ppg":18.3,"assists":4.3,"rebounds":5.3,"steals":1.6,"blocks":0.4,"ts%":0.589,"years":13},
{"name":"Anthony Davis","ppg":24.0,"assists":2.5,"rebounds":10.4,"steals":1.3,"blocks":2.3,"ts%":0.588,"years":12},
{"name":"Kawhi Leonard","ppg":19.6,"assists":2.9,"rebounds":6.4,"steals":1.8,"blocks":0.6,"ts%":0.569,"years":10},
{"name":"Damian Lillard","ppg":25.1,"assists":6.7,"rebounds":4.2,"steals":1.0,"blocks":0.3,"ts%":0.558,"years":12},
{"name":"Joel Embiid","ppg":27.9,"assists":3.6,"rebounds":11.2,"steals":0.9,"blocks":1.7,"ts%":0.642,"years":9},
{"name":"Devin Booker","ppg":24.0,"assists":5.0,"rebounds":4.0,"steals":0.9,"blocks":0.3,"ts%":0.593,"years":9},
{"name":"Ja Morant","ppg":22.4,"assists":7.4,"rebounds":4.8,"steals":1.0,"blocks":0.3,"ts%":0.538,"years":5},
{"name":"Shai Gilgeous-Alexander","ppg":21.6,"assists":4.6,"rebounds":4.4,"steals":1.2,"blocks":0.7,"ts%":0.558,"years":6},
{"name":"Donovan Mitchell","ppg":24.8,"assists":4.6,"rebounds":4.3,"steals":1.3,"blocks":0.3,"ts%":0.557,"years":7},
{"name":"Zion Williamson","ppg":25.8,"assists":3.6,"rebounds":7.0,"steals":0.9,"blocks":0.6,"ts%":0.621,"years":4},
{"name":"Tyrese Haliburton","ppg":17.2,"assists":8.6,"rebounds":3.9,"steals":1.6,"blocks":0.5,"ts%":0.599,"years":4},
{"name":"Anthony Edwards","ppg":21.8,"assists":3.6,"rebounds":5.0,"steals":1.4,"blocks":0.5,"ts%":0.552,"years":4},
{"name":"LaMelo Ball","ppg":19.4,"assists":7.4,"rebounds":6.2,"steals":1.5,"blocks":0.3,"ts%":0.545,"years":4},
{"name":"Karl-Anthony Towns","ppg":22.9,"assists":3.2,"rebounds":10.8,"steals":0.8,"blocks":1.3,"ts%":0.613,"years":9},
{"name":"Paul George","ppg":20.4,"assists":3.7,"rebounds":6.4,"steals":1.7,"blocks":0.4,"ts%":0.558,"years":13},
{"name":"James Harden","ppg":24.1,"assists":7.0,"rebounds":5.6,"steals":1.5,"blocks":0.5,"ts%":0.566,"years":14},
{"name":"Kyrie Irving","ppg":23.5,"assists":5.7,"rebounds":3.9,"steals":1.3,"blocks":0.4,"ts%":0.570,"years":13},
{"name":"De'Aaron Fox","ppg":19.9,"assists":6.2,"rebounds":3.7,"steals":1.3,"blocks":0.4,"ts%":0.573,"years":7},
{"name":"Jaylen Brown","ppg":18.6,"assists":2.4,"rebounds":5.3,"steals":1.0,"blocks":0.4,"ts%":0.541,"years":8},
{"name":"Pascal Siakam","ppg":17.7,"assists":3.6,"rebounds":6.5,"steals":0.9,"blocks":0.7,"ts%":0.566,"years":7},
{"name":"Brandon Ingram","ppg":19.4,"assists":4.2,"rebounds":5.2,"steals":0.7,"blocks":0.6,"ts%":0.553,"years":7},
{"name":"Julius Randle","ppg":17.8,"assists":3.6,"rebounds":9.2,"steals":0.7,"blocks":0.4,"ts%":0.530,"years":9},
{"name":"Bam Adebayo","ppg":15.0,"assists":3.5,"rebounds":8.5,"steals":1.2,"blocks":0.9,"ts%":0.573,"years":6},
{"name":"Draymond Green","ppg":8.7,"assists":5.6,"rebounds":7.0,"steals":1.3,"blocks":1.0,"ts%":0.516,"years":13},
{"name":"Rudy Gobert","ppg":12.5,"assists":1.3,"rebounds":11.7,"steals":0.7,"blocks":2.1,"ts%":0.679,"years":10},
{"name":"Khris Middleton","ppg":16.9,"assists":3.8,"rebounds":4.8,"steals":1.2,"blocks":0.3,"ts%":0.566,"years":11},
{"name":"Chris Paul","ppg":17.6,"assists":9.4,"rebounds":4.5,"steals":2.1,"blocks":0.1,"ts%":0.531,"years":18},
{"name":"DeMar DeRozan","ppg":21.2,"assists":4.0,"rebounds":4.4,"steals":1.0,"blocks":0.3,"ts%":0.542,"years":15},
{"name":"Bradley Beal","ppg":22.1,"assists":4.3,"rebounds":4.1,"steals":1.1,"blocks":0.4,"ts%":0.548,"years":11},
{"name":"CJ McCollum","ppg":19.9,"assists":3.6,"rebounds":3.5,"steals":0.9,"blocks":0.3,"ts%":0.566,"years":11},
{"name":"Fred VanVleet","ppg":14.6,"assists":5.3,"rebounds":3.3,"steals":1.5,"blocks":0.3,"ts%":0.553,"years":8},
{"name":"Trae Young","ppg":25.5,"assists":9.5,"rebounds":3.6,"steals":1.0,"blocks":0.2,"ts%":0.548,"years":6},
{"name":"Desmond Bane","ppg":17.4,"assists":3.4,"rebounds":4.1,"steals":1.0,"blocks":0.4,"ts%":0.594,"years":3},
{"name":"Jaren Jackson Jr.","ppg":16.1,"assists":1.0,"rebounds":5.5,"steals":0.7,"blocks":2.3,"ts%":0.628,"years":5},
{"name":"Mikal Bridges","ppg":13.5,"assists":2.5,"rebounds":4.3,"steals":1.2,"blocks":0.6,"ts%":0.558,"years":6},
{"name":"Michael Jordan","ppg":30.1,"assists":5.3,"rebounds":6.2,"steals":2.3,"blocks":0.8,"ts%":0.563,"years":15},
{"name":"Wilt Chamberlain","ppg":30.1,"assists":4.4,"rebounds":22.9,"steals":0.0,"blocks":0.0,"ts%":0.548,"years":14},
{"name":"Kareem Abdul-Jabbar","ppg":24.6,"assists":3.6,"rebounds":11.2,"steals":0.9,"blocks":2.6,"ts%":0.603,"years":20},
{"name":"Magic Johnson","ppg":19.5,"assists":11.2,"rebounds":7.2,"steals":1.9,"blocks":0.4,"ts%":0.564,"years":13},
{"name":"Larry Bird","ppg":24.3,"assists":6.3,"rebounds":10.0,"steals":1.7,"blocks":0.8,"ts%":0.572,"years":13},
{"name":"Kobe Bryant","ppg":25.0,"assists":4.7,"rebounds":5.2,"steals":1.4,"blocks":0.5,"ts%":0.537,"years":20},
{"name":"Shaquille O'Neal","ppg":23.7,"assists":2.5,"rebounds":10.9,"steals":0.6,"blocks":2.3,"ts%":0.546,"years":19},
{"name":"Tim Duncan","ppg":19.0,"assists":3.0,"rebounds":10.8,"steals":0.7,"blocks":2.2,"ts%":0.595,"years":19},
{"name":"Hakeem Olajuwon","ppg":21.8,"assists":2.5,"rebounds":11.1,"steals":1.7,"blocks":3.1,"ts%":0.560,"years":18},
{"name":"Oscar Robertson","ppg":25.7,"assists":9.5,"rebounds":7.5,"steals":0.0,"blocks":0.1,"ts%":0.521,"years":14},
{"name":"Dirk Nowitzki","ppg":20.7,"assists":2.4,"rebounds":7.5,"steals":0.8,"blocks":0.8,"ts%":0.581,"years":21},
{"name":"Charles Barkley","ppg":22.1,"assists":3.9,"rebounds":11.7,"steals":1.5,"blocks":0.8,"ts%":0.567,"years":16},
{"name":"Allen Iverson","ppg":26.7,"assists":6.2,"rebounds":3.7,"steals":2.2,"blocks":0.2,"ts%":0.504,"years":14},
{"name":"Dwyane Wade","ppg":22.0,"assists":5.4,"rebounds":4.7,"steals":1.5,"blocks":0.8,"ts%":0.529,"years":16},
{"name":"Kevin Garnett","ppg":17.8,"assists":3.7,"rebounds":10.0,"steals":1.3,"blocks":1.4,"ts%":0.556,"years":21},
{"name":"Karl Malone","ppg":25.0,"assists":3.6,"rebounds":10.1,"steals":1.4,"blocks":0.8,"ts%":0.540,"years":19}
]


print(type(players))

def true_stat_index(tsi_value):
    # Base score with adjusted weights
    score = (
        (tsi_value["ppg"] * tsi_value["ts%"])   # scoring weighted by efficiency
        + (tsi_value["assists"] * 1.5)       # assists weighted more
        + tsi_value["rebounds"]              # rebounds normal
        + (tsi_value["steals"] * 5)          # defense weighted
        + (tsi_value["blocks"] * 5)
    )

    # Longevity bonus: +1% for each career year
    longevity_multiplier = 1 + (player["years"] * 0.015)
    score *= longevity_multiplier

    return score




i = 0
while i < 1:
    player_name_input = input("Enter a player's full name (e.g., LeBron James): ").strip().lower()

    found_player = None
    for player in players:
        if player["name"].lower() == player_name_input:
            found_player = player
            break

    # Print stats and TSI if found
    if found_player:
        print(f"\nStats for {found_player['name']}:")
        for stat, value in found_player.items():
            if stat != "name":
                print(f"  {stat.capitalize()}: {value}")
        tsi = true_stat_index(found_player)
        print(f"  True Stat Index: {tsi:.1f}")
    else:
        print(f"\nPlayer '{player_name_input.capitalize()}' not found. Please check your spelling.")

    continuer = input("Continue? (y/n): ").lower()
    if continuer == "y" or continuer == "yes":
        continue
    elif continuer == "n" or continuer == "no":
        print("Thank you for using Neme's TSI Calculator! Now Closing..")
        break

















