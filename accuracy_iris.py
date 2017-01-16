count = 0

with open("iris_data.csv") as textfile1, open("results.csv") as textfile2:
    for x, y in zip(textfile1, textfile2):
        x = x.strip()
        y = y.strip()

        cellX = x.split(",")
        cellY = y.split(",")

        if cellX[4] == "Iris-setosa" and int(cellY[1]) == 1:
            count = count + 1

        elif cellX[4] == "Iris-versicolor" and int(cellY[1]) == 2:
            count = count + 1

        elif cellX[4] == "Iris-virginica" and int(cellY[1]) == 3:
            count = count + 1

        else:
            continue

print("Total number of rows considered: 150")
print("Correctly clustered number of rows: " + str(count))
print("Incorrectly clustered number of rows: " + str(150-count))
print("Accuracy of the clustering technique : " + str((count/150)*100) + "%")