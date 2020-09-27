import json

def Position(pos):
	if pos.endswith('11'):
		return pos+'th'
	if pos.endswith('12'):
		return pos+'th'
	if pos.endswith('13'):
		return pos+'th'
	if pos.endswith('1'):
		return pos+'st'
	if pos.endswith('2'):
		return pos+'nd'
	if pos.endswith('3'):
		return pos+'rd'
	return pos+'th'

with open('/home/kooli/Documents/Certs/score.json','r') as file:
	data = json.load(file)
data = data['standings']

#Get Current image & layers
image = gimp.image_list()[0]
team = pdb.gimp_image_get_layer_by_name(image,'team')
points = pdb.gimp_image_get_layer_by_name(image,'points')
position = pdb.gimp_image_get_layer_by_name(image,'position')
for d in data:
	try:
		score = str(d['score'])
		pos = Position(str(d['pos']))
		team_name = str(d['team'])
		#----Team-----
		font = pdb.gimp_text_layer_get_font(team) 
		pdb.gimp_text_layer_set_text(team, team_name)
		pdb.gimp_text_layer_set_font(team, font)
		pdb.gimp_text_layer_set_font_size(team, 113, 0)
		pdb.gimp_layer_set_offsets(team, 960-team.width/2, 500-team.height/2)
		#----Points----
		font = pdb.gimp_text_layer_get_font(points) 
		pdb.gimp_text_layer_set_text(points, score+' pts')
		pdb.gimp_text_layer_set_font_size(points, 62, 0)
		pdb.gimp_text_layer_set_font(points, font)
		pdb.gimp_layer_set_offsets(points, 960-points.width/2, 612-points.height/2)
		#----Position----
		font = pdb.gimp_text_layer_get_font(position) 
		pdb.gimp_text_layer_set_text(position, pos)
		pdb.gimp_text_layer_set_font_size(position, 62, 0)
		pdb.gimp_text_layer_set_font(position, font)
		pdb.gimp_layer_set_offsets(position, 705-position.width/2, 792-position.height/2)
		#Saving image
		new_image = pdb.gimp_image_duplicate(image)
		layer = pdb.gimp_image_merge_visible_layers(new_image, CLIP_TO_IMAGE)
		pdb.gimp_file_save(new_image, layer, '/home/kooli/Documents/Certs/Certs/'+team_name+'.png', '?')
	except Exception :
		continue