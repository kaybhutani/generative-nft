from Trait import Trait
from Variant import Variant


def getMinimumDifference(generated: 'list[list[Variant]]', arr: 'list[Variant]'):
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
                currDiff += 1
        diff = min(diff, currDiff)
    return diff


def isUniqueNFT(generated: 'list[list[Variant]]', arr: 'list[Variant]', minimumDifference: int = 1):
    return getMinimumDifference(generated, arr) >= minimumDifference


def getMetaData(traits: 'list[Trait]', variants: 'list[Variant]') -> dict:
    metadata = {}
    for i,j in zip(traits, variants):
        metadata[i.name] = j.name
    return metadata
