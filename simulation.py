# Importing Packages
import matplotlib.pyplot as plt
import random as rd

#List of teams that reached the round of 16 for the 2023 Champions League
Teams = [['NAP','A',1,'ITA' ],['LIV','A',2,'ENG'],['POR','B',1,'POR'],['BRU','B',2,'BEL'],['BAY','C',1,'GER'],
                  ['INT','C',2,'ITA'], ['TOT','D',1,'ENG'],['FRA','D',2,'GER'],['CHE','E',1,'ENG'],['MIL','E',2,'ITA'],
                  ['Real','F',1,"SPA"],['LEI','F',2,'ENG'],['ManC','G',1,"ENG"],['DOR','G',2,'GER'],['BEN','H',1,'POR'],
                  ['PSG','H',2,'FRA']]


#Game simulation

def separate_first_and_second_place(teams):
    first_rank_teams = []
    second_rank_teams = []
    for t in teams:
        if t[2] == 1:
            first_rank_teams.append(t)
        else:
            second_rank_teams.append(t)
    return first_rank_teams,second_rank_teams



def randomly_select_second_place_team(second_teams_left):
    """
    Choose a second ranked team and update the ballot box
    """
    e = 0
    if (len(second_teams_left) != 0):
        e = rd.randint(0,len(second_teams_left)-1)
    team_picked = second_teams_left[e]
    second_teams_left.pop(e)
    return team_picked

def randomly_select_team_opponent(first_place_teams,potential_opponents):
    """
    Choose a second ranked team and update the ballot box
    """
    e = 0
    if (len(potential_opponents) == 0):
        return '0'
    if (len(potential_opponents) != 0):
        e = rd.randint(0,len(potential_opponents)-1)
    team_picked = potential_opponents[e]
    first_place_teams.remove(team_picked)
    return team_picked

def list_of_possible_matches(teams):
    matches = []
    first, second = separate_first_and_second_place(teams)
    for f in first:
        for s in second:
            matches.append(f[0]+s[0])
    return matches


def list_of_potential_opponents(second_ranked_teams_picked,first_ranked_teams_left):
    potential_opponents = []
    for t in first_ranked_teams_left:
        if second_ranked_teams_picked[1] != t[1] and second_ranked_teams_picked[3] != t[3]:
            potential_opponents.append(t)

    return potential_opponents

def draw(teams):
    """
    Drawing according to UEFA rules
    """

    first_rank_teams, second_rank_teams = separate_first_and_second_place(teams)
    matches = []
    while len(second_rank_teams) != 0:
        picked_team = randomly_select_second_place_team(second_rank_teams) # a team is picked among the second-place teams
        opponents = list_of_potential_opponents(picked_team,first_rank_teams) # list of potential opponents of the team picked
        opponent = randomly_select_team_opponent(first_rank_teams, opponents) #  an opponent is picked
        matches.append(opponent[0] + picked_team[0])
    return matches


"""SIMULATION"""

# Inputs
num_simulations = 10000
# Tracking

matches = list_of_possible_matches(Teams)

#Initializing probabilities
probabilities = {}
for m in matches:
    key = str(m)
    probabilities[key] = 0

for key, value in probabilities.items():
    exec(f'{key}={value}')


def simulation(teams,N):

    for i in range(N):
        draw_result = draw(teams)
        for versus in draw_result:
            probabilities[versus] += 1

    for m in matches:
        probabilities[m] /= N

    return probabilities









