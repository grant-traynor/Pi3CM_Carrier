#!/usr/bin/python
import csv

topleft = {'x': 47000, 'y': 43000}
dimensions = {'x':3000, 'y': 12700}
vspace = 200
pinlen = 500
textoffset = {'x': 55, 'y': -5}
pinidoffset = {'x': -95, 'y': 45}

pinout_fh = open('ComputeModulePinouts.csv')
pinout_csv = csv.reader(pinout_fh)
pinout = []

header = True
for x in pinout_csv:
    if header:
        header = False
        continue

    pinout.append(x)

leftpin_template = """P {0} {2} {1} {2} 1 0 0
{{
T {0} {2} 5 10 0 0 0 0 1
pintype={9}
T {4} {5} 5 10 1 1 0 0 1
pinlabel={8}
T {6} {7} 5 10 1 1 0 6 1
pinnumber={3}
T {0} {2} 5 10 0 0 0 0 1
pinseq={3}
}} """
rightpin_template = """P {0} {2} {1} {2} 1 0 0
{{
T {0} {2} 5 10 0 0 0 0 1
pintype={9}
T {4} {5} 5 10 1 1 0 6 1
pinlabel={8}
T {6} {7} 5 10 1 1 0 0 1
pinnumber={3}
T {0} {2} 5 10 0 0 0 0 1
pinseq={3}
}} """
pin_templates = [ rightpin_template, leftpin_template ]

for pin in pinout:
    pinid = int(pin[0])
    pinname = pin[1]
    pintype = pin[2]

    if pinid % 2:
        pin_start_x = topleft['x'] - pinlen
        pin_stop_x  = topleft['x'] 
        pin_y = topleft['y'] - vspace/2 - vspace * int(pinid/2)
        textx = pin_stop_x + textoffset['x']
        texty = pin_y + textoffset['y']
        pinidx = pin_stop_x + pinidoffset['x']
        pinidy = pin_y + pinidoffset['y']
        pin_template = pin_templates[pinid%2].format( int(pin_start_x), 
                                                      int(pin_stop_x), 
                                                      int(pin_y), 
                                                      int(pinid),
                                                      int(textx),
                                                      int(texty),
                                                      int(pinidx),
                                                      int(pinidy),
                                                      pinname,
                                                      pintype)
        print( pin_template )
    else:
        pin_start_x = topleft['x'] + dimensions['x'] + pinlen
        pin_stop_x  = topleft['x'] + dimensions['x']
        pin_y = topleft['y'] - vspace/2 - vspace * int(pinid/2)
        textx = pin_stop_x + textoffset['x']
        texty = pin_y + textoffset['y']
        pinidx = pin_stop_x + pinidoffset['x']
        pinidy = pin_y + pinidoffset['y']
        pin_template = pin_templates[pinid%2].format( int(pin_start_x), 
                                                      int(pin_stop_x), 
                                                      int(pin_y), 
                                                      int(pinid),
                                                      int(textx),
                                                      int(texty),
                                                      int(pinidx),
                                                      int(pinidy),
                                                      pinname,
                                                      pintype)
        print( pin_template )

