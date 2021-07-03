#!/usr/bin/env python3

import math

RT2 = math.sqrt(2)
RT3 = math.sqrt(3)
ROUNDTO = 2

# paper format is A4
width, height = 210, 297 # millimeters

dotsize = 1

numy = 30 #number of points on vertical axis
numx = int(round( numy * RT2 / RT3, 4))

scale = height / numy
pad_x = (width - numx * scale * RT3 / 2) / 2 


allpoints = []

for yi in range(numy):
    for xi in range(numx):
        allpoints += [(round(xi * RT3 * scale + pad_x, ROUNDTO), round(yi * scale, ROUNDTO))]
    for xi in range(numx - 1):
        allpoints += [(round((xi + 0.5) * RT3 * scale + pad_x, ROUNDTO), round((yi + 0.5) * scale, ROUNDTO))]

file = open("my_dot_paper.svg", "w")

svg_header = '<?xml version="1.0" encoding="utf-8" ?>'
svg_header += '<svg xmlns="http://www.w3.org/2000/svg" xmlns:ev="http://www.w3.org/2001/xml-events" xmlns:xlink="http://www.w3.org/1999/xlink" '
svg_header += 'baseProfile="tiny" version="1.2" '
svg_header += 'width="100%" height="100%" viewBox="{},{},{},{}">'.format(0, 0, width, height)
svg_defs = '<defs />'

file.write(svg_header)
file.write(svg_defs)

for p in allpoints:
    file.write('<circle cx="{}" cy="{}" fill="black" r="{}" />'.format(p[0], p[1], dotsize))

file.write('</svg>')

file.close()
