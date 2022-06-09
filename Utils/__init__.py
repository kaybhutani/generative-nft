from Trait import Trait
from Variant import Variant


def getMinimumDifference(generated: 'list[list[Variant]]', currentGenerated: 'list[Variant]'):
    diff = len(currentGenerated)
    variants = []
    allLayerNames = []
    for g in generated:
        temp = []
        for i in g:
            temp.append(i.name)
        allLayerNames.append(temp)
    for i in currentGenerated:
        if not i.shouldExcludeInDifference:
            # exclude layers like background, etc. to be counted in minimum difference
            variants.append(i.name)

    for i in allLayerNames:
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
