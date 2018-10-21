import pygame, sys, time, math
from Scripts.UltraColor import *
from Scripts.textures import *
from Scripts.globals import *
from Scripts.map_engine import * 
from Scripts.NPC import *
from Scripts.player import *
from Scripts.meloonatic_gui import *


pygame.init()

cSec = 0
cFrame = 0
FPS = 0


terrain = Map_Engine.load_map("maps/world.map")

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

clock = pygame.time.Clock()

def show_fps():
	fps_overlay = fps_font.render(str(FPS), True, Color.Goldenrod)
	window.blit(fps_overlay, (0, 0))

def create_window():
	global window, window_height, window_width, window_title
	window_width, window_height = 800, 600
	window_title = "Game game"
	pygame.display.set_caption(window_title)
	window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
	clock = pygame.time.Clock()

def count_fps():
	global FPS

	FPS = clock.get_fps()
	if FPS > 0:
		Globals.deltatime = 1 / FPS

create_window()

player = Player("GrassyKnolls")
player_w, player_h = player.width, player.height
player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size
player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size


man1 = Male1(name = "Eyo", pos = (300, 400), dialog = Dialog(text = [("Hey man", "How are you doing?"), ("What's up?", "Can you bugger off?")]))
man2 = Male1(name = "David", pos = (800, 680), dialog = Dialog(text = [("Hey du", "What's up?"), ("Yes?", "Can I help you with something?")]))
man3 = Male1(name = "Brian", pos = (580, 450), dialog = Dialog(text = [("Hey", "Sorry, not much to say")]))

#initalize music
pygame.mixer.music.load("music/title.wav")
pygame.mixer.music.play(-1)

# initialize sounds
btnSound = pygame.mixer.Sound("sounds/button.wav")

# initialize gui

def Play():
	Globals.scene = "game"
	pygame.mixer.music.load("music/forest.wav")
	pygame.mixer.music.play(-1)

def Exit():
	global isRunning
	isRunning = False

btnPlay = Menu.Button(text = "Play", rect = (0, 0, 300, 60), tag = ("menu", None))

btnPlay.Left = window_width / 2 - btnPlay.Width / 2
btnPlay.Top = window_height / 2 - btnPlay.Height / 2
btnPlay.Command = Play


btnExit = Menu.Button(text = "Exit", rect = (0, 0, 300, 60), tag = ("menu", None))
btnExit.Left = btnPlay.Left
btnExit.Top = btnPlay.Top + btnExit.Height + 3
btnExit.Command = Exit

menuTitle = Menu.Text(text = "Welcome! Sup fam?", color = Color.IndianRed, font = Font.Large)
menuTitle.Left, menuTitle.Top = window_width / 2 - menuTitle.Width / 2, 0



isRunning = True

while isRunning:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w and not Globals.dialog_open:
				Globals.camera_move = 1
				player.facing = "north"
			elif event.key == pygame.K_s and not Globals.dialog_open:
				Globals.camera_move = 2
				player.facing = "south"
			elif event.key == pygame.K_a and not Globals.dialog_open:
				Globals.camera_move = 3
				player.facing = "east"
			elif event.key == pygame.K_d and not Globals.dialog_open:
				Globals.camera_move = 4
				player.facing = "west"

			if event.key == pygame.K_RETURN:
				if Globals.dialog_open:
				#handle next page
					if Globals.active_dialog.Page < len(Globals.active_dialog.Text) - 1:
						Globals.active_dialog.Page += 1
					else:
						Globals.dialog_open = False
						Globals.active_dialog.Page = 0
						Globals.active_dialog = None


						#unpause paused npcs
						for npc in NPC.AllNPCs:
							if not npc.Timer.Active:
								npc.Timer.Start()

				else:
					#if dialoge isnt open
					for npc in NPC.AllNPCs:
						#is player in speach bounds
						#player coords are by tile
						#npcs cords are by pixel
						npc_x = npc.X / Tiles.Size
						npc_y = npc.Y / Tiles.Size
						if player_x >= npc_x - 2 and player_x <= npc_x + 2 and player_y >= npc_y - 2 and player_y <= npc_y + 2:
						#player is next to npc, however is player facing?
							if player.facing == "north" and npc_y < player_y:
								Globals.dialog_open = True
								Globals.active_dialog = npc.Dialog
								npc.Timer.Pause()
								npc.walking = False
							elif player.facing == "south" and npc_y > player_y:
								Globals.dialog_open = True
								Globals.active_dialog = npc.Dialog
								npc.Timer.Pause()
								npc.walking = False
							elif player.facing == "east" and npc_x < player_x:
								Globals.dialog_open = True
								Globals.active_dialog = npc.Dialog
								npc.Timer.Pause()
								npc.walking = False
							elif player.facing == "west" and npc_x > player_x:
								Globals.dialog_open = True
								Globals.active_dialog = npc.Dialog
								npc.Timer.Pause()
								npc.walking = False




		elif event.type == pygame.KEYUP:
			Globals.camera_move = 0

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



	#render scene
	if Globals.scene == "game":



		#logic
		if Globals.camera_move == 1:
			if not Tiles.Blocked_At((round(player_x), math.floor(player_y))):
				Globals.camera_y += 150 * Globals.deltatime #speed
		elif Globals.camera_move == 2:
			if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))):
				Globals.camera_y -= 150 * Globals.deltatime #speed
		elif Globals.camera_move == 3:
			if not Tiles.Blocked_At((math.floor(player_x), round(player_y))):
				Globals.camera_x += 150 * Globals.deltatime #speed
		elif Globals.camera_move == 4:
			if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))):
				Globals.camera_x -= 150 * Globals.deltatime #speed

		player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size
		player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size



		#Render Graphics
		window.blit(Sky, (0, 0))

		window.blit(terrain, (Globals.camera_x, Globals.camera_y))

		for npc in NPC.AllNPCs:
			npc.Render(window)

		player.render(window, (window_width / 2 - player_w / 4, window_height / 2 - player_h / 4))

		if Globals.dialog_open:
			window.blit(Dialog_Background, (window_width / 2 - Dialog_Background_Width / 2, window_height - Dialog_Background_Height - 2))

		#draw dialog text
			if Globals.active_dialog != None:
				lines = Globals.active_dialog.Text[Globals.active_dialog.Page]

				for line in lines:
					#draw text to screen
					window.blit(Font.Default.render(line, True, Color.White), (130, (window_height - Dialog_Background_Height) + 10 + (lines.index(line)) * 25))


		#for t in Tiles.Blocked:
			#pygame.draw.rect(window, Color.Red, (t[0] * Tiles.Size + Globals.camera_x, t[1] * Tiles.Size + Globals.camera_y, Tiles.Size, Tiles.Size), 2)

	#process menu
	elif Globals.scene == "menu":
		window.fill(Color.Fog)

		menuTitle.Render(window)

		for btn in Menu.Button.All:
			if btn.Tag[0] == "menu":
				btn.Render(window)



	show_fps()



	pygame.display.update()


	clock.tick()
	count_fps()

	#clock = pygame.time.clock(30)

time.sleep(1)
pygame.quit()
sys.exit()