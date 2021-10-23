from Controllers import generateRandomCollection
from Variant import Variant

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

if __name__ == '__main__':
    count = 10  # number of unique nft to generate
    generateRandomCollection(traits, count)
    print("Done! All files generated.")