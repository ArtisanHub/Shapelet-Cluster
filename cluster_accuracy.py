

original_dataset_with_clusters = ""  #Provide the original dataset file name with clusters
input_file_with_clusters = ""  #Provide the input filen ame which has the cluster results

output_file_with_stats = ""  #Provide the filename where the accuracy stats needs to be written

def cluster_accuracy(input_file_with_clusters,output_file_with_stats):

    count = 0

    with open(original_dataset_with_clusters) as textfile1, open(input_file_with_clusters) as textfile2:
        x = "" #Postion of cluster value column in the textfile1
        y = ""  # Postion of cluster value column in the textfile2
        for x, y in zip(textfile1, textfile2):
            x = x.strip()
            y = y.strip()

            cellX = x.split(",")
            cellY = y.split(",")

            if cellX[x] == cellY[y]:
                count = count + 1

    output = open(output_file_with_stats, 'w')


    print("Output writing")

    output.write(str("Cluster stats of Occupancy Detection dataset"))
    output.write(str("\n"))

    output.write(str("Total number of rows considered: 1100"))
    output.write(str("\n"))

    output.write(str("Correctly clustered number of rows: " + str(count)))
    output.write(str("\n"))

    output.write(str("Incorrectly clustered number of rows: " + str(1100-count)))
    output.write(str("\n"))

    output.write(str("Accuracy of the clustering technique : " + str((count/1100)*100) + "%"))
    output.write(str("\n"))

    print("Output written")