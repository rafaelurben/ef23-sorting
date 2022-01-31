# 2022 - Rafael Urben

from utils import SortingAlgorithm

def bucketsort_func(data, bucketsortalgorithm=sorted):
    mi = min(data)
    ma = max(data)

    # Create bucket amount depending on the length of the list
    bucketcount = len(data)//10+1
    buckets = list([] for i in range(bucketcount))
    bucketrange = (ma-mi)/bucketcount+0.000000001

    # Sort elements into buckets
    for elem in data:
        bucketnum = (elem-mi)/bucketrange
        buckets[int(bucketnum)].append(elem)

    sortedbuckets = map(bucketsortalgorithm, buckets)

    result = []
    for bucket in sortedbuckets:
        result += bucket

    return result

# Testing

if __name__ == '__main__':
    bucketsort = SortingAlgorithm(bucketsort_func)
    
    r = bucketsort.test(20)
    print(r)

    bucketsort.analyze()
