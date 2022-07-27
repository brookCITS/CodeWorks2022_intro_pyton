import arcade

screen_width = 600
screen_height = 600
screen_title = "New Game"

arcade.open_window(screen_width, screen_height, screen_title)

arcade.set_background_color( arcade.color.PINK_SHERBET)
arcade.start_render( )


#drawing code here
arcade.draw_circle_filled(125, 300, 55, arcade.color.BLACK)
arcade.draw_circle_filled(475, 300, 55, arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(88,512, 140, 88, arcade.color.RED)

arcade.finish_render( )


arcade.run()
