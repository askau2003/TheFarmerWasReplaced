def is_even(num):
	return num % 2 == 0

def water_entity():
	if get_water() < 0.5:
		use_item(Items.Water)

def go_to_00():
	while get_pos_x() != 0:
		move(East)
	while get_pos_y() != 0:
		move(North)
		
