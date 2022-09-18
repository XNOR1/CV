import time

# step 1
beatles = []

# step 2
beatles.append("John Lennon") 
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("The Beatles are", beatles, "\n")
time.sleep(3)
print("The Beatles are lonely...")



# step 3
members = ["Stu Ratcliff", "Pete Best"]
for i in range(len(members)):
    print("Add", members[i], "to the band!: ", end='')
    beatles.append(input())
    print()
print("The Beatles are now:", beatles, "\n")
time.sleep(5)


# step 4
print("Oh, no!", beatles[3], "and", beatles[4], "got kicked out of the band!")
time.sleep(5)
del beatles[-1]
del beatles[-1]
print("We're back down to these guys: ", beatles, "\n")

time.sleep(5)

print("But, who is this Starr shining on the horizon? It can't Be! its...")
time.sleep(5)
print("Ringo Starr!!!")
time.sleep(4)

# step 5
beatles.insert(0,"Ringo Starr")
print()


# testing list legth
print("The Fab", len(beatles), beatles)