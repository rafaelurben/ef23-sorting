# 2022 - Rafael Urben

from analyzer import generate_graph, random_list

# Debug setting
DEBUG = False

def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

# Use bucket sort to sort a list
def bucket_sort(lst, bucketsortalgorithm=sorted):
    mi = min(lst)
    ma = max(lst)
    
    # Create bucket amount depending on the length of the list
    bucketcount = len(lst)//10+1
    buckets = list([] for i in range(bucketcount))
    bucketrange = (ma-mi)/bucketcount+0.000000001
        
    # Sort elements into buckets
    for elem in lst:
        bucketnum = (elem-mi)/bucketrange
        buckets[int(bucketnum)].append(elem)

    debug(buckets)
    
    sortedbuckets = map(bucketsortalgorithm, buckets)
    
    result = []
    for bucket in sortedbuckets:
        result += bucket
    
    return result


if __name__ == '__main__':
    # r = bucket_sort(random_list(20))
    # print(r)
    
    generate_graph(bucket_sort)
