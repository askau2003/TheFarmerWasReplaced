import Utils

world_size = get_world_size()

def plant_entity(entity):
	if entity == Entities.Grass:
		if get_ground_type() != Grounds.Grassland:
			till()
		#plant(Entities.Grass)
	elif entity == Entities.Bush:
		if get_ground_type() != Grounds.Soil:
			till()
		#Utils.water_entity()
		plant(Entities.Bush)
	elif entity == Entities.Carrot:
		if get_ground_type() != Grounds.Soil:
			till()
		#Utils.water_entity()
		plant(Entities.Carrot)
	if entity == Entities.Tree:
		if get_ground_type() != Grounds.Soil:
			till()
		if Utils.is_even(get_pos_y()):
			plant(Entities.Tree)
			#Utils.water_entity()
	elif entity == Entities.Sunflower:
		if get_ground_type() != Grounds.Soil:
			till()
		#Utils.water_entity()
		plant(Entities.Sunflower)
	elif entity == Entities.Pumpkin:
		if get_ground_type() != Grounds.Soil:
			till()
		#Utils.water_entity()
		plant(Entities.Pumpkin)
		if get_entity_type() == Entities.Dead_Pumpkin:
			plant(Entities.Pumpkin)