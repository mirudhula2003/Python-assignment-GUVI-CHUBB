inputstr=input()
if inputstr.strip():
    l=list(map(int,inputstr.split(' ')))
else:
    l=[]

def clean_product_id(arr):
    if not arr:
        return "empty list provided"
    arr=set(arr)
    arr=sorted(arr)
    return arr

print("Product_ID's:",l)
arr=clean_product_id(l)
print("Cleaned Product_ID's:",arr)    
