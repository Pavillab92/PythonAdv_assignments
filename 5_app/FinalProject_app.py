#***************************************************************************************************
# Name       = LIMB ASSISTANT (WPI).
# Content    = Quickly create FK and Ik setups with stretchable attributes.

# Version    = 1.0.0 beta
# Date       = 30-07-2026

# Dependency = Maya Command.
# How_to     = Quick tutorial on how to activate this script.
# Todo       = If script requieres changes or updates, list them here.

# License    = MIT <https://github.com/Pavillab92>
# Author     = Pablo Villasenor B. | Character TD | Rigger
# Portfolio  = pavillab.artstation.com
#***************************************************************************************************

# Variable names NOT FINAL change them.

from maya import cmds as mc

# CONSTANT
ACTIVE = []
CONSTVAR_2 = 'Constant variable 2'
CONSTVAR_3 = 'Constant variable 3'



# Create FK setup

'''
que necesito?
1. encontrar mi seleccion, identificar su tipo sea joint
2. crear 2 funciones, si es FK o IK
3. (si es FK crear un control en cada hueso )
'''



def active_selection(param1=None):
    sel = mc.ls(selection=True, long=True, type='joint')
    for obj in sel:
        sep = obj.split('|')[-1]
        ACTIVE.append(sep)
    return ACTIVE


active_selection()

def fk_or_ik(parameter1=None):
    print('use this function to choose if selecton is FK or IK chain')