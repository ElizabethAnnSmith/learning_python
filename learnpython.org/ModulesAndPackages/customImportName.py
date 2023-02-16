# Modules may be loaded under any name you want. Useful when importing a module conditionally to use the same name in the rest of the code.
# For example, if you have two 'draw' modules using slightly different names, you can ...
# game.py
# import the draw module
if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)
