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

output = open('output.csv', 'w')

print("Output writing")

output.write(str("Cluster stats of Wine dataset"))
output.write(str("\n"))

output.write(str("Total number of rows considered: 178"))
output.write(str("\n"))

output.write(str("Correctly clustered number of rows: " + str(count)))
output.write(str("\n"))

output.write(str("Incorrectly clustered number of rows: " + str(178-count)))
output.write(str("\n"))

output.write(str("Accuracy of the clustering technique : " + str((count/178)*100) + "%"))
output.write(str("\n"))
