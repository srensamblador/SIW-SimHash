from bag_of_words import BagOfWords
from heapq import heappush, heappop


def simhash(item, restrictiveness, ngrams):
    set = BagOfWords(item)
    queue = []
    for x in set:
        heappush(queue, (hash(x[0]), x[0]))
    simhash = 0
    for x in range (0, restrictiveness):
        simhash ^= heappop(queue)[0]
    return simhash
