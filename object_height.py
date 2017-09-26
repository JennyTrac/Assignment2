# Created by: Jenny Trac
# Created on: Sept 25 2017
# Assignment 2
# This program calculates an object's height after being
# dropped from 100 m

import ui

def calculate_touch_up_inside(sender):
    # button to calculate height
	
    # input
    time = int(view['time_textfield'].text)
    gravity = 9.81
	
    # process
    if time < 0:
        view['height_label'].text = "Non-real result"
    
    if time >= 0:
        height = 100 - gravity * (time)**2
	
        # output
        if height >= 0:
            view['height_label'].text = "Object's height above the ground = " + str(height) + " m"
        else:
            view['height_label'].text = "Object has hit the ground"

view = ui.load_view()
view.present('sheet')
