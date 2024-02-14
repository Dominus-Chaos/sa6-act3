stringlist=["Bob", "billy", "please", "stop"]
stringlist2= ["i", "Bob", "stop", "UwU"]

intersection = list(filter(lambda x: x in stringlist, stringlist2))
print(intersection)