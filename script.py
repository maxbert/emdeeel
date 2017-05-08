import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    ARG_COMMANDS = [ 'line', 'scale', 'move', 'rotate', 'save', 'circle', 'bezier', 'hermite', 'box', 'sphere', 'torus' ]
    
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)
    step = 0.1
    systems = [ temp ]
    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    ident(tmp)
    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    tmp = []
    step = 0.1
    clear_screen(screen)
    for command in commands:
        if command[0] in ARG_COMMANDS:
            args = command[1:]

        if command[0] == "sphere":
            add_sphere(edges,float(args[0]), float(args[1]), float(args[2]),float(args[3]), step)
            matrix_mult( systems[-1], edges )
            draw_polygons(edges, screen, color)
            edges = []
        elif command[0] == 'torus':
            #print 'TORUS\t' + str(args)
            add_torus(edges,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), step)
            matrix_mult( systems[-1], edges )
            draw_polygons(edges, screen, color)
            edges = []
        elif command[0] == 'box':
            #print 'BOX\t' + str(args)
            add_box(edges,
                    float(args[0]), float(args[1]), float(args[2]),
                    float(args[3]), float(args[4]), float(args[5]))
            matrix_mult( systems[-1], edges )
            draw_polygons(edges, screen, color)
            edges = []
        elif line == 'circle':
            #print 'CIRCLE\t' + str(args)
            add_circle(edges,
                       float(args[0]), float(args[1]), float(args[2]),
                       float(args[3]), step)

        elif command == 'hermite' or command == 'bezier':
            #print 'curve\t' + line + ": " + str(args)
            add_curve(edges,
                      float(args[0]), float(args[1]),
                      float(args[2]), float(args[3]),
                      float(args[4]), float(args[5]),
                      float(args[6]), float(args[7]),
                      step, line)                      
        elif command == 'line':            
            #print 'LINE\t' + str(args)

            add_edge( edges,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), float(args[5]) )

        print command
