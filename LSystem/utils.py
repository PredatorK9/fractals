import math

chosen = 'bush2'
length = 20

systemType = {
    '0L': {
        'rule': {
            'F':'F+F-F-FF+F+F-F',
        },
        'angle': 90,
        'axiom': 'F+F+F+F'
    },

    'bush1': {
        'rule': {
            'X': 'X[-FFF][+FFF]FX',
            'Y': 'YFX[+Y][-Y]'
        },
        'angle': 25.7,
        'axiom': 'Y'
    },

    'bush2': {
        'rule': {
            'F':'FF+[+F-F-F]-[-F+F+F]'
        },
        'angle': 22.5,
        'axiom': 'F'
    },

    'bush3': {
        'rule': {
            'F':'F[+FF][-FF]F[-F][+F]F'
        },
        'angle': 35,
        'axiom': 'F'
    },

    'triangle': {
        'rule': {
            'F':'F-F+F'
        },
        'angle': 120,
        'axiom': 'F+F+F'
    },

    'crystal' : {
        'rule' : {
            'F' : 'FF+F++F+F'
        },
        'angle':90,
        'axiom': 'F+F+F+F'
    },

    'square sierpinski':{
        'rule': {
            'X': 'XF-F+F-XF+F+XF-F+F-X'
        },
        'angle': 90,
        'axiom': 'F+XF+F+XF'
    },

    'sticks':{
        'rule': {
            'F': 'FF',
            'X': 'F[+X]F[-X]+X'
        },
        'angle': 20,
        'axiom': 'X'
    },

    'snowflake': {
        'rule': {
            'F': 'F-F+F+F-F'
        },
        'angle':90,
        'axiom':'F'
    },

    'board': {
        'rule': {
            'F': 'FF+F+F+F+FF'
        },
        'angle':90,
        'axiom':'F+F+F+F'
    },

    'dragon': {
        'rule': {
            'X': 'X+YF+',
            'Y': '-FX-Y'
        },
        'angle':90,
        'axiom':'FX'
    },

    'koch snowflake': {
        'rule': {
            'F': 'F-F++F-F'
        },
        'angle':60,
        'axiom': 'F++F++F'
    },

    'arrowhead': {
        'rule': {
            'X' : 'YF+XF+Y',
            'Y' : 'XF-YF-X'
        },
        'angle':60,
        'axiom':'YF'
    }
}

def axiom_init():
    return systemType[chosen]['axiom']
remember = []

def turtle(func, character, posX, posY, angle, x, y):
    decimal = angle - int(angle)
    angle = int(angle) % 360
    angle = angle + decimal

    if character == '+':
        angle = angle + systemType[chosen]['angle']
    elif character == '-':
        angle = angle - systemType[chosen]['angle']

    x = math.sin(math.radians(angle)) * length
    y = math.cos(math.radians(angle)) * length

    if character == '[':
        remember.append((posX, posY, angle))
    elif character == ']':
        posX, posY, angle = remember.pop()

    elif character == 'f':
        posX = posX + x
        posY = posY + y

    elif character == 'F':
        posX, posY = func((posX, posY), (posX + x, posY + y))  

    return (posX, posY), angle, x, y


def generate(axiom):
    newSentence = ''
    for character in axiom:
        if character in systemType[chosen]['rule']:
            newSentence = newSentence + systemType[chosen]['rule'][character]
        else:
            newSentence = newSentence + character

    return newSentence