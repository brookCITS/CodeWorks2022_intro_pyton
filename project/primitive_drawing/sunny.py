#import arcade module
import arcade

#define screen properties (width, height, and title)
screen_width = 600
screen_height = 600
screen_title = "New Game"

#open window
arcade.open_window(screen_width, screen_height, screen_title)

#set background color
arcade.set_background_color( (0,0,0))
#start render
arcade.start_render( )

#drawing code here


#finish render
arcade.finish_render( )
#run
arcade.run()
