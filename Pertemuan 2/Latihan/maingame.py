from game.Image.open import *
from game.Image.change import *
from game.Image.close import *

from game.Level.start import *
from game.Level.load import *
from game.Level.over import *

from game.Sound.load import *
from game.Sound.play import *
from game.Sound.pause import *

while(True):
    print("Menu : ")
    print("1. Load sound")
    print("2. Play sound")
    print("3. Pause sound")
    print("4. Open image")
    print("5. Change image")
    print("6. Close image")
    print("7. Start level")
    print("8. Load level")
    print("9. Over level")

    pilihan = int(input("Pilih : "))

    if pilihan == 1:
        sound = input("What sound?")
        load_sound(sound)
        break

    elif pilihan == 2:
        sound = input("What sound?")
        play_sound(sound)
        break

    elif pilihan == 3:
        pause_sound()
        break

    elif pilihan == 4:
        image = input("What image?")
        open_image(image)
        break

    elif pilihan == 5:
        image = input("What image?")
        change_image(image)
        break

    elif pilihan == 6:
        close_image()
        break

    elif pilihan == 7:
        level = input("What level?")
        start_level(level)
        break

    elif pilihan == 8:
        level = input("What level?")
        load_level(level)
        break

    elif pilihan == 9:
        score = input("What score?")
        game_over(score)
        break
 
    else:
        print("Pilihan tidak ada")