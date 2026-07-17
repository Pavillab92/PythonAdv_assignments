from maya import cmds
import sys

MENU_NAME = 'CTRL2BLEND'
IMG_PATH  = 'D:\Documentos\My Maya Projects\customBootup\icons'

# SET custom shelf
def custom_shelf():
    delete_custom_shelf()

    shelf = cmds.shelfLayout(MENU_NAME, parent="ShelfLayout")

    cmds.shelfButton(parent=shelf,
                     label='C2B',
                     annotation='Open Control 2 Blend',
                     image1=IMG_PATH + '/c2b_shelf.png',
                     command='import ctrl2blend; ctrl2blend.load_ui()')


def delete_custom_shelf():
    if cmds.shelfLayout(MENU_NAME, exists=True):
        cmds.deleteUI(MENU_NAME)


def startup():
    custom_shelf()

cmds.evalDeferred(startup)