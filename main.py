world_size = get_world_size()

from Utils import go_to_coords
from lines import y_lines
from Plant import plant_pumpkin
from Plant import plant_entity

def main(count):
	go_to_coords(0,0)
	if count % 5 == 0:
		harvest()
	plant_pumpkin()
	for x in range(world_size):
		for y in range(world_size):
			y_lines(Entities.Tree, 0)
			y_lines(Entities.Carrot, 1)
			y_lines(Entities.Grass, 2)
			y_lines(Entities.Tree, 3)
			y_lines(Entities.Carrot, 4)
			y_lines(Entities.Grass, 5)
			y_lines(Entities.Tree, 6)
			y_lines(Entities.Carrot, 7)
			y_lines(Entities.Grass, 8)
			y_lines(Entities.Tree, 9)
			y_lines(Entities.Carrot, 10)
			y_lines(Entities.Sunflower, 11)
			move(North)
		move(East)
	
count = 0
while True:
	main(count)
	count += 1