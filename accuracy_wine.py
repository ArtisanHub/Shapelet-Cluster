count = 0

with open("wine_data.csv") as textfile1, open("results.csv") as textfile2:
    for x, y in zip(textfile1, textfile2):
        x = x.strip()
        y = y.strip()

        cellX = x.split(",")
        cellY = y.split(",")

        if int(cellX[0]) == int(cellY[1]):
            count = count + 1

        else:
            continue

print("Total number of rows considered: 178")
print("Correctly clustered number of rows: " + str(count))
print("Incorrectly clustered number of rows: " + str(178-count))
print("Accuracy of the clustering technique : " + str((count/178)*100) + "%")