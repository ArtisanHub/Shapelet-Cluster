import math

count1 = 1
count2 = 1
distance = 0

clusterdRowID = []

f = open('D:/FYP-Developments/Shapelet-Cluster/occu_demo_data.csv', 'rU' ) #open train data


#preping the analysis file with the respective window data
for line in f:
    cells = line.split(",")
    print("line number:"  + str(count1) + " ########### " + cells[7])

    k = open('D:/FYP-Developments/Shapelet-Cluster/occu_demo_data.csv', 'rU')  # open train data

    for tempLine in k:
        tempCells = tempLine.split(",")
        distance = pow((float(cells[2]) - float(tempCells[2])), 2) + pow((float(cells[3]) - float(tempCells[3])), 2) + pow((float(cells[4]) - float(tempCells[4])), 2) + pow((float(cells[5]) - float(tempCells[5])), 2) + pow((float(cells[6]) - float(tempCells[6])), 2)
        print(str(distance) + " $$$$$$$$ " + str(tempCells[7]))

    k.close()

    count1 = count1 + 1

f.close()