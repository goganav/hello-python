import cocos
from cocos.director import director
from cocos.text import *

class TestLayer(cocos.layer.Layer):
    def update(self, dt):
        self.text.x=self.text.x+1
        w, h = director.get_window_size()
        if self.text.x> w:
            self.text.x=0
        self.rotation+=dt * 2
        self.text.element.text=str(dt)
    def __init__(self):
        super(TestLayer, self).__init__()
        x, y = director.get_window_size()
        self.text = RichLabel("hello", (x//2, y//2))
        self.add(self.text)
        self.schedule(self.update)

def main():
    director.init(width=1920,height=1080, fullscreen=1)
    test_layer = TestLayer()
    main_scene = cocos.scene.Scene(test_layer)
    director.show_FPS = True
    director.run(main_scene)

if __name__ == '__main__':
    main()