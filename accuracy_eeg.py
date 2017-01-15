count = 0

with open("eeg_demo.csv") as textfile1, open("results.csv") as textfile2:
    for x, y in zip(textfile1, textfile2):
        x = x.strip()
        y = y.strip()

        cellX = x.split(",")
        cellY = y.split(",")

        if cellX[14] == cellY[1]:
            count = count + 1

print("Total number of rows considered: 1000")
print("Correctly clustered number of rows: " + str(count))
print("Incorrectly clustered number of rows: " + str(1000-count))
print("Accuracy of the clustering technique : " + str((count/1000)*100) + "%")