# code fait par Viktor

y = 0
x = 560
valuea = 13
valueb = 18


def rosevent(x):

    while x > 360:
        x = x - 360
    if x < 23:
        y = "NNE", x, "°"
    if 45 > x > 23:
        y = "NE", x, "°"
    if 68 >= x > 45:
        y = "ENE", x, "°"
    if 90 >= x > 68:
        y = "E", x, "°"
    if 113 >= x > 90:
        y = "ESE", x, "°"
    if 135 >= x > 113:
        y = "SE", x, "°"
    if 158 >= x > 135:
        y = "SSE", x, "°"
    if 180 >= x > 158:
        y = "S", x, "°"
    if 203 >= x > 180:
        y = "SSW", x, "°"
    if 225 >= x > 203:
        y = "SW", x, "°"
    if 248 >= x > 225:
        y = "WSW", x, "°"
    if 270 >= x > 248:
        y = "W", x, "°"
    if 293 >= x > 270:
        y = "WNW", x, "°"
    if 315 >= x > 293:
        y = "NW", x, "°"
    if 338 >= x > 315:
        y = "NNW", x, "°"
    if 360 >= x > 338:
        y = "N", x, "°"


o = open("./js/setvalue.js", "a")
o.truncate(0)
o.write("""document.getElementById("VM") = "Vent Moyen:  """)
a = str(valuea)
o.write(a)
o.write(""" " """)
o.write("\n")
o.write("""document.getElementById("VR") = "Vent en Rafale :  """)
b = str(valueb)
o.write(b)
o.write(""" " """)
o.write("\n")
o.write("""document.getElementById("DV") = "Direction du Vent :  """)
y = str(y)
o.write(y)
o.write(""" " """)
exit
