History_File = "history.txt"

def show_history():
    file = open(History_File, "r")
    lines = file.readline()
    if len(lines) == 0:
        print("No history found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()            

def clear_history():
   file = open(History_File, "w")
   file.close()
   print('History created')

def save_to_history(equation, result):
    file = open(History_File, "a")
    file.write(equation + "=" + str(result) + "\n")
    file.close()   
    