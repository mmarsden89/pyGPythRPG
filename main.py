import pygame, sys, time, math
from Scripts.UltraColor import *
from Scripts.textures import *
from Scripts.globals import *
from Scripts.map_engine import * 
from Scripts.NPC import *
from Scripts.meloonatic_gui import *


#Exc.blit(exc, (npc_loc[0], npc_loc[1] - 1))

pygame.init()
clock = pygame.time.Clock()
cSec = 0
cFrame = 0
FPS = 0
deltatime = 0
walkRight = [pygame.image.load('graphics/R1.png'), pygame.image.load('graphics/R2.png'), pygame.image.load('graphics/R3.png'), pygame.image.load('graphics/R4.png'), pygame.image.load('graphics/R5.png'), pygame.image.load('graphics/R6.png'), pygame.image.load('graphics/R7.png'), pygame.image.load('graphics/R8.png'), pygame.image.load('graphics/R9.png')]
walkLeft = [pygame.image.load('graphics/L1.png'), pygame.image.load('graphics/L2.png'), pygame.image.load('graphics/L3.png'), pygame.image.load('graphics/L4.png'), pygame.image.load('graphics/L5.png'), pygame.image.load('graphics/L6.png'), pygame.image.load('graphics/L7.png'), pygame.image.load('graphics/L8.png'), pygame.image.load('graphics/L9.png')]
walkNorth = [pygame.image.load('graphics/N1.png'), pygame.image.load('graphics/N2.png'), pygame.image.load('graphics/N3.png'), pygame.image.load('graphics/N4.png'), pygame.image.load('graphics/N5.png'), pygame.image.load('graphics/N6.png'), pygame.image.load('graphics/N7.png'), pygame.image.load('graphics/N8.png'), pygame.image.load('graphics/N9.png')]
walkSouth = [pygame.image.load('graphics/S6.png'), pygame.image.load('graphics/S7.png'), pygame.image.load('graphics/S8.png'), pygame.image.load('graphics/S9.png'), pygame.image.load('graphics/S1.png'), pygame.image.load('graphics/S2.png'), pygame.image.load('graphics/S3.png'), pygame.image.load('graphics/S4.png'), pygame.image.load('graphics/S5.png')]
layDown = [pygame.image.load('graphics/lay1.png'), pygame.image.load('graphics/lay2.png'), pygame.image.load('graphics/lay3.png'), pygame.image.load('graphics/lay4.png'), pygame.image.load('graphics/lay5.png'), pygame.image.load('graphics/lay6.png'), pygame.image.load('graphics/lay7.png'), pygame.image.load('graphics/lay8.png'), pygame.image.load('graphics/lay9.png')]

treeto = pygame.image.load("graphics/treeto.png")
house1to = pygame.image.load("graphics/house1to.png")
house2to = pygame.image.load("graphics/house2to.png")
house3to = pygame.image.load("graphics/house3to.png")
house3sto = pygame.image.load("graphics/house3sto.png")
Treeto = pygame.Surface((6000, 6000), pygame.HWSURFACE|pygame.SRCALPHA)
Treeto.blit(treeto, (840, 480))
Treeto.blit(treeto, (1200, 480))
Treeto.blit(treeto, (840, 900))
Treeto.blit(treeto, (1260, 900))
Treeto.blit(treeto, (2220, 1440))
Treeto.blit(treeto, (2580, 1440))
Treeto.blit(treeto, (2160, 420))
Treeto.blit(treeto, (2520, 240))
Treeto.blit(house1to, (1680, 660))
Treeto.blit(house2to, (1680, 1080))
Treeto.blit(house3to, (2100, 780))
Treeto.blit(house3sto, (2100, 1200))


keypressed = False

terrain = Map_Engine.load_map("maps/world.map")
#

fps_font = pygame.font.SysFont("Verdana.ttf", 20)

