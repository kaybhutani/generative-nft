from Variant import Variant
from PIL import Image
import random
import os


class Trait:

    def __init__(self, name: str, foldername: str, variants: 'list[Variant]', collectionsize: int = 100, basedir: str = "layers"):
        """
        :param name: name of trait
        :param foldername: name of folder
        :param variants: variants under trait
        :return:
        """
        self.name = name
        self.foldername = "{}/{}".format(basedir, foldername)
        self.collectionsize = collectionsize
        self.variants = self.rarityBasedVariants(variants)
        self.iterator = 0
        self.basedir = basedir

        if not os.path.isdir(self.foldername):
            raise  ValueError(self.foldername, "doesn't exists")

    def rarityBasedVariants(self, variants: 'list[Variant]') -> 'list[Variant]':
        generated: list[Variant] = []
        for i in variants:
            generated.extend((int(i.rarity*self.collectionsize))*[i])
        return generated

    def getNextVariant(self) -> Image:
        nextVariant = self.variants[self.iterator]
        imagePath = "{}/{}".format(self.foldername, nextVariant.filename)
        if not os.path.isfile(imagePath):
            raise ValueError(imagePath, "doesn't exists")
        image = Image.open(imagePath)
        self.iterator += 1
        return image

    def getRandomVariant(self) -> Variant:
        return random.choice(self.variants)

    def getRandomImage(self, variant: Variant) -> Image:
        randomVariant = random.choice(self.variants) if not variant else variant
        imagePath = "{}/{}".format(self.foldername, randomVariant.filename)
        if not os.path.isfile(imagePath):
            raise ValueError(imagePath, "doesn't exists")
        image = Image.open(imagePath)
        return image

    def getImage(self, variant: Variant) -> Image:
        imagePath = "{}/{}".format(self.foldername, variant.filename)
        if not os.path.isfile(imagePath):
            raise ValueError(imagePath, "doesn't exists")
        image = Image.open(imagePath)
        return image





