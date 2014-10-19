# Color definitions
# Using solarized colorscheme from cheatsheet:
# http://www.zovirl.com/2011/07/22/solarized_cheat_sheet/

base03 =  (0  , 43 , 54 )
base02 =  (7  , 54 , 66 )
base01 =  (88 , 110, 117)
base00 =  (101, 123, 131)
base0  =  (131, 148, 150)
base1  =  (147, 161, 161)
base2  =  (238, 232, 213)
base3  =  (253, 246, 227)
yellow =  (181, 137, 0  )
orange =  (203, 75 , 22 )
red    =  (220, 50 , 47 )
magenta=  (211, 54 , 130)
violet =  (108, 113, 196)
blue   =  (38 , 139, 210)
cyan   =  (42 , 161, 152)
green  =  (133, 153, 0  )

base = [0]*8
base[0] = base0
base[1] = base1
base[2] = base2
base[3] = base3
base[4] = base00
base[5] = base01
base[6] = base02
base[7] = base03

color = [0]*8
color[0] = yellow
color[1] = orange
color[2] = red
color[3] = magenta
color[4] = violet
color[5] = blue
color[6] = cyan
color[7] = green


def rgba(color, a=(255,)):
    """
    Cocos often requires an rgb input with opacity as well (0-255)
    This function returns the color vector with an attached opacity
    """
    return color + a