sky = pygame.image.load("graphics/sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0, 0))
del sky

dialog_background = pygame.image.load("graphics/gui/dialog.png")
Dialog_Background = pygame.Surface(dialog_background.get_size(), pygame.HWSURFACE|pygame.SRCALPHA)
Dialog_Background.blit(dialog_background, (0, 0))
Dialog_Background_Width, Dialog_Background_Height = Dialog_Background.get_size()
del dialog_background

inventory_background = pygame.image.load("graphics/gui/inventory.png")
Inventory_Background = pygame.Surface(inventory_background.get_size(), pygame.HWSURFACE|pygame.SRCALPHA)
Inventory_Background.blit(inventory_background, (0, 0))
Inventory_Background_Width, Inventory_Background_Height = Inventory_Background.get_size()
del inventory_background



class player(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = 30
		self.height = 60
		self.left = False
		self.right = False
		self.down = True
		self.up = False
		self.walkCount = 0
		self.standing = True
		self.laying = False
		self.facepix = pygame.image.load("graphics/budface.png")

	def draw(self, window):

		if not(self.standing):
			if self.walkCount + 1 >= 27:
				self.walkCount = 3
			if self.left:
				window.blit(walkLeft[self.walkCount//3], (self.x,self.y))
				self.walkCount += 1
			elif self.right:
				window.blit(walkRight[self.walkCount//3], (self.x,self.y))
				self.walkCount += 1
			elif self.down:
				window.blit(walkSouth[self.walkCount//3], (self.x, self.y))
				self.walkCount += 1
			elif self.up:
				window.blit(walkNorth[self.walkCount//3], (self.x, self.y))
				self.walkCount += 1
			elif self.laying:
				window.blit(layDown[self.walkCount//3], (self.x, self.y))
				self.walkCount += 1

		else:
			if self.right:
				window.blit(walkRight[0], (self.x, self.y))
			elif self.left:
				window.blit(walkLeft[0], (self.x, self.y))
			elif self.up:
				window.blit(walkNorth[0], (self.x, self.y))
			elif self.down:
				window.blit(walkSouth[0], (self.x, self.y))



def show_fps():
	fps_overlay = fps_font.render(str(FPS), True, Color.Goldenrod)
	window.blit(fps_overlay, (0, 0))

def create_window():
	global window, window_height, window_width, window_title
	window_width, window_height = 800, 600
	window_title = "Game game"
	pygame.display.set_caption(window_title)
	window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.SRCALPHA)
	clock = pygame.time.Clock()


def count_fps():
	global FPS

	FPS = clock.get_fps()
	if FPS > 0:
		Globals.deltatime = 1 / FPS


create_window()


## "game"
man1 = Male2(name = "Brian", pos = (5, 6), fpix = pygame.image.load("graphics/manface2.png"), dialog = Dialog(text = [("Hey man",), ("How are you doing?",), ("Welcome to town!",), ("Have a good time!",)]), scene = "game")
man2 = Male1(name = "David", pos = (9, 13), fpix = pygame.image.load("graphics/manface1.png"), dialog = Dialog(text = [("Hey du",), ("What's up?",), ("Yes?",), ("Can I help you with something?",)]), scene = "game")
man3 = Female1(name = "Janeen", pos = (50, 16), fpix = pygame.image.load("graphics/girlface1.png"), dialog = Dialog(text = [("Hey",), ("Sorry, not much to say",), ("What's up?",), ("Yes?",), ("Can I help you with something?",)]), scene = "game")
man4 = Male2(name = "Jerry", pos = (10, 30), fpix = pygame.image.load("graphics/manface2.png"), dialog = Dialog(text = [("Oh! Hey Dude, hows it hanging?",), (" Whats up man?",), ("What's up?",), ("Yes?",), ("Can I help you with something?",)]), scene = "game")
man5 = Male5(name = "John", pos = (20, 24), fpix = pygame.image.load("graphics/manface5.png"), dialog = Dialog(text = [("I hate the weather this time of year",), ("Isn't it bland?",), ("Yes?",), ("The absolute worst",)]), scene = "game")
man6 = Male2(name = "Joe", pos = (13, 18), fpix = pygame.image.load("graphics/manface2.png"), dialog = Dialog(text = [("I heard that they're rebooting Twilight",), ("I cant wait!",), ("Are you team Edward?",), ("I'm team CHARLIE",)]), scene = "game")
man7 = Female1(name = "Margaret", pos = (29, 42), fpix = pygame.image.load("graphics/girlface1.png"), dialog = Dialog(text = [("I feel like Greta Van Fleet is a total Zeppelin rip-off"), ("Do you think?",), ("Could be",), ("Maybe I'm just a grump",)]), scene = "game")
man8 = Female3(name = "Lorah", pos = (16, 21), fpix = pygame.image.load("graphics/girlface3.png"), dialog = Dialog(text = [("Hello Hello",), ("Something Something",), ("Vertigo",), ("U2 Sucks big time",)]), scene = "game")
man9 = Female2(name = "Debra", pos = (35, 28), fpix = pygame.image.load("graphics/girlface2.png"), dialog = Dialog(text = [("Have you heard of Hunter S. Thompson?",), ("My girlfriend hand't",), ("Neither did her friends. I kinda felt like an idiot",), ("Also, sort of like a snob",)]), scene = "game")
man10 = Male2(name = "Miguel", pos = (3, 28), fpix = pygame.image.load("graphics/manface2.png"), dialog = Dialog(text = [("I'm worried about the country",), ("Bunch of libtards walking around",), ("It's time we take action",), ("All hail TRUMP",)]), scene = "game")
man11 = Male3(name = "Zorro", pos = (12, 50), fpix = pygame.image.load("graphics/manface3.png"), dialog = Dialog(text = [("go sox",), ("GO SOX",), ("Tom Brady is my God",)]), scene = "game")
man12 = Female2(name = "Tammy", pos = (45, 28), fpix = pygame.image.load("graphics/girlface2.png"), dialog = Dialog(text = [("I can't get over this cold",), ("ah",), ("AH",), ("ACHUUUU",)]), scene = "game")
man13 = Male4(name = "Tommy", pos = (3, 28), fpix = pygame.image.load("graphics/manface4.png"), dialog = Dialog(text = [("I'm worried about the country",), ("Bunch of libtards walking around",), ("It's time we take action",), ("All hail TRUMP",)]), scene = "game")
man14 = Male3(name = "Douglas", pos = (19, 9), fpix = pygame.image.load("graphics/manface3.png"), dialog = Dialog(text = [("Don't stop me now",), ("cause I'm having such a good time",), ("I'm having a ball!",)]), scene = "game")
man14 = Male4(name = "Michaelo", pos = (40, 15), fpix = pygame.image.load("graphics/manface4.png"), dialog = Dialog(text = [("I think I need to stop drinking coffee",), ("I have about 10-12 c-c-c-cups a day",), ("Is the ground shaking or is it just me?",)]), scene = "game")
man14 = Female3(name = "Angela", pos = (26, 8), fpix = pygame.image.load("graphics/girlface3.png"), dialog = Dialog(text = [("Doesn't it look lovely?",), ("I'm waiting for some geese",), ("Hopefully Matt gets to it soon!",)]), scene = "game")

## "bar"
man15 = Male3(name = "Pedro", pos = (26, 16), fpix = pygame.image.load("graphics/manface3.png"), dialog = Dialog(text = [("Don't stop me now",), ("cause I'm having such a good time",), ("I'm having a ball!",)]), scene = "bar")

## "shop"
man16 = Female2(name = "Ianna", pos = (24, 22), fpix = pygame.image.load("graphics/girlface2.png"), dialog = Dialog(text = [("Don't stop me now",), ("cause I'm having such a good time",), ("I'm having a ball!",)]), scene = "shop")



#initalize music
pygame.mixer.music.load("music/newtitle.wav")
pygame.mixer.music.play(-1)

# initialize sounds
btnSound = pygame.mixer.Sound("sounds/button.wav")
footsteps = pygame.mixer.Sound("sounds/footsteps.wav")
footsteps.set_volume(.2)

# initialize gui

def Play():
	Globals.scene = "game"
	pygame.mixer.music.load("music/forest.wav")
	pygame.mixer.music.play(-1)

def Exit():
	global isRunning
	isRunning = False

def BarScene():
	pygame.mixer.music.load("music/title.wav")
	pygame.mixer.music.play(-1)
	Globals.scene = "bar"

def ShopScene():
	Globals.scene = "shop"

btnPlay = Menu.Button(text = "Play", rect = (0, 0, 300, 60), tag = ("menu", None))

btnPlay.Left = window_width / 2 - btnPlay.Width / 2
btnPlay.Top = window_height / 2 - btnPlay.Height / 2
btnPlay.Command = Play


btnExit = Menu.Button(text = "Exit", rect = (0, 0, 300, 60), tag = ("menu", None))
btnExit.Left = btnPlay.Left
btnExit.Top = btnPlay.Top + btnExit.Height + 3
btnExit.Command = Exit

menuTitle = Menu.Text(text = "Welcome to Game Game!", color = Color.IndianRed, font = Font.Large)
menuTitle.Left, menuTitle.Top = window_width / 2 - menuTitle.Width / 2, 0

bud_width, bud_height = 30, 60
bud_x = (window_width / 2 - bud_width / 4)
bud_y = (window_height / 2 - bud_height / 4)
bud = player(bud_x, bud_y, bud_width, bud_height)

exc = pygame.image.load("graphics/exc.png")
exc = exc.convert_alpha()
Exc = pygame.Surface((30,30), pygame.HWSURFACE|pygame.SRCALPHA)

inventory = False

isRunning = True
while isRunning:
	clock.tick(30)


	location = [(Globals.camera_x / Tiles.Size - 6.5) * -1, (Globals.camera_y / Tiles.Size - 5) * -1]

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False


		if event.type == pygame.KEYDOWN:

			location = [(Globals.camera_x / Tiles.Size - 6.5) * -1, (Globals.camera_y / Tiles.Size - 5) * -1]

			print(location)

			if event.key == pygame.K_w and not Globals.dialog_open:
				footsteps.stop()
				footsteps.play(-1)
				Globals.camera_move = 1
				bud.up = True
				bud.down = False
				bud.left = False
				bud.right = False					
				bud.standing = False

			elif event.key == pygame.K_s and not Globals.dialog_open:
				footsteps.stop()
				footsteps.play(-1)
				#footsteps.play()
				Globals.camera_move = 2
				bud.down = True
				bud.up = False
				bud.left = False
				bud.right = False
				bud.standing = False

			elif event.key == pygame.K_a and not Globals.dialog_open:
				footsteps.stop()
				footsteps.play(-1)
				#footsteps.play()
				Globals.camera_move = 3
				bud.left = True
				bud.right = False
				bud.down = False
				bud.up = False
				bud.standing = False

			elif event.key == pygame.K_d and not Globals.dialog_open:
				footsteps.stop()
				footsteps.play(-1)
				#footsteps.play()
				Globals.camera_move = 4
				bud.left = False
				bud.right = True
				bud.down = False
				bud.up = False
				bud.standing = False

			elif event.key == pygame.K_SPACE and not Globals.dialog_open:
				bud.left = False
				bud.right = False
				bud.down = False
				bud.up = False
				bud.standing = False
				bud.laying = True

			elif event.key == pygame.K_i and not Globals.dialog_open:
				if inventory != True:
					bud.standing = True
					inventory = True
				else:
					inventory = False

		#quit button not working currently ******
		#if event.type == pygame.KEYDOWN:
		#	if event.key == pygame.K_q:
		#		break

			if event.key == pygame.K_RETURN:
				if Globals.dialog_open:
				#handle next page
					if Globals.active_dialog.Page < len(Globals.active_dialog.Text) - 1:
						Globals.active_dialog.Page += 1
					else:
						Globals.dialog_open = False
						Globals.active_dialog.Page = len(Globals.active_dialog.Text) - 1
						Globals.active_dialog = None
						Globals.exclamation = False


						#unpause paused npcs
						for npc in NPC.AllNPCs:
							Globals.exclamation = True
							if not npc.Timer.Active:
								npc.Timer.Start()


				### SCENE LOGIC
				elif Globals.scene == "game" and location[0] >= 28 and location[0] <= 30 and location[1] >= 16 and location[1] <= 17:
					pygame.mixer.music.fadeout(3000)
					footsteps.stop()
					del Tiles.Blocked[:]
					terrain = Map_Engine.load_map("maps/bar.map")
					pygame.time.delay(100)
					BarScene()

				elif Globals.scene == "bar" and location[0] >= 28 and location[0] <= 30 and location[1] >= 16 and location[1] <= 17:
					pygame.mixer.music.fadeout(3000)
					footsteps.stop()
					del Tiles.Blocked[:]
					terrain = Map_Engine.load_map("maps/world.map")
					Play()

				elif Globals.scene == "game" and location[0] >= 28 and location[0] <= 30 and location[1] >= 23 and location[1] <= 24:
					pygame.mixer.music.fadeout(3000)
					footsteps.stop()
					del Tiles.Blocked[:]
					terrain = Map_Engine.load_map("maps/shop.map")
					ShopScene()


				elif Globals.scene == "shop" and location[0] >= 28 and location[0] <= 30 and location[1] >= 23 and location[1] <= 24:
					pygame.mixer.music.fadeout(3000)
					footsteps.stop()
					del Tiles.Blocked[:]
					terrain = Map_Engine.load_map("maps/world.map")
					Play()
				### END SCENE LOGIC

				else:
					#if dialoge isnt open
					for npc in NPC.AllNPCs:
						#is player in speach bounds
						#player coords are by tile
						#npcs cords are by pixel
						npc_loc = [(npc.X / Tiles.Size), (npc.Y / Tiles.Size)]
						if location[0] >= npc_loc[0] - 2 and location[0] <= npc_loc[0] + 2 and location[1] >= npc_loc[1] - 2 and location[1] <= npc_loc[1] + 2:
						#player is next to npc, however is player facing?
							if bud.up and npc_loc[1] <= location[1]:
								Globals.active_face = npc.Fpix
								Globals.active_name = npc.Name
								Globals.dialog_open = True
								Globals.active_dialog = npc.Dialog
								npc.Timer.Pause()
								npc.walking = False
							elif bud.down and npc_loc[1] >= location[1]:
								Globals.active_face = npc.Fpix
								Globals.active_name = npc.Name
								Globals.dialog_open = True
								Globals.active_dialog = npc.Dialog
								npc.Timer.Pause()
								npc.walking = False
							elif bud.left and npc_loc[0] <= location[0]:
								Globals.active_face = npc.Fpix
								Globals.active_name = npc.Name
								Globals.dialog_open = True
								Globals.active_dialog = npc.Dialog
								npc.Timer.Pause()
								npc.walking = False
							elif bud.right and npc_loc[0] >= location[0]:
								Globals.active_face = npc.Fpix
								Globals.active_name = npc.Name
								Globals.dialog_open = True
								Globals.active_dialog = npc.Dialog
								npc.Timer.Pause()
								npc.walking = False



		elif event.type == pygame.KEYUP:
			footsteps.stop()
			Globals.camera_move = 0
			bud.standing = True
			walkCount = 0


		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1: #left click

				#handle button click events
				for btn in Menu.Button.All:
					if btn.Tag[0] == Globals.scene and btn.Rolling:
						if btn.Command != None:
							btn.Command() #do button event
						btnSound.play()
						btn.Rolling = False
						break #exit loop





		# old logic for player/camera movement
	if Globals.camera_move == 1: #W
			#if not Tiles.Blocked_At((round(bud_x), math.floor(bud_y))):
		if location[1] > 0 and not Tiles.Blocked_At((round(location[0]), math.floor(location[1]))):
			Globals.camera_y -= -135 * Globals.deltatime #speed
	elif Globals.camera_move == 2: #S
			#if not Tiles.Blocked_At((round(bud_x), math.ceil(bud_y))):
		if location[1] < 98 and not Tiles.Blocked_At((round(location[0]), math.ceil(location[1]))):
			Globals.camera_y -= 135 * Globals.deltatime#speed
	elif Globals.camera_move == 3: #3 is A
		#if not Tiles.Blocked_At((math.floor(bud_x), round(bud_y))):
		if location[0] > 0 and not Tiles.Blocked_At((math.floor(location[0]), round(location[1]))):
			Globals.camera_x -= -135 * Globals.deltatime#speed
	elif Globals.camera_move == 4: #4 is D
		#if not Tiles.Blocked_At((math.ceil(bud_x), round(bud_y))):
		if location[0] < 98 and not Tiles.Blocked_At((math.ceil(location[0]), round(location[1]))):
			Globals.camera_x -= 135 * Globals.deltatime#speed

	if Globals.scene == "game":

		#Render Graphics in game
		window.blit(Sky, (0, 0))

		window.blit(terrain, (Globals.camera_x, Globals.camera_y))

		surface1 = pygame.Surface((60,60))
		surface1.set_colorkey((0,0,0))
		surface1.set_alpha(60)
		pygame.draw.circle(surface1, (20,20,20), (50,50), 12)
		window.blit(surface1, (372.5,285))

		location = [(Globals.camera_x / Tiles.Size - 6.5) * -1, (Globals.camera_y / Tiles.Size - 5) * -1]



		for npc in NPC.AllNPCs:
			npc.Render(window)


		bud.draw(window)
		#pygame.draw.rect(window, Color.Red, (location[0] * Tiles.Size + Globals.camera_x, location[1] * Tiles.Size + Globals.camera_y, Tiles.Size, Tiles.Size), 2)

		for npc in NPC.AllNPCs:
			npc_loc = [(npc.X / Tiles.Size), (npc.Y / Tiles.Size)]
			if location[0] >= npc_loc[0] - 1.5 and location[0] <= npc_loc[0] + 1.5 and location[1] >= npc_loc[1] - 1.5 and location[1] <= npc_loc[1] + 1.5 and Globals.exclamation == True:
				Exc.blit(exc, (0, 0))
				window.blit(Exc, (npc.X + 20 + Globals.camera_x, npc.Y + Globals.camera_y - 30))

		window.blit(Treeto, (Globals.camera_x, Globals.camera_y))

		if Globals.dialog_open:
			window.blit(Dialog_Background, (window_width / 2 - Dialog_Background_Width / 2, window_height - Dialog_Background_Height - 2))

		#draw dialog text
			if Globals.active_dialog != None:
				lines = Globals.active_dialog.Text[Globals.active_dialog.Page]

				for line in lines:
					#draw text to screen
					window.blit(Font.Default.render(line, True, Color.White), (275, (window_height - Dialog_Background_Height) + 50 + (lines.index(line)) * 25))

				window.blit(Globals.active_face, (135, 425))
				window.blit(Font.Default.render(Globals.active_name, True, Color.White), (window_width / 5 - len(Globals.active_name) / 3, 535))

		#for t in Tiles.Blocked:
		#	pygame.draw.rect(window, Color.Red, (t[0] * Tiles.Size + Globals.camera_x, t[1] * Tiles.Size + Globals.camera_y, Tiles.Size, Tiles.Size), 2)

	elif Globals.scene == "bar":

		#render graphics in bar
		window.fill(Color.Black)

		window.blit(terrain, (Globals.camera_x, Globals.camera_y))

		for npc in NPC.BarNPCs:
			npc.Render(window)


		bud.draw(window)

		if Globals.dialog_open:
			window.blit(Dialog_Background, (window_width / 2 - Dialog_Background_Width / 2, window_height - Dialog_Background_Height - 2))

		#draw dialog text
			if Globals.active_dialog != None:
				lines = Globals.active_dialog.Text[Globals.active_dialog.Page]

				for line in lines:
					#draw text to screen
					window.blit(Font.Default.render(line, True, Color.White), (275, (window_height - Dialog_Background_Height) + 50 + (lines.index(line)) * 25))

				window.blit(Globals.active_face, (135, 425))
				window.blit(Font.Default.render(Globals.active_name, True, Color.White), (window_width / 5 - len(Globals.active_name) / 3, 535))


	elif Globals.scene == "shop":

		window.fill(Color.Black)

		window.blit(terrain, (Globals.camera_x, Globals.camera_y))

		for npc in NPC.ShopNPCs:
			npc.Render(window)

		bud.draw(window)

		if Globals.dialog_open:
			window.blit(Dialog_Background, (window_width / 2 - Dialog_Background_Width / 2, window_height - Dialog_Background_Height - 2))


	#process menu
	elif Globals.scene == "menu":
		window.fill(Color.Fog)

		menuTitle.Render(window)

		for btn in Menu.Button.All:
			if btn.Tag[0] == "menu":
				btn.Render(window)


	if inventory == True:
		window.blit(Inventory_Background, (window_width / 2 - Dialog_Background_Width / 2, window_height - Dialog_Background_Height - 2))

	show_fps()


	pygame.display.update()

	count_fps()




	#render scene
time.sleep(1)
pygame.quit()
sys.exit()