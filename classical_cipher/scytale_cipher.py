# implement scytale cipher

Data = "AAMSMTFSCAIYTTOCGSEOMAMCRRELBE"
input_data = input("Input Want to Decode Data: ")
pass_count = int(input('Input skip Number: '))

# print(len(Data)/pass_count)
for i in range(int(len(Data)/pass_count)):
    print(Data[i::pass_count])