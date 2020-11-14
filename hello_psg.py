# img_viewer.py


import PySimpleGUI as sg

import os.path


pngFileName = "\\Bierbot\\designs\\test.png"
# For now will only show the name of the file that was chosen

image_viewer_column = [

    [sg.Image(filename=os.getcwd() + pngFileName, key='key1', size=(1920, 1080))]

]



layout = [

    [
        sg.Column(image_viewer_column),

    ]

]


window = sg.Window("Image Viewer", layout,no_titlebar=False,location=(0,0),  size = (1920,1080),keep_on_top=False)


# Run the Event Loop

while True:

    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:

        break

    # Folder name was filled in, make a list of files in the folder


window.close()
