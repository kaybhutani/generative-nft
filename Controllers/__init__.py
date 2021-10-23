import os

from NFT import NFT
from Trait import Trait
from Utils import isUniqueNFT, getMetaData


def generateRandomCollection(traits: dict, count: int, exportDir: str = "exports", minimumDifference: int = 1):

    if not os.path.isdir(exportDir):
        os.mkdir(exportDir)
    generatedNft = []
    map = []
    i = 0
    while i < count:
        variantsArray = []
        traitsArray = []
        for t in traits:
            trait = Trait(t, t, traits[t])
            traitsArray.append(trait)
            variantsArray.append(trait.getRandomVariant())

        if isUniqueNFT(map, variantsArray, minimumDifference):
            print("Found unique traits")
            map.append(variantsArray)
            layers = []
            for j, k in zip(variantsArray, traitsArray):
                layers.append(k.getImage(j))
            metadata = getMetaData(traitsArray, variantsArray)
            nft = NFT(layers, metadata, i)
            generatedNft.append(nft)
            i += 1
        else:
            print("Found duplicate nft")
            continue
    print("Got all of the unique NFT! Generating images now.")
    for nft in generatedNft:
        nft.save()


