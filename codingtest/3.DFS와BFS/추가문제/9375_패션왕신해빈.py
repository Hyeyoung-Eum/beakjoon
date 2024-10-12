n=int(input())
for _ in range(n):
    m=int(input())
    #옷장
    wardrobe = {}
    for _ in range(m):
        name, cloth_type = input().split()
        if cloth_type not in wardrobe:
            wardrobe[cloth_type]=0
        wardrobe[cloth_type]+=1
    result = 1
    for value in wardrobe.values():
        result *= (value + 1)
    print(result-1)