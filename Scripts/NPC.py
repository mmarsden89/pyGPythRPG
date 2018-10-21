import pygame, random
from Scripts.timer import Timer
from Scripts.globals import Globals
from Scripts.textures import Tiles

pygame.init()



def get_faces(sprite):
	faces = {}

	size = sprite.get_size()
	tile_size = (int(size[0] / 2), int(size[1] / 2))

	south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
	south.blit(sprite, (0, 0), (0, 0, tile_size[0], tile_size[1]))
	faces["south"] = south

	north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
	north.blit(sprite, (0, 0), (tile_size[0], tile_size[1], tile_size[0], tile_size[1]))
	faces["north"] = north

	east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
	east.blit(sprite, (0, 0), (tile_size[0], 0, tile_size[0], tile_size[1]))
	faces["east"] = east

	west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
	west.blit(sprite, (0, 0), (0, tile_size[1], tile_size[0], tile_size[1]))
	faces["west"] = west

	return faces

def MoveNPC(npc):
	npc.facing = random.choice(("south", "north", "east", "west"))
	npc.walking = random.choice((True, False))


class Dialog:

	def __init__(self, text):
		self.Page = 0
		self.Text = text
		


class NPC:

	AllNPCs = []

	def __init__(self, name, pos, dialog, sprite):
		self.Name = name
		self.X = pos[0]
		self.Y = pos[1]
		self.Dialog = dialog
		self.width = sprite.get_width()
		self.height = sprite.get_height()
		self.walking = False
		self.Timer = Timer()
		self.Timer.OnNext = lambda: MoveNPC(self)
		self.Timer.Start()

		self.LastLocation = (0, 0)


		#get NPC faces
		self.facing = "south"
		self.faces = get_faces(sprite)

		#publish npc
		NPC.AllNPCs.append(self)

	def Render(self, surface):
		self.Timer.Update()
		if self.walking:
			move_speed = 100 * Globals.deltatime 
			if self.facing == "south":
				self.Y += move_speed
			elif self.facing == "north":
				self.Y -=  move_speed
			elif self.facing == "east":
				self.X -= move_speed
			elif self.facing == "west":
				self.X += move_speed

			#blocked tile npc standing on
			location = [round(self.X / Tiles.Size), round(self.Y / Tiles.Size)]
			if self.LastLocation in Tiles.Blocked:
				Tiles.Blocked.remove(self.LastLocation)

			if not location in Tiles.Blocked:
				Tiles.Blocked.append(location)
				self.LastLocation = location


		surface.blit(self.faces[self.facing], (self.X + Globals.camera_x, self.Y + Globals.camera_y))


class Male1(NPC):

	def __init__(self, name, pos, dialog = None):
		super().__init__(name, pos, dialog, pygame.image.load("graphics/npc/male1.png"))





