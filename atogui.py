# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 05:07:28 2022

@author: Jatin ChaudharyYou Are a Bhaalu

"""

import random
import pyautogui as pg
import time
animal=('Dog','Suar','Gadha','ullu','Bhaalu','Shaand','Gover','Besharam','Londiyabaaz')
time.sleep(10)
for i in range(100):
    a=random.choice(animal)
    pg.write("You Are a " + a)
    pg.press('enter')



