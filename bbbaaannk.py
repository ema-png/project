import os

directory = "People"
count = 0
for i in os.listdir(directory):
    with open(os.path.join(directory, i)) as f:
        print(f.read())
        count += 1
        print(count)
        
def findcurrent(anum):
        directory = "People"
        for i in os.listdir(directory):
            with open(os.path.join(directory, i)) as f:
                lines=f.readlines()
                line3 = lines[2]
                print(line3)
        