import rotatescreen,win32api
import time,autopy,random
def main():
    print("Wait, dont close the window.....")
    screen = rotatescreen.get_primary_display()
    running = True
    screen_rotate_value = 0
    height = win32api.GetSystemMetrics(1)
    width = win32api.GetSystemMetrics(0)
    x = random.randint(5,width-3)
    y = random.randint(5,height-3)
    print("Akhil Rocks lol")
    while running:
        screen.rotate_to(screen_rotate_value)
        screen_rotate_value += 90
        if screen_rotate_value == 360:
            screen_rotate_value = 0
        autopy.mouse.smooth_move(x,y)
        x = random.randint(10,1000)
        y = random.randint(10,1000)
        time.sleep(1)
if __name__ == "__main__":
    main()