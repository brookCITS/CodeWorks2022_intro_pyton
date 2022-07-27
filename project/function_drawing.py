import arcade
screen_width = 600
screen_height = 600
screen_title = "New Game"

def draw_bird(x, y):


def main():
    arcade.open_window(screen_width, screen_height, screen_title)
    #set background color
    arcade.set_background_color( (0,0,0))
    
    arcade.start_render( )

    #call drawing functioncs


    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()
