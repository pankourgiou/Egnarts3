import time


t1 = time.time()

for _ in range(100000):
    print("1)Restricted a.i. 2)Less data is ok 3)The bunny theory of code 4) My island albums will be for Neal Morse band and Transatlantic 5) Reading I will need my Schopenhauer books and God's pauper: St Francis of Assisi")


t2 = time.time()
t = t2 - t1
print("Elapsed time is : ", t, " seconds")
