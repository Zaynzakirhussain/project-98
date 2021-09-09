def swapFileData():
    intro = "The file swapper... Follow instructions to SWAP a file"
    print(intro)

    file1 = input("Enter the first file to be swapped: ")
    file2 = input("Enter the second file to be swapped with first file: ")

    with open(file1,'r') as a:
        data_a = a.read()

    with open(file2,'r') as b:
        data_b = b.read()

    with open(file1,'w') as a:
        a.write(data_b)

    with open(file2,'w') as b:
        b.write(data_a)

    swapped = "File swapped!!!"
    print(swapped)

swapFileData()