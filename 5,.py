#5. Find the First Non-Repeated Characterinput_str = "teeteracdacd"
input_str = "teeteracdacdrx"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break