import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Python Landscape Drawing"

def draw_background():
    arcade.draw_lrtb_rectangle_filled(0, 
            SCREEN_WIDTH,SCREEN_HEIGHT, SCREEN_HEIGHT * (1/3),
            arcade.color.SKY_BLUE)
    arcade.draw_lrtb_rectangle_filled(0,
            SCREEN_WIDTH, SCREEN_HEIGHT/3, 0,
            arcade.color.DARK_SPRING_GREEN)

def draw_bird(x, y):
    arcade.draw_arc_outline(x, y, 20, 20, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(x + 40, y, 20, 20, arcade.color.BLACK, 90, 180)

def draw_pine_tree(x,y):
    arcade.draw_triangle_filled(x + 40, y, x, y - 100, x + 80, y - 100, 
            arcade.color.DARK_GREEN)

    arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140, arcade.color.DARK_BROWN)

def draw_sun(x,y):
    arcade.draw_circle_filled(x, y, 80, arcade.color.YELLOW, 0)

def main():
    
    #init window 
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.start_render()

    draw_background()
    draw_pine_tree(50, 250)
    draw_pine_tree(350, 320)
    draw_pine_tree(700, 270)
    draw_pine_tree(850, 300)
    draw_bird(70, 500)
    draw_bird(470, 550)
    draw_sun(700, 500)
    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()
