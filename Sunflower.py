from Plant import plant_entity

def check_sunflowers(measured):
	max_val_key = None
	max_val = 0
	if get_entity_type() == Entities.Sunflower:
		y_pos = get_pos_y()
		measured[y_pos] = measure()
		if y_pos != get_world_size() - 1:
			return
		while len(measured) > 0:
			max_val = 0
			for key in measured:
				if measured[key] > max_val:
					max_val = measured[key] 
					max_val_key = key
			while get_pos_y() > max_val_key:
				move(South)
			while get_pos_y() < max_val_key:
				move(North)
			harvest()
			plant_entity(Entities.Sunflower)
			measured.pop(max_val_key)
		while get_pos_y() != get_world_size() - 1:
			move(North)