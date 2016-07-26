from direct.showbase.ShowBase import ShowBase
from panda3d.core import *

class Main(ShowBase):
    
    def __init__(self):
        ShowBase.__init__(self)
        
        self.scene = self.loader.loadModel("models/world")
        
        
        self.scene.reparentTo(self.render)
        
        
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.3, .3, .3, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection((-5, -5, -5))
        directionalLight.setColor((1, 1, 1, 1))
        directionalLight.setSpecularColor((1, 1, 1, 1))
        self.render.setLight(self.render.attachNewNode(ambientLight))
        self.render.setLight(self.render.attachNewNode(directionalLight))
        
app = Main();
app.run();