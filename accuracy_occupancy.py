
count = 0

with open("occu_demo_data.csv") as textfile1, open("results.csv") as textfile2:
    for x, y in zip(textfile1, textfile2):
        x = x.strip()
        y = y.strip()

        #print(x)

        cellX = x.split(",")
        #print(cellX)
        cellY = y.split(",")

        if cellX[7] == cellY[1]:
            count = count + 1

print("Total number of rows considered: 1100")
print("Correctly clustered number of rows: " + str(count))
print("Incorrectly clustered number of rows: " + str(1100-count))
print("Accuracy of the clustering technique : " + str((count/1100)*100) + "%")