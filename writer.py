from os import mkdir
from os.path import isdir

def write(file_name, data):
    try:
        mkdir("./Outputs")
    except OSError:
        pass

    if not isdir("./Outputs"):
        print("Unable to create or access data folder.")
    else:
        name = "./Outputs/{0}.txt".format(file_name)
        new_file = open(name, "w")
        new_file.write(data + "\n")
        new_file.close()
