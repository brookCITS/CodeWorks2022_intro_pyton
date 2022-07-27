import arcade
screen_width = 600
screen_height = 600
screen_title = "New Game"

arcade.open_window(screen_width, screen_height, screen_title)

arcade.set_background_color( (0,0,0))
arcade.start_render( )

def draw_pine_tree(x, y):
    #draws a pine tree at the specified location
    arcade.draw_triangle_filled(x+40, y, x, y-100, x+80, y-100, (0,255,0))
    arcade.draw_lrtb_rectangle_filled(x+30,x+50, y-100,y-140, (0,255,0))

x = 200
y = 200
r = 22
color = (0,255,0)
draw_pine_tree(200,220)
arcade.draw_circle_filled(x, y, r, color)

arcade.draw_lrtb_rectangle_filled(20, 23, 400, 200, (0,255,0))



arcade.finish_render( )
arcade.run()
