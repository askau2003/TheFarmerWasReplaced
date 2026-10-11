from Sunflower import check_sunflowers
from Plant import plant_entity

plants = [Entities.Grass, Entities.Bush, Entities.Carrot, Entities.Tree, Entities.Pumpkin]
measured = {}

def y_lines(entity, x_pos):
	check_sunflowers(measured)
	#if get_entity_type() == Entities.Pumpkin:
		#print(measure())
		#harvest()
	if get_pos_x() == x_pos:
		if can_harvest() and get_entity_type() in plants:
			harvest()
		plant_entity(entity)