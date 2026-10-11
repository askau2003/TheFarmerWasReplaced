import Utils

world_size = get_world_size()

def plant_entity(entity):
	if get_entity_type() == Entities.Pumpkin or get_entity_type() == Entities.Dead_Pumpkin:
		return
	elif entity == Entities.Sunflower:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Sunflower)
	elif entity == Entities.Grass:
		if get_ground_type() != Grounds.Grassland:
			till()
		plant(Entities.Grass)
	elif entity == Entities.Tree:
		if get_ground_type() != Grounds.Soil:
			till()
		if Utils.is_even(get_pos_y()):
			plant(Entities.Tree)
	elif entity == Entities.Carrot:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
	#elif entity == None:
		#plant(Entities.Grass)
		#planttype, (x, y) = get_companion()
		#plants = [Entities.Grass, Entities.Bush, Entities.Tree]
		#if planttype == Entities.Carrot:
			#if get_ground_type() != Grounds.Soil:
				#till()
				#plant(Entities.Carrot)
		#if planttype in plants:
			#Utils.go_to_coords(x, y)
			#plant(planttype)
			#return

def plant_pumpkin():
	for x in range(6):
		for y in range(6):
			if get_ground_type() != Grounds.Soil:
				till()
			if get_entity_type() != Entities.Pumpkin:
				plant(Entities.Pumpkin)
			elif get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)
			move(North)
		for y in range(6):
			move(South)
		move(East)
	for x in range(6):
		move(West)