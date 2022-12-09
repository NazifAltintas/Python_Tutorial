
for i in range(3, 51):
    count = 1
    for j in range(2, i ):
        if i % j == 0:
            count = count + 1
    if count == 1:
        print(i , "asal sayidir")
    else:
        print(i ,"asal sayi degildir")
