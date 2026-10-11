world_size = get_world_size()

from Utils import go_to_00
from lines import y_lines

def main():
	go_to_00()
	if get_pos_x() == 0 and get_pos_y() == 0:
		for x in range(world_size):
			for y in range(world_size):
				y_lines(Entities.Grass,0)
				y_lines(Entities.Tree,1)
				y_lines(Entities.Carrot,2)
				y_lines(Entities.Carrot,3)
				y_lines(Entities.Carrot,4)
				y_lines(Entities.Sunflower,5)
				y_lines(Entities.Pumpkin,6)
				y_lines(Entities.Pumpkin,7)
				y_lines(Entities.Pumpkin,8)
				y_lines(Entities.Pumpkin,9)
				y_lines(Entities.Pumpkin,10)
				y_lines(Entities.Pumpkin,11)
				move(North)
			move(East)

while True:
	main()