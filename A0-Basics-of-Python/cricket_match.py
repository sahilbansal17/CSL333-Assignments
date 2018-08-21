from random import *
from operator import itemgetter
ml_names = ['ma', 'mb', 'mc', 'md', 'me', 'mf', 'mg', 'mh', 'mi', 'mj', 'mk']
dl_names = ['da', 'db', 'dc', 'dd', 'de', 'df', 'dg', 'dh', 'di', 'dj', 'dk']

# list of dictionary fiels containing all the details of each of the player
ml_stats = []
dl_stats = []

# ml.append({'runs' : 50, 'balls': 25, 'sr': 2.0})
# print(ml)

# add player details to each of the lists
for j in range(2):
	if (j == 0):
		print("Players of the Team ML: \n")
	else:
		print("Players of the Team DL: \n")
	# set initial number of balls for the first player of the team
	current_balls = 20
	for i in range(11):
		# create an empty dictionary to store the details of the player
		player = {}
		# enter the details of the player
		if (j == 0): 
			player['name'] = ml_names[i]
		else :
			player['name'] = dl_names[i]
		player['balls'] = current_balls
		player['runs'] = randint(0, (current_balls - 1)*6)
		player['sr'] = 1.0*player['runs']/player['balls'] 
		# update the no of balls for the next player
		balls_dec = int(randrange(0, 10))
		current_balls = current_balls - balls_dec
		if (current_balls <= 0) :
			current_balls = 2
		print(player)
		if (j == 0) :
			ml_stats.append(player)
		else:
			dl_stats.append(player)
	print("===============================================================")

# function to print the maximum runs made by the DL batsman
def max_runs_DL():
	sort_by_runs = (sorted(dl_stats, key=itemgetter('runs'), reverse = True))
	print("\nMaximum runs scored by the DL batsman is:", sort_by_runs[0]['runs'])
max_runs_DL()

# function to print who scored the maximum runs from both the teams
# and who has the highest SR amongst both the teams
def legend_batsman():
	# sort both the team stats based on the runs scored
	sort_runs_ml = sorted(ml_stats, key=itemgetter('runs'), reverse = True)
	sort_runs_dl = sorted(dl_stats, key=itemgetter('runs'), reverse = True)
	max_ml_score = sort_runs_ml[0]['runs']
	max_dl_score = sort_runs_dl[0]['runs']
	# check which teams top scorer has made the highest no of runs
	if (max_ml_score > max_dl_score):
		print ("Max score is scored by the following ML batsman:", sort_runs_ml[0]['name'], "and the maximum score is:", sort_runs_ml[0]['runs'])
	else:
		print ("Max score is scored by the following DL batsman:", sort_runs_dl[0]['name'], "and the maximum score is:", sort_runs_dl[0]['runs'])

	print ("\n")

	# append the stats of both the teams to find the highest SR among both the teams
	# both_teams = ml_stats
	# both_teams.append(dl_stats)
	# print(both_teams)
	# sort_SR = sorted(both_teams, key=itemgetter('sr'), reverse = True) # This showed some error
	# print("The highest Strike Rate amongst both the teams is:", both_teams[0]['sr'])
	s1 = sorted(ml_stats, key=itemgetter('sr'), reverse = True)
	s2 = sorted(dl_stats, key=itemgetter('sr'), reverse = True)
	if (s1[0]['sr'] > s2[0]['sr']):
		print("The highest SR is : ", s1[0]['sr'], "\n")
	else:
		print("The highest SR is : ", s2[0]['sr'], "\n")
legend_batsman() 

# function to find man of the man_of_the_match
# the player who scores more than 50 runs 
# and has the highest Strike rate among all those
# who scored more than 50 runs 
def man_of_the_match():
    max_sr = 0
    for i in range(11):
        if (ml_stats[i]['runs'] > 50 and ml_stats[i]['sr'] > max_sr):
            player = ml_stats[i]['name']
            max_sr = ml_stats[i]['sr']
        if (dl_stats[i]['runs'] > 50 and dl_stats[i]['sr'] > max_sr):
            player = dl_stats[i]['name']
            max_sr = dl_stats[i]['sr']
    print ("The player who is awarded IIT Jammu presents man of the match prize is: ", player, "\n")
man_of_the_match()

# function to find the player who has the minimum strike rate 
# among all the players of both the teams 
def minimum_SR():
    min_sr = 7.0
    for i in range(11):
        if (dl_stats[i]['sr'] < min_sr):
            player = dl_stats[i]['name']
            min_sr = dl_stats[i]['sr']
        if (ml_stats[i]['sr'] < min_sr):
            player = ml_stats[i]['name']
            min_sr = ml_stats[i]['sr']
    print ("The player recommended for the ongoing test series between India and England is: ", player)
minimum_SR()























