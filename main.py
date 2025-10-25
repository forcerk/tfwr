change_hat(Hats.Brown_Hat)
do_a_flip()

while True:
	if get_pos_x() == 0 and get_pos_y() <= 3:
		for i in range(3):
			if can_harvest():
				harvest()
				move(North)
	if get_pos_x() == 1 and get_pos_y() <= 3:
		for i in range (3):
			if can_harvest():
				harvest()
				plant(Entities.Bush)
				move(North)
			elif get_pos_y() == 3:
				move(East)