from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

Sky() 

player = FirstPersonController()

grass_block = load_texture('assets/grass_block.jpg')

jump = Audio(
    'assets\jump.mp3',
    autoplay= False,
    loop= False
)

walk = Audio(
    'assets\walk.mp3',
    autoplay=False,
    loop=False
)

def update():
    walking = held_keys['w'] or \
        held_keys['a'] or \
        held_keys['s'] or \
        held_keys['d']
    if walking and player.grounded:
        if not walk.playing:
            walk.play()
    else:
        if walk.playing:
            walk.stop()  

class Cubes(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = 'grass_block',
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.lime,
            scale=0.5
        )

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                cubes = Cubes(position= self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)
            if key == 'q':
                quit() #Buggy (not sure why??)
            if key == 'space':
                if not jump.playing:
                    jump.play()

      
for z in range(20):
	for x in range(25):
		platform = Cubes(position = (x,0,z))

window.title = 'My Minecraft Clone (:' 
window.fullscreen = False

Text.size = 0.025
Text.default_resolution = 1080 * Text.size
info = Text(text="q to quit")
info.x = -0.7
info.y = 0.4
info.background = True


app.run() 
