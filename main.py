from NFT import NFT
from Trait import Trait
from Variant import Variant
import os

traits = {
    'background': [Variant("cyan", "cyan.png", 0.16), Variant("green", "green.png", 0.16), Variant("pink", "pink.png", 0.16), Variant("purple", "purple.png", 0.16), Variant("red", "red.png", 0.16), Variant("yellow", "yellow.png", 0.16)],
    'body': [Variant("body", "body.png", 1)],
    'arm': [Variant("furry", "furry.png", 0.25), Variant("skeleton", "skeleton.png", 0.25), Variant("human", "human.png", 0.25), Variant("tenticle", "tenticle.png", 0.25)],
    'eyes': [Variant("green", "green.png", 0.25), Variant("purple", "purple.png", 0.25), Variant("red", "red.png", 0.25), Variant("shades", "shades.png", 0.25)],
    'hair': [Variant("long-grey", "long-grey.png", 0.14),Variant("long-purple", "long-purple.png", 0.10), Variant("long-yellow", "long-yellow.png", 0.14), Variant("short-blue", "short-blue.png", 0.10), Variant("short-green", "short-green.png", 0.10), Variant("short-pink", "short-pink.png", 0.22), Variant("short-yellow", "short-yellow.png", 0.18)],
    'top': [Variant("cyan-crop-top", "cyan-crop-top.png", 0.16), Variant("dark-blue-tshirt", "dark-blue-tshirt.png", 0.16), Variant("green-crop-top", "green-crop-top.png", 0.16), Variant("orange-tshirt", "orange-tshirt.png", 0.16), Variant("pink-tshirt", "pink-tshirt.png", 0.16), Variant("red-crop-top", "red-crop-top.png", 0.16)],
    'hat': [Variant("antlerns", "antlerns.png", 0.25), Variant("horns", "horns.png", 0.25), Variant("wizard", "wizard.png", 0.5)],
    'mouth': [Variant("evil", "evil.png", 0.15), Variant("smile", "smile.png", 0.35), Variant("grin", "grin.png", 0.20), Variant("surprised", "surprised.png", 0.30)]
}

def checkDifference(generated: list[list[Variant]], arr: list[Variant]):
    diff = len(arr)
    variants = []
    map = []
    for g in generated:
        temp = []
        for i in g:
            temp.append(i.name)
        map.append(temp)
    for i in arr:
        variants.append(i.name)

    for i in map:
        currDiff = 0
        for j in variants:
            if j not in i:
                currDiff+=1
        diff = min(diff, currDiff)
    return  diff

def generate():
    exportDir = "exports"

    if not os.path.isdir(exportDir):
        os.mkdir(exportDir)
    generatedNft = []
    map = []
    count = 10
    i = 0
    while i < count:
        variantsArray = []
        traitsArray = []
        for t in traits:
            trait = Trait(t, t, traits[t])
            traitsArray.append(trait)
            variantsArray.append(trait.getRandomVariant())

        if checkDifference(map, variantsArray) > 1:
            print("Found unique traits")
            map.append(variantsArray)
            layers = []
            for j, k in zip(variantsArray, traitsArray):
                layers.append(k.getImage(j))
            nft = NFT(layers, i)
            generatedNft.append(nft)
            i += 1
        else:
            print("Found duplicate nft")
            continue
    print("Got all of the unique NFT! Generating images now.")
    for nft in generatedNft:
        nft.save()






if __name__ == '__main__':
    generate()
    print("Done!")