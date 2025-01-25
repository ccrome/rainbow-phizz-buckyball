import ColorIt
import sys
from math import sqrt
from cairo import *
import math
def side_is_okay(side):
    side_is_ok = 0
    legal_sides = ['front', 'back', 'laser']
    for s in legal_sides:
        if (side == s):
            side_is_ok = 1
    if (not side_is_ok):
        raise Exception(f"Bad 'side' chosen: {sides}, legal sides are {legal_sides}")

def bucky(polygon, square_size, square_margin, fill_type='face', margin = {'left' : 0.5, 'right' : 0.5, 'top' : 0.5, 'bottom' : 0.5}, 
          sheet_size=[8.5, 11],
          side = 'front'):
    side_is_okay(side)
    width_in  = sheet_size[0] - margin['left'] - margin['right']
    inches = 1.*square_size + square_margin*2
    cols = int(width_in / inches)

    all_blocks = ColorIt.get_edges(polygon)
    ColorIt.write_adjacency_matrix(polygon, "%s_adjacency_matrix.txt" % polygon)
    face_polygons = [
        [ [0, 0], [0, 1], [2, 1], [1, 0], [0, 0] ], 
        [ [1, 0], [2, 1], [3, 1], [2, 0], [1, 0] ],
        [ [2, 0], [3, 1], [4, 1], [4, 0], [2, 0] ],
        [ [0, 4-0], [0, 4-1], [2, 4-1], [1, 4-0], [0, 4-0] ], 
        [ [1, 4-0], [2, 4-1], [3, 4-1], [2, 4-0], [1, 4-0] ],
        [ [2, 4-0], [3, 4-1], [4, 4-1], [4, 4-0], [2, 4-0] ],
        ]
    gradient_polygons = [
        [ [0, 0], [4, 0], [4, 1.1], [0, 1.1], [0, 0] ], 
        ]
    sheet_height = sheet_size[1]
    if (sheet_height == 'auto'):
        num_blocks = len(all_blocks)
        rows = int(math.ceil(1.*num_blocks/cols))
        sheet_height = (math.ceil(inches * rows) + margin['top'] + margin['bottom'])
        if (sheet_height < 9.0):
            sheet_height = 9.0
        height_in = sheet_height - margin['top'] - margin['bottom']
    else:
        height_in = sheet_height - margin['top'] - margin['bottom']
        rows = int(height_in/ inches)
    print(("Generating polygon %s, side %s, for sheet size %f x %f inches" % (polygon, side, sheet_size[0], sheet_height)))
    blocks_at_a_time = rows * cols
    images = []
    sheet = 0
    points_to_inch = 72.
    width, height = int(inches*points_to_inch*cols), int(inches*points_to_inch*rows)
    pdf_filename = "%s_%.1fx%.1f_%s.pdf" % (polygon, sheet_size[0], sheet_size[1], side)
    surface = PDFSurface(pdf_filename, sheet_size[0]*72, sheet_height*72)
        
    for b in range(0, len(all_blocks), blocks_at_a_time):
        last_block = b + blocks_at_a_time - 1
        if (last_block >= len(all_blocks)):
            last_block = len(all_blocks) - 1
        blocks = all_blocks[slice(b, last_block+1)]
        if (fill_type == 'face'):
            polygons = face_polygons
        else:
            polygons = gradient_polygons
        # white background
        ctx = Context(surface)
        points_per_inch=72.
        inches_per_square=(square_size+2*square_margin)
        points_per_square=scale=points_per_inch*inches_per_square
        scale = points_per_square/4

        if (side == 'back'):
            ctx.scale(-1, 1) # Flip left-right
            ctx.translate(-1*points_per_inch*(sheet_size[0]), 0)
            pass
        if (side == 'laser'):
            # With the laser, we want the lasering to start exactly on the crop lines.  Therefore we translate
            # negative by the block margin
            correction = square_margin*points_per_inch
            ctx.translate(-correction, -correction)
        else:
            ctx.translate(margin['left']*72., margin['top']*72.)
        ctx.scale(scale, scale)
        reverse_margin = ctx.device_to_user_distance(points_per_inch*square_margin,0)[0]
        if (side == 'back'):
            reverse_margin = -reverse_margin
        block_array(ctx, blocks, cols, rows, polygons, fill_type, reverse_margin)
        surface.show_page()
        sheet = sheet + 1

