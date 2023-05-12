from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture  = load_texture('assets/dirt_block.png')
diamond_texture = load_texture('assets/diamond_block.png')
terracotta_texture = load_texture('assets/terracotta_block.png')
purpur_texture = load_texture('assets/purpur_block.png')
prismarine_texture = load_texture('assets/prismarine_block.png')
bedrock_texture = load_texture('assets/bedrock_block.png')

sky_texture   = load_texture('assets/skybox.png')
arm_texture   = load_texture('assets/arm_texture.png')
punch_sound   = Audio('assets/punch_sound',loop = False, autoplay = False)
background_sound = Audio('assets/bg_music',loop=True, autoplay=True)
block_pick = 1

height=2

window.fps_counter.enabled = True
window.exit_button.visible = False

def update():
    global block_pick
    global height
    
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()       
   
    if held_keys['left shift'] or held_keys['right shift']:
        player.speed = 8
    else:
        player.speed = 5
    
    if held_keys['left control'] or held_keys['right control']:
        player.speed = 3
        camera.y=-0.5
    else:
        player.speed = 5
        camera.y=0
        
    if held_keys['f']:
        camera.z=-5
    else:
        camera.z=0
    
    
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4 
    if held_keys['5']: block_pick = 5
    if held_keys['6']: block_pick = 6
    if held_keys['7']: block_pick = 7
    if held_keys['8']: block_pick = 8
    
 
    

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            scale = 0.5)

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
                if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = diamond_texture)
                if block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, texture = purpur_texture)
                if block_pick == 7: voxel = Voxel(position = self.position + mouse.normal, texture = prismarine_texture)
                if block_pick == 8: voxel = Voxel(position = self.position + mouse.normal, texture = terracotta_texture)

            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)
class Bedoxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = bedrock_texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            scale = 0.5)
        
class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)


        
#bedrock layer
for z in range(40):
	for x in range(40):
		bedrock= Bedoxel(position = (x,0,z))
        
#grass layer        
for z in range(40):
	for x in range(40):
		voxel = Voxel(position = (x,1,z))

############
#deactivate this section to preserve ram       
for l in range(80):    
        voxel=Voxel(position=(random.randint(5,20),random.randint(2, 3),random.randint(5,20)) , texture=stone_texture)
##########


player = FirstPersonController(model='cube',height=height)



sky = Sky()
hand = Hand()

app.run()