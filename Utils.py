def is_even(num):
	return num % 2 == 0

def water_entity():
	if get_water() < 0.5:
		use_item(Items.Water)

def go_to_coords(x, y):
	ws = get_world_size()

	steps_x = (x - get_pos_x()) % ws
	if steps_x <= ws // 2:
		for i in range(steps_x):
			move(East)
	else:
		for i in range(ws - steps_x):
			move(West)

	steps_y = (y - get_pos_y()) % ws
	if steps_y <= ws // 2:
		for i in range(steps_y):
			move(North)
	else:
		for i in range(ws - steps_y):
			move(South)
			