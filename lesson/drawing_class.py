import arcade
screen_width = 600
screen_height = 600
screen_title = "New Game"


class Charachter:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def update(self, delta_time):
        #all logic for moving and the game logic
        pass

    def on_key_press(self, key, key_modifiers):
        #called when keyboard is pressed
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        #called when the mouse is moved
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        #called when the mouse is clicked
        pass


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        #create carachters and set up the game
        pass

    def on_draw(self):
        #Render the screen
        arcade.start_render()

def main():
    game = MyGame(screen_width, screen_height, screen_title)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
