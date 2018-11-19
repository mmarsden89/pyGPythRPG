import pygame

pygame.init()

class Tiles:

	Size = 60

	Blocked = []

	Blocked_Types = ["3", "3A", "3B", "3C", "3D", "3E", "3F", "3G", "3H", "3I", "3J", "9", "9A", "9B", "9C", "9D", "9E", "10", "10A", "10B", "10C", "10E", "10F", "10G", "10H"]

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
	WaterW = Load_Texture("graphics/waterW.png", Size)
	Water8 = Load_Texture("graphics/water8.png", Size)
	Water9 = Load_Texture("graphics/water9.png", Size)
	StoneN = Load_Texture("graphics/stoneN.png", Size)
	StoneNW = Load_Texture("graphics/stoneNW.png", Size)
	StoneNE = Load_Texture("graphics/StoneNE.png", Size)
	StoneS = Load_Texture("graphics/StoneS.png", Size)
	StoneW = Load_Texture("graphics/stoneW.png", Size)
	StoneE = Load_Texture("graphics/stoneE.png", Size)
	StoneSE = Load_Texture("graphics/StoneSE.png", Size)
	StoneSW = Load_Texture("graphics/StoneSW.png", Size)
	House = Load_Texture("graphics/house1.png", 360)
	House2 = Load_Texture("graphics/house2.png", 360)
	House3 = Load_Texture("graphics/house3.png", 360)
	House4 = Load_Texture("graphics/house4.png", 480)
	House5 = Load_Texture("graphics/house5L.png", 480)
	House6 = Load_Texture("graphics/house3s.png", 360)
	Tree = Load_Texture("graphics/tree.png", 240)
	Wood = Load_Texture("graphics/wood.png", Size)
	Wall = Load_Texture("graphics/wall.png", Size)
	WallUpper = Load_Texture("graphics/wallupper.png", Size)
	WallLeft = Load_Texture("graphics/wallleft.png", Size)
	WallRight = Load_Texture("graphics/wallright.png", Size)
	WallUp = Load_Texture("graphics/wallup.png", Size)
	WallDown = Load_Texture("graphics/walldown.png", Size)
	Bar = Load_Texture("graphics/bar.png", Size)
	BarLeft = Load_Texture("graphics/barleft.png", Size)
	BarCLD = Load_Texture("graphics/barcld.png", Size)
	BarUp = Load_Texture("graphics/barup.png", Size)
	Window = Load_Texture("graphics/window.png", Size)
	WindowUpper = Load_Texture("graphics/windowupper.png", Size)
	Rug = Load_Texture("graphics/rug.png", Size)
	Isle = Load_Texture("graphics/aisle.png", Size)
	Isle2 = Load_Texture("graphics/aisle2.png", Size)
	Lily = Load_Texture("graphics/lily.png", Size)




	Texture_Tags = {"1": Grass, "2": Stone, "2A": StoneN, "2B": StoneNW, "2C": StoneW, "2D": StoneE, "2E": StoneNE, "2F": StoneS, "2G": StoneSE, "2H": StoneSW, "3": Water, "3A": WaterN, "3B": WaterNE, "3C": WaterNEW, "3D": WaterE, "3E": WaterS, "3F": WaterSE, "3G": WaterSEN, "3H": WaterW, "3I": Water8, "3J": Water9, "3K": Lily, "4": Rose_Pink, "5": Rose_Red, "6": House, "6A": House2, "6B": House3, "6C": House4, "6D": House5, "6E": House6, "7": Tree, "8": Wood, "9": Wall, "9A": WallUpper, "9B": WallLeft, "9C": WallRight, "9D": WallUp, "9E": WallDown, "10": Bar, "10A": BarLeft, "10B": Window, "10C": WindowUpper, "10D": Rug, "10E": Isle, "10F": Isle2, "10G": BarUp, "10H": BarCLD,}




