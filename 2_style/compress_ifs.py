"""
content = assignment
course  = Python Advanced
 
date    = 14.11.2025
email   = contact@alexanderrichtertd.com
"""

from maya import cmds as mc


# COMMENT --------------------------------------------------
# Not optimal
def set_color(ctrlList=None, color=None):

    for ctrlName in ctrlList:
        try:
            mc.setAttr(ctrlName + 'Shape.overrideEnabled', 1)
        except:
            pass

        try:
            if color == 1:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 4)
            elif color == 2:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 13)
            elif color == 3:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 25)
            elif color == 4:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 17)
            elif color == 5:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 17)
            elif color == 6:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 15)
            elif color == 7:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 6)
            elif color == 8:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 16)
        except:
            pass


# EXAMPLE
# set_color(['circle','circle1'], 8)


# COMMENT --------------------------------------------------
# Optimized

# CONSTANT VARIABLES
COLOR_MAP = {
    1 : 4,
    2 : 13,
    3 : 25,
    4 : 17,
    5 : 17,
    6 : 15,
    7 : 6,
    8 : 16,
}


def set_color(ctrlList=None, color=None):
    override_value = COLOR_MAP.get(color)
    for ctrlName in ctrlList:
        try:
            mc.setAttr(ctrlName + 'Shape.overrideEnabled', 1)
            mc.setAttr(ctrlName + 'Shape.overrideColor', override_value)
        except:
            pass


# EXAMPLE
# set_color(['circle','circle1'], 8)
