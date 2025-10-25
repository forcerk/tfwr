change_hat(Hats.Brown_Hat)
do_a_flip()

clear()
move(East)
for i in range (3):
	plant(Entities.Bush)
	move(North)
move(East)
for i in range(3):
	till()
	plant(Entities.Carrot)
	move(North)
move(East)

while True:
	if get_entity_type() == Entities.Grass:
		for i in range(3):
			if can_harvest():
				harvest()
				move(North)
		move(East)
	if get_entity_type() == Entities.Bush:
		for i in range(3):
			if get_water() < 1:
				use_item(Items.Water)
			if can_harvest():
				harvest()
				plant(Entities.Bush)
				move(North)
		move(East)
	if get_entity_type() == Entities.Carrot:
		for i in range(3):
			if get_water() < 1:
				use_item(Items.Water)
			if can_harvest():
				harvest()
				plant(Entities.Carrot)
				move(North)
		move(East)