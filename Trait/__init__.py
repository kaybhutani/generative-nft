from Variant import Variant
from PIL import Image
import random
import os

class Trait:

    def __int__(self, name: str, foldername:str, variants: list[Variant], collectionsize: int = 100, basedir: str = "layers"):
        """

        :param name: name of trait
        :param foldername: name of folder
        :param variants: variants under trait
        :return:
        """
        self.name = name
        self.foldername = "{}/{}".format(basedir, foldername)
        self.variants = self.rarityBasedVariants(variants)
        self.collectionsize = collectionsize
        self.iterator = 0
        self.basedir = basedir

        if not os.path.isdir(foldername):
            raise  ValueError(foldername, "doesn't exists")

    def rarityBasedVariants(self, variants: list[Variant]) -> list[Variant]:
        generated: list[Variant] = []
        for i in variants:
            generated.extend(i.rarity*self.collectionsize*[i])
        return generated

    def getNextVariant(self) -> Image:
        nextVariant = self.variants[self.iterator]
        imagePath = "{}/{}".format(self.foldername, nextVariant.filename)
        if not os.path.isfile(imagePath):
            raise ValueError(imagePath, "doesn't exists")
        image = Image.open(imagePath)
        self.iterator += 1
        return image

    def getRandom(self) -> Image:
        randomVariant = random.choice(self.variants)
        imagePath = "{}/{}".format(self.foldername, randomVariant.filename)
        if not os.path.isfile(imagePath):
            raise ValueError(imagePath, "doesn't exists")
        image = Image.open(imagePath)
        return image





