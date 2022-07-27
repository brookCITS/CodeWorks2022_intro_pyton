import arcade

screen_width = 600
screen_height = 600
screen_title = "New Game"

arcade.open_window(screen_width, screen_height, screen_title)

arcade.set_background_color( (255,255,255))
arcade.start_render( )

x = 300
y = 300
r = 200
color = (255, 255, 0)
arcade.draw_circle_filled(x, y, r, color)

x = 370
y = 350
r = 20
color = (0, 0, 0)
arcade.draw_circle_filled(x, y, r, color)

x = 230
y = 350
color = (0, 0, 0)
arcade.draw_circle_filled(x, y, r, color)

x = 300
y = 250
width = 220
height = 155
color = (0, 0, 0)
start_angle = 190
end_angle = 350
line_width = 10

arcade.draw_arc_outline(x,y,width, height, color, start_angle, end_angle, line_width)




arcade.finish_render( )


arcade.run()