def draw_crop_marks(ctx, reverse_margin):
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(0.02)
        ctx.move_to(0, reverse_margin)
        ctx.line_to(reverse_margin/2 , reverse_margin)
        ctx.move_to(4, reverse_margin)
        ctx.line_to(4-(reverse_margin/2) , reverse_margin)
        ctx.move_to(0, 4-reverse_margin)
        ctx.line_to(reverse_margin/2 , 4-reverse_margin)
        ctx.move_to(4, 4-reverse_margin)
        ctx.line_to(4-(reverse_margin/2) , 4-reverse_margin)
        ctx.stroke()
        
        # Vertical crop marks inside the white area
        sx = reverse_margin+1
        lx = .5
        ctx.move_to( reverse_margin, sx)
        ctx.line_to( reverse_margin, sx+lx )
        ctx.stroke()
        ctx.move_to( 4-reverse_margin, sx)
        ctx.line_to( 4-reverse_margin, sx+lx )
        ctx.stroke()
        ctx.move_to( reverse_margin, 4-sx)
        ctx.line_to( reverse_margin, 4-(sx+lx) )
        ctx.stroke()
        ctx.move_to( 4-reverse_margin, 4-sx)
        ctx.line_to( 4-reverse_margin, 4-(sx+lx) )
        ctx.stroke()

def block_array(ctx, blocks, cols, rows, polygons, fill_type, reverse_margin):
    row = 0
    col = 0
    for block in blocks:
        vertex1, color1, vertex2, color2 = block[0], block[1], block[2], block[3]
        if (side != 'laser'):
            if fill_type == "face":
                face_block(ctx, vertex1, color1, vertex2, color2, polygons, reverse_margin)
            else:
                gradient_block(ctx, vertex1, color1, vertex2, color2, polygons, reverse_margin)
            # Draw horizontal line
    #        ctx.set_source_rgb(0, 0, 0)
    #        ctx.move_to(0, 2)
    #        ctx.line_to(4, 2)
    #        ctx.set_line_width(0.02)
    #        ctx.stroke()
            ctx.set_source_rgb(0, 0, 0)
            ctx.set_font_size(.2)
            ctx.move_to(reverse_margin*2, reverse_margin+2+.2*1.5)
            ctx.show_text("FRONT")
            if (row==0 and col==0):
                # Write copyright text
                ctx.move_to(reverse_margin, reverse_margin*2+1)
                ctx.show_text("Copyright 2012, Caleb Crome")
                ctx.move_to(reverse_margin, reverse_margin*2+1+.2*1.5)
                ctx.show_text("All rights reserved")
            if (row==0 and col==1):
                # Write copyright text
                ctx.move_to(reverse_margin, reverse_margin*2+1)
                ctx.show_text("Buckyball Awesomeness!")
        else:
            # Side is laser:
            ctx.set_source_rgb(0, 0, 0)
            # Set line width to 0.001 inches.
            lw = ctx.device_to_user_distance(0.001*72.0, 0)[0]
            ctx.set_line_width(lw)
                               
            ctx.move_to(reverse_margin, reverse_margin)
            ctx.line_to(4-reverse_margin, reverse_margin)
            ctx.line_to(4-reverse_margin, 4-reverse_margin)
            ctx.line_to(reverse_margin, 4-reverse_margin)
            ctx.line_to(reverse_margin, reverse_margin)
            ctx.stroke()
        col = col + 1
        if (col == cols):
            col = 0
            ctx.translate(-4*(cols), 4)
            row = row + 1
        ctx.translate(4, 0)
    return 

def face_block(ctx, vertex1, color1, vertex2, color2, polygons, reverse_margin):
    num_margin=0.1
    create_block(ctx, polygons, [color1, [0, 0, 0], color2], 
                 [[vertex1, 0+num_margin, 1-num_margin, "left" , "bottom"], [vertex2, 4-num_margin, 0+num_margin, "right", "top"   ],
                  [vertex1, 0+num_margin, 3+num_margin, "left" , "top"], [vertex2, 4-num_margin, 4-num_margin, "right", "bottom"   ]],
                 "face", reverse_margin)

def gradient_block(ctx, vertex1, color1, vertex2, color2, polygons, reverse_margin):
    num_margin=0.1
    create_block(ctx, polygons, [color1, color2],
                 [[vertex1, 0+num_margin, 1-num_margin, "left" , "bottom"], [vertex2, 4-num_margin, 0+num_margin, "right", "top"   ],
                  [vertex1, 0+num_margin, 3+num_margin, "left" , "top"], [vertex2, 4-num_margin, 4-num_margin, "right", "bottom"   ]],
#                 [[vertex1, .1, .6, "left", "bottom"], [vertex2, 3.55, .1, "right", "top"]],
                 "gradient", reverse_margin)

