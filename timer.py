import time
import winsound

tr = int(input("how long would you like to set your timer for "))
# tr = tr*60

while tr > 0:
    print(tr)
    time.sleep(1)
    tr = tr - 1

print(tr)
winsound.Beep(500, 3000)
print("The timer has finished")
