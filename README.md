# RokuRogue
## Overview
Did you know that many Roku TVs are exposing port 8600 to the entire internet? Well, Brandon Dorsey [discovered](https://medium.com/@brannondorsey/attacking-private-networks-from-the-internet-with-dns-rebinding-ea7098a2d325) that you can use DNS rebind attacks to turn smart device pwning into an absolute nightmare. In addition, he worked on exposing all of the cool things that can be done through port 8600 on Roku TVs.

That's when it occured to me - how can I take this seemingly annoying issue, and make it more of a nightmare? I read the documentation and learned that you can actually install applications. Unfortunately, to do this, at least on ONN Roku TVs (which was my test case), you need to have a pin. Fortunately, getting a pin is as easy as a brute force! There's only a 4-digit pin in our way, with 10,000 possible combinations seperating us from the prize.

## Usage
`python3 roku-rogue.py`

Also download Web Video Caster on Android or iOS if you want to mirror media.

Options:
1. Install Web Cast -- Installs web cast, which can be used for pwning TVs with your own custom video content or MP3s. First, the script turns the volume down to 0 to ensure that the victim device will not disturb the owner with the sound of attempts or pin entry. Then, it runs through all of the combinations until it successfully brutes the pin to install the application. It then re-adjusts the volume to a reasonable level.
2. Install Another App -- Same as option 1, except you can enter the app ID of the app you want to install. Please see "Custom Apps" for details.
3. Launch Web Cast -- Starts the Web Cast application, which will give you the ability to stream your media via the application.
4. Launch Web Cast (PWN Mode: Be warned!) -- Turns the volume up to max, and then launches Web Cast.
5. Launch Another App -- Starts your custom application by ID.
6. Study Mode -- Sends a poweroff command every second to the TV until you kill the script.
7. Exit

## Custom Apps
Maybe you'd rather install a custom app. If you have a Roku TV, install the app, and then navigate to http://ip:8060/query/apps to get the App ID, then you can pass the application ID via the options to install that app instead of webcast.

Here is an example of what it looks like, where 2595 is the app id:
`<app id="2595" type="appl" version="4.8.1110">Crunchyroll</app>`

# Proof of Concept
## App Install Bruteforce

https://user-images.githubusercontent.com/39013067/227747518-5ee5e888-1752-4616-bbaf-691d68ae7f8a.mp4

## Playing a Video Remotely via Installed Webcast + Mobile App

https://user-images.githubusercontent.com/39013067/227747726-6f8dfd6c-92f5-45ee-a3cc-805e2578e2dc.mp4
