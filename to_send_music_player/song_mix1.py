import playsound
import random

L = ['sad.mp3', 'sad1.mp3', 'sad2.mp3', 'sad3.mp3']
S = random.randint(0, len(L))
playsound.playsound(L[S], True)