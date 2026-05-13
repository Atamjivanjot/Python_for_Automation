with open(r"C:\Users\delln\OneDrive\Desktop\projects\python-automation\logs.txt", "r") as file:
    counter = 0
    search_word = "Error"
    """
    for line in file:
        if search_word in line:
            print(line)
            counter+=1
    print(counter)
    """
    for line_no, content in enumerate(file, start=1):
        if search_word in content:
            print(line_no)
            counter+=1
    print(f"the counter value is {counter}")

