import pygame
import keyboard
import time

# Initialize mixer
pygame.mixer.init()

def play_sound(fichier):
    pygame.mixer.music.load(f"Soundboard/{fichier}")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

print(" Soundboard [Online] :")
print(
    "Commandes disponibles :\n"
    "   [1] →   Welcome\n"
    "   [2] →   place_your_track_here\n"
    "   [-] →   Quit"

)

try:
    while True:
        if keyboard.is_pressed('1'):
            print("→→→ Welcome!")
            play_sound("Welcome.mp3")
            while keyboard.is_pressed('1'):
                pass
# Duplicate this section for each sound you have in the folder Soundboard. 

        if keyboard.is_pressed('2'):
            print("→→→ place_your_track_here")
            play_sound("place_your_track_here.mp3")
            while keyboard.is_pressed('2'):
                pass



        if keyboard.is_pressed('-'):
            print("-> Soundboard [Offline]")
            break

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\n Script Stopped.")
