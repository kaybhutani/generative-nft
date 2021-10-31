import json
import os

from NFT import NFT
from Trait import Trait
from Utils import isUniqueNFT, getMetaData


def generateRandomCollection(traits: dict, count: int, exportDir: str = "exports", minimumDifference: int = 1, useFolder: bool = True, writeMetaForEachFile = False):

    if not os.path.isdir(exportDir):
        os.mkdir(exportDir)
    generatedNft = [] # nft objects
    combinedMetaData = {} # nft id -> metadata
    map = [] # array of all variants
    i = 0
    while i < count:
        variantsArray = []
        traitsArray = []
        layersToExclude = set()
        for t in traits:
            trait = Trait(t, t, traits[t])
            traitsArray.append(trait)
            randomVariant = trait.getRandomVariant()
            while layersToExclude.intersection(set(randomVariant.layersToExclude)):
                randomVariant = trait.getRandomVariant()
            layersToExclude.update(randomVariant.layersToExclude)
            variantsArray.append(randomVariant)

        if isUniqueNFT(map, variantsArray, minimumDifference):
            print("Found unique traits")
            map.append(variantsArray)
            layers = []
            for j, k in zip(variantsArray, traitsArray):
                layers.append(k.getImage(j))
            metadata = getMetaData(traitsArray, variantsArray)
            combinedMetaData[i] = metadata
            nft = NFT(layers, metadata, i, useFolder=useFolder)
            generatedNft.append(nft)
            i += 1
        else:
            print("Found duplicate nft")
            continue
    print("Got all of the unique NFT! Generating images now.")
    for nft in generatedNft:
        nft.save(writeMetaForEachFile)
    metajson = json.dumps(combinedMetaData, indent=4)
    metaPath = "{}/metadata.json".format(exportDir)
    with open(metaPath, "w") as outfile:
        outfile.write(metajson)



