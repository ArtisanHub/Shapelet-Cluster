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


output = open('output.csv', 'w')


print("Output writing")

output.write(str("Cluster stats of iris dataset"))
output.write(str("\n"))

output.write(str("Total number of rows considered: 150"))
output.write(str("\n"))

output.write(str("Correctly clustered number of rows: " + str(count)))
output.write(str("\n"))

output.write(str("Incorrectly clustered number of rows: " + str(150-count)))
output.write(str("\n"))

output.write(str("Accuracy of the clustering technique : " + str((count/150)*100) + "%"))
output.write(str("\n"))