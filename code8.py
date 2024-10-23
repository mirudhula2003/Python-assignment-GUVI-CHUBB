l=list(map(int,input().split()))
goodrating=filter(lambda rating:rating>=5,l)
goodrating=map(lambda ele:ele**2,goodrating)
print(*goodrating)
