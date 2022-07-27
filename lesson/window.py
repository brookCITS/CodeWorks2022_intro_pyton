import arcade

screen_width = 600
screen_height = 600
screen_title = "New Game"

arcade.open_window(screen_width, screen_height, screen_title)

arcade.set_background_color( (255,255,255))
arcade.start_render( )


#drawing code here


arcade.finish_render( )


arcade.run()
