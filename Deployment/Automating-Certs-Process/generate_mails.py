import csv
import json


teams = []
with open('Fword CTF-teams.csv') as csvfil:
	t = csv.reader(csvfil, delimiter=',')
	for team in t:
		teams.append({'id':team[0],'name':team[2],'emails':[]})

with open('Fword CTF-users.csv') as csvfile:
	users = csv.reader(csvfile, delimiter=',')
	for u in users:
		for t in teams:
			if u[14]==t['id']:
				t['emails'].append(u[4])
				break
		
print teams

with open('team_mail.json', 'w') as outfile:
    json.dump(teams, outfile)