import pygame

pygame.init()

class Tiles:

	Size = 60

	Blocked = []

	Blocked_Types = ["3", "3A", "3B", "3C", "3D", "3E", "3F", "3G"]

	def Blocked_At(pos):
		if list(pos) in Tiles.Blocked:
			return True
		else:
			return False

	def Load_Texture(file, Size):
		bitmap = pygame.image.load(file)
		bitmap = pygame.transform.scale(bitmap, (Size, Size))
		surface = pygame.Surface((Size, Size), pygame.HWSURFACE|pygame.SRCALPHA)
		surface.blit(bitmap, (0, 0))
		return surface

	Grass = Load_Texture("graphics/grass.png", Size)
	Stone = Load_Texture("graphics/stone.png", Size)
	Water = Load_Texture("graphics/water.png", Size)
	Rose_Pink = Load_Texture("graphics/rose_pink.png", Size)
	Rose_Red = Load_Texture("graphics/rose_red.png", Size)
	WaterN = Load_Texture("graphics/waterN.png", Size)
	WaterNE = Load_Texture("graphics/waterNE.png", Size)
	WaterNEW = Load_Texture("graphics/waterNEW.png", Size)
	WaterE = Load_Texture("graphics/waterE.png", Size)
	WaterS = Load_Texture("graphics/waterS.png", Size)
	WaterSE = Load_Texture("graphics/waterSE.png", Size)
	WaterSEN = Load_Texture("graphics/waterSEN.png", Size)


	Texture_Tags = {"1": Grass, "2": Stone, "3": Water, "3A": WaterN, "3B": WaterNE, "3C": WaterNEW, "3D": WaterE, "3E": WaterS, "3F": WaterSE, "3G": WaterSEN, "4": Rose_Pink, "5": Rose_Red}







