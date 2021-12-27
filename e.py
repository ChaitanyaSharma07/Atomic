arr = [1, 2, 3, 4, 5]

for i in enumerate(arr):
    print(i)

    for j in i:
        print("index = " + str(i[0]))
        print("value = " + str(i[1]))
        print("--------------------------")