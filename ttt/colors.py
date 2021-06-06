'''
Provides the RGB color-tuples used by the game for drawing things in the GUI.
'''

RED = (255, 0, 0)


Color = tuple[int, int, int]

def color_to_str(c: Color) -> str:
    return '(Red, {}; Green: {}, Blue: {})'.format(c[0], c[1], c[2])
