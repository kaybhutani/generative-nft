import json
from PIL.Image import Image
from datetime import datetime
import os


def mergeImages(background: Image, foreground: Image):
    background.paste(foreground, (0, 0), foreground)
    return background


class NFT:
    def __init__(self, layers: 'list[Image]', metadata: dict, uniqueId: str = str(datetime.now().timestamp()*1000), exportPath: str = "exports", filetype: str = "png", useFolder: bool = True):
        if not layers:
            raise ValueError("Cannot generate image with 0 layers")
        self.image = layers[0]
        for layer in layers[1:]:
            self.image = mergeImages(self.image, layer)
        self.uniqueId = uniqueId
        self.exportPath = exportPath
        self.filetype = filetype
        self.metadata = metadata
        self.usefolder = useFolder

    def save(self, writeMeta: bool):
        if self.usefolder:
            folderPath = "{}/{}".format(self.exportPath, self.uniqueId)
            if os.path.isdir(folderPath):
                raise ValueError("NFT with same ID already exists")
            os.mkdir(folderPath)
            imagePath = "{}/image.{}".format(folderPath, self.filetype)
            metadataPath = "{}/metadata.json".format(folderPath)
            self.image.save(imagePath)
            metajson = json.dumps(self.metadata, indent=4)
            if writeMeta:
                with open(metadataPath, "w") as outfile:
                    outfile.write(metajson)
        else:
            imagePath = "{}/{}.{}".format(self.exportPath, self.uniqueId, self.filetype)
            metadataPath = "{}/{}.json".format(self.exportPath, self.uniqueId)
            self.image.save(imagePath)
            metajson = json.dumps(self.metadata, indent=4)
            if writeMeta:
                with open(metadataPath, "w") as outfile:
                    outfile.write(metajson)




