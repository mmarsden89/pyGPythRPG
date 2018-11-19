import pygame, sys, math
from Scripts.UltraColor import *
from Scripts.textures import *


def export_map(file):
	map_data = ""

	#get map dimensions
	max_x = 0
	max_y = 0

	for t in tile_data:
		if t[0] > max_x:
			max_x = t[0]
		if t[1] > max_y:
			max_y = t[1]

	#save map tiles
	for tile in tile_data:
		map_data = map_data + str(int(tile[0] / Tiles.Size)) + "," + str(int(tile[1] / Tiles.Size)) + ":" + tile[2] + "-"

	#save map dimensions
	map_data = map_data + str(int(max_x / Tiles.Size)) + "," + str(int(max_y / Tiles.Size))

	#write file
	with open(file, "w") as mapfile:
		mapfile.write(map_data)


def load_map(file):
	global tile_data
	with open(file, "r") as mapfile:
		map_data = mapfile.read()

	map_data = map_data.split("-")

	map_size = map_data[len(map_data) - 1]
	map_data.remove(map_size)
	map_size = map_size.split(",")
	map_size[0] = int(map_size[0]) * Tiles.Size
	map_size[1] = int(map_size[1]) * Tiles.Size

	tiles = []

	for tile in range(len(map_data)):
		map_data[tile] = map_data[tile].replace("\n", "")
		tiles.append(map_data[tile].split(":"))

	for tile in tiles:
		tile[0] = tile[0].split(",")
		pos = tile[0]
		for p in pos:
			pos[pos.index(p)] = int(p)

		tiles[tiles.index(tile)] = [pos[0] * Tiles.Size, pos[1] * Tiles.Size, tile[1]]

	tile_data = tiles

window = pygame.display.set_mode((1152, 648), pygame.HWSURFACE)
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()

txt_font = pygame.font.SysFont("Verdana.ttf", 20)

mouse_pos = 0
mouse_x, mouse_y = 0, 0

map_width, map_height = 100 * Tiles.Size, 100 * Tiles.Size


selector = pygame.Surface((Tiles.Size, Tiles.Size), pygame.HWSURFACE|pygame.SRCALPHA)
selector.fill(Color.WithAlpha(100, Color.CornflowerBlue))

tile_data = []

camera_x = 0
camera_y = 0
camera_move = 0

brush = "1"


# Initialize Default Map
for x in range(0, map_width, Tiles.Size):
	for y in range(0, map_height, Tiles.Size):
		tile_data.append([x, y, "1"])


isRunning = True

while isRunning:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False

		#movement
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				camera_move = 1
			elif event.key == pygame.K_a:
				camera_move = 2
			elif event.key == pygame.K_s:
				camera_move = 3
			elif event.key == pygame.K_d:
				camera_move = 4

		#brushes
			if event.key == pygame.K_F4:
				brush = "r"

			elif event.key == pygame.K_F1:
				selection = input("Brush Tag: ")
				brush = selection

		#save map
			if event.key == pygame.K_F10:
				name = input("Map Name: ")
				export_map(name + ".map")
				print("Map Saved Successfully")

			elif event.key == pygame.K_F9:
				name = input("Map Name: ")
				load_map(name + ".map")
				print("Map successfully loaded")

		elif event.type == pygame.KEYUP:
			camera_move = 0

		if event.type == pygame.MOUSEMOTION:
			mouse_pos = pygame.mouse.get_pos()
			mouse_x = math.floor(mouse_pos[0] / Tiles.Size) * Tiles.Size
			mouse_y = math.floor(mouse_pos[1] / Tiles.Size) * Tiles.Size

		if event.type == pygame.MOUSEBUTTONDOWN:
			tile = [mouse_x - camera_x, mouse_y - camera_y, brush] #keep as list
			found = False
			for t in tile_data:
				if t[0] == tile[0] and t[1] == tile[1]:
					found = True
					break

			if not found:
				if not brush == "r":
					tile_data.append(tile)

			else:
				if brush == "r":
					#remove tile
					for t in tile_data:
						if t[0] == tile[0] and t[1] == tile[1]:
							tile_data.remove(t)
							print("Tile Removed!")

				else:
					print("A tile is already placed here!")
					print(tile)


		#logic
	if camera_move == 1:
		camera_y += Tiles.Size
	elif camera_move == 3:
		camera_y -= Tiles.Size
	elif camera_move == 2:
		camera_x += Tiles.Size
	elif camera_move == 4:
		camera_x -= Tiles.Size


		#render graphics


	window.fill(Color.Black)

	# dRaw Map
	for tile in tile_data:
		try:
			window.blit(Tiles.Texture_Tags[tile[2]], (tile[0] + camera_x, tile[1] + camera_y))
		except:
			pass


	#DRAW TILE HIGHLTIERGHTERER
	window.blit(selector, (mouse_x, mouse_y))


	pygame.display.update()

	clock.tick(60)


pygame.quit()
sys.exit()