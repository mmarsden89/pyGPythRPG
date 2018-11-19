import pygame, random, math
from Scripts.timer import Timer
from Scripts.globals import Globals
from Scripts.textures import Tiles

pygame.init()



def get_faces(sprite):
	faces = {}

	size = sprite.get_size()
	tile_size = (int(size[0] / 2), int(size[1] / 2))

	south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
	south.blit(sprite, (5, 5), (0, 0, tile_size[0], tile_size[1]))
	faces["south"] = south

	north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
	north.blit(sprite, (5, 5), (tile_size[0], tile_size[1], tile_size[0], tile_size[1]))
	faces["north"] = north

	east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
	east.blit(sprite, (5, 5), (tile_size[0], 0, tile_size[0], tile_size[1]))
	faces["east"] = east

	west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
	west.blit(sprite, (5, 5), (0, tile_size[1], tile_size[0], tile_size[1]))
	faces["west"] = west

	return faces

def MoveNPC(npc):
	npc.facing = random.choice(("south", "north", "east", "west"))
	npc.walking = random.choice((True, False))


class Dialog:

	def __init__(self, text):
		self.Page = 0
		self.Text = text
		
class FaceFace:
	def __init__(self, fpix):
		self.Fpix = fpix



class NPC:

	AllNPCs = []
	BarNPCs = []
	ShopNPCs = []

	def __init__(self, name, pos, fpix, dialog, sprite, scene):
		self.Name = name
		self.X = pos[0] * Tiles.Size
		self.Y = pos[1] * Tiles.Size
		self.Dialog = dialog
		self.width = sprite.get_width()
		self.height = sprite.get_height()
		self.walking = False
		self.Timer = Timer()
		self.Timer.OnNext = lambda: MoveNPC(self)
		self.Timer.Start()
		self.Fpix = fpix
		self.scene = scene

		self.LastLocation = [0, 0]


		#get NPC faces
		self.facing = "south"
		self.faces = get_faces(sprite)

		#publish npc
		if scene == "game":
			NPC.AllNPCs.append(self)
		elif scene == "bar":
			NPC.BarNPCs.append(self)
		elif scene == "shop":
			NPC.ShopNPCs.append(self)

	def Render(self, surface):
		self.Timer.Update()
		if self.walking:
			why = self.Y
			ex = self.X
			move_speed = 60 * Globals.deltatime 
			if self.facing == "south":
				if self.Y < 100 and not Tiles.Blocked_At((round(self.X / Tiles.Size + .05), math.ceil(self.Y / Tiles.Size + .05))):
					self.Y += move_speed
					if self.Y > why + 2:
						move_speed = 0
				else:
					move_speed = 0
			elif self.facing == "north":
				if self.Y > 0 and not Tiles.Blocked_At((round(self.X / Tiles.Size - .05), math.floor(self.Y / Tiles.Size - .05))):
					self.Y -=  move_speed
					if self.Y < why - 2:
						move_speed = 0
				else:
					move_speed = 0
			elif self.facing == "east":
				if self.X > 0 and not Tiles.Blocked_At((math.ceil(self.X / Tiles.Size + .05), round(self.Y / Tiles.Size + .05))):
					self.X -= move_speed
					if self.X > ex + 2:
						move_speed = 0
				else:
					move_speed = 0
			elif self.facing == "west":
				if self.X < 100 and not Tiles.Blocked_At((math.floor(self.X / Tiles.Size - .05), round(self.Y / Tiles.Size - .05))):
					self.X += move_speed
					if self.X < ex - 2:
						move_speed = 0
				else:
					move_speed = 0

			#blocked tile npc standing on
			location = [round(self.X / Tiles.Size), round(self.Y / Tiles.Size)]
			if self.LastLocation in Tiles.Blocked:
				Tiles.Blocked.remove(self.LastLocation)

			if not location in Tiles.Blocked:
				Tiles.Blocked.append(location)
				self.LastLocation = location


		surface.blit(self.faces[self.facing], (self.X + Globals.camera_x, self.Y + Globals.camera_y))


class Male1(NPC):

	def __init__(self, name, pos, fpix = None, dialog = None, scene = None):
		super().__init__(name, pos, fpix, dialog, pygame.image.load("graphics/npc/male1.png"), scene)

class Male2(NPC):
	def __init__(self, name, pos, fpix = None, dialog = None, scene = None):
		super().__init__(name, pos, fpix, dialog, pygame.image.load("graphics/npc/male2.png"), scene)

class Female1(NPC):
	def __init__(self, name, pos, fpix = None, dialog = None, scene = None):
		super().__init__(name, pos, fpix, dialog, pygame.image.load("graphics/npc/girl1.png"), scene)

class Female2(NPC):
	def __init__(self, name, pos, fpix = None, dialog = None, scene = None):
		super().__init__(name, pos, fpix, dialog, pygame.image.load("graphics/npc/girl2.png"), scene)

class Male3(NPC):
	def __init__(self, name, pos, fpix = None, dialog = None, scene = None):
		super().__init__(name, pos, fpix, dialog, pygame.image.load("graphics/npc/malec.png"), scene)

class Male4(NPC):
	def __init__(self, name, pos, fpix = None, dialog = None, scene = None):
		super().__init__(name, pos, fpix, dialog, pygame.image.load("graphics/npc/male4.png"), scene)

class Female3(NPC):
	def __init__(self, name, pos, fpix = None, dialog = None, scene = None):
		super().__init__(name, pos, fpix, dialog, pygame.image.load("graphics/npc/girl3.png"), scene)

class Male5(NPC):
	def __init__(self, name, pos, fpix = None, dialog = None, scene = None):
		super().__init__(name, pos, fpix, dialog, pygame.image.load("graphics/npc/male5.png"), scene)



