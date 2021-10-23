from PIL.Image import Image
from datetime import datetime
import os

class NFT:
    def __init__(self, layers: list[Image], uniqueId: str = str(datetime.now().timestamp()*1000), exportPath: str = "exports", filetype: str = "png"):
        if not layers:
            raise ValueError("Cannot generate image with 0 layers")
        self.image = layers[0]
        for layer in layers[1:]:
            self.image = self.mergeImages(self.image, layer)
        self.uniqueId = uniqueId
        self.exportPath = exportPath
        self.filetype = filetype

    def mergeImages(self,background: Image, foreground: Image):
        background.paste(foreground, (0, 0), foreground)
        return background

    def save(self):
        folderPath = "{}/{}".format(self.exportPath, self.uniqueId)
        if os.path.isdir(folderPath):
            raise ValueError("NFT with same ID already exists")
        os.mkdir(folderPath)
        imagePath = "{}/image.{}".format(folderPath, self.filetype)
        self.image.save(imagePath)



