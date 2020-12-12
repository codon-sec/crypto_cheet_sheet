# input number and letters for shift
# python3
Data = "KZDVWCZVJCZBVRERIIFN"
input_data = input("Input Want to Decode Data: ")
shift_count = int(input('Input Shift Number: '))
result = ""

# A:65 Z:90 z:122
for i in range(len(input_data)):
    # 大文字・小文字で処理を変更
    # 小文字
    if (input_data[i].islower()):
        diff = ord(input_data[i]) - ord('a')
        shifted_code = diff + shift_count
        # a-z = 25
        if shifted_code >= 26:
            shifted_code = shifted_code - 26
        result += chr(shifted_code + ord('a'))
    # 大文字
    if (input_data[i].isupper()):
        diff = ord(input_data[i]) - ord('A')
        shifted_code = diff + shift_count
        # A-Z = 25
        if shifted_code >= 26:
            shifted_code = shifted_code - 26
        result += chr(shifted_code + ord('A'))
    print(ord(result[i]))
print("result is {0}".format(result))