import os

main = """
    +======================+
    |      USB BOOTER      |
    +======================+

"""
print(main)
iso_path = str(input(" Enter the iso path: "))


def select_option():
    out = os.popen('sudo df -h').read().split('\n')
    disp = [x for x in out if '/dev/' in x]
    x = 1
    for i in disp:
        print(f" Option {x} {i}")
        x += 1   
    opt = int(input(" Number the option: "))
    path = disp[opt-1].split()[0]
    return path 

def format_usb():
    global path 
    path = select_option()
    os.system(f'sudo umount {path}')
    os.system(f'sudo mkfs.vfat -F 32 -n "USB_ONFUNC" -I {path}')
    print(" USB Formated!")

def booting():
    print(" Booting the USB. This may take a while.")
    os.system(f'sudo dd bs=4M if={iso_path} of={path} conv=fdatasync')
    print(" USB Booted! ")


if __name__ == "__main__":
    format_usb()
    booting()