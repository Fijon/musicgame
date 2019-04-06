import Piano
import random

player = Piano.Player()
for idx in range(0, 87):
    idx = random.randint(0,87)
    player.play(idx)
    print('end')
