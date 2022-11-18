import time
import os 
os.system("cls")


frames = [" "," ",'(0','(|','[X','[I']

nlines = 3
# scroll up to make room for output
print(f"\033[{nlines}S", end="")

# move cursor back up
print(f"\033[{nlines}A", end="")

# save current cursor position
print("\033[s", end="")

for t in range(6):
    # restore saved cursor position
    print("\033[u", end="")
    print(frames[0 + t])
    print(frames[0 + t])
    t += 1
    time.sleep(.7)