def create_block(ctx, polygons, colors, texts, fill_type, reverse_margin):
    color_index = 0
    if (fill_type == 'face'):
        t_colors = [colors[0], colors[2]]
        for poly in polygons:
            color = colors[color_index]
            r, g, b = color[0]/255.0, color[1]/255.0, color[2]/255.0
            ctx.set_source_rgb(r, g, b)
            ctx.move_to(poly[0][0], poly[0][1])
            for pi in range(1, len(poly)):
                ctx.line_to(poly[pi][0], poly[pi][1])
            ctx.close_path()
            ctx.fill()
            color_index = (color_index + 1) % len(colors)
    elif (fill_type == 'gradient'):
        t_colors = colors
        # Top gradient
        g = LinearGradient(0, 1, 4, 0)
        r0, g0, b0 = colors[0][0]/255., colors[0][1]/255., colors[0][2]/255.
        r1, g1, b1 = colors[1][0]/255., colors[1][1]/255., colors[1][2]/255.
        g.add_color_stop_rgb(.2, r0, g0, b0)
        g.add_color_stop_rgb(.8, r1, g1, b1)
        ctx.rectangle(0, 0, 4, 1+reverse_margin)
        ctx.set_source(g)
        ctx.fill()

        # Bottom gradient
        g = LinearGradient(0, 3, 4, 4)
        g.add_color_stop_rgb(.2, r0, g0, b0)
        g.add_color_stop_rgb(.8, r1, g1, b1)
        ctx.rectangle(0, 3-reverse_margin, 4, 1+reverse_margin)
        ctx.set_source(g)
        ctx.fill()

        # Center Gradient
        g = LinearGradient(0, 2, 4, 2)
        g.add_color_stop_rgb(.2, r0, g0, b0)
        g.add_color_stop_rgb(.8, r1, g1, b1)
        ctx.rectangle(0, 1.8, 4, .4)
        ctx.set_source(g)
        ctx.fill()

    else:
        raise Exception("Unknown fill type %s" % fill_type)

    for i in range(len(texts)):
        text = texts[i]
        r, g, b = reverse_color(t_colors[i % len(t_colors)])
        string      = text[0]
        x           = text[1]
        y           = text[2]
        xalign      = text[3]
        yalign      = text[4]
        if (math.sqrt((r*r+g*g+b*b) / 3) < 128):
            ctx.set_source_rgb(0, 0, 0)
        else:
            ctx.set_source_rgb(1, 1, 1)
        ctx.select_font_face("Georgia", FONT_SLANT_NORMAL, FONT_WEIGHT_BOLD)
        text_size = .2
        ctx.set_font_size(text_size)
        xx, yy = text_offset(ctx, string, xalign, yalign, reverse_margin)
        ctx.move_to(x + xx, y + yy)
        ctx.show_text(string)
    # Draw crop marks
    draw_crop_marks(ctx, reverse_margin)
        

def text_offset(ctx, string, xalign, yalign, reverse_margin):
    x_bearing, y_bearing, width, height = ctx.text_extents(string)[:4]
    if (xalign == 'right'):
        xx = 0 - x_bearing - width - reverse_margin
    else:
        xx = 0 + x_bearing + reverse_margin
    if (yalign == 'top'):
        yy = 0 - y_bearing + reverse_margin
    else:
        yy = 0 - y_bearing - height - reverse_margin
    return xx, yy
        
def reverse_color(color):
    r = []
    for c in color:
        r.append(255.-c)
    return r



square_size = 1.5 # in inches
#sheet_size = [24, 14]
#margin     = {'left' : 0.5, 'right' : 0.5, 'top' : 0.5, 'bottom' : .75}


#sheet_size = [36, 18]
#margin     = {'left' : 0.5, 'right' : 12.5, 'top' : 0.5, 'bottom' : .75}


sheet_size = [8.5, 11]
margin     = {'left' : 0.5, 'right' : 0.5, 'top' : 0.5, 'bottom' : .5}

for shape in ["dodecahedron", "buckyball", "buckyball_240"]:
    for side in ['front', 'back', 'laser']:
        bucky(shape , square_size = square_size, square_margin=.1, fill_type='gradient', margin = margin, sheet_size = sheet_size, side=side)

#bucky("torus_5_10",
#bucky("icosohedron" 

