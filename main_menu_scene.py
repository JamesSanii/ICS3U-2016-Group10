# Created by: James Sanii
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui

from game_scene import *
from help_scene import *
from credits import *

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
        #create start button
        self.start_button = SpriteNode('./assets/sprites/start.png',
                                       parent = self,
                                       position = self.size/2)
        #create help button position
        self.help_button_position = self.size/2
        self.help_button_position.y = self.help_button_position.y/2
        #create help button
        self.help_button = SpriteNode('./assets/sprites/help.png',
                                       parent = self,
                                       position = self.help_button_position)
        #create credits button position
        self.credits_button_position = Vector2()
        self.credits_button_position.y = self.size.y/1.3
        self.credits_button_position.x = self.size.x/2
        #create credits button
        self.credits_button = SpriteNode('./assets/sprites/Credits.PNG',
                                       parent = self,
                                       position = self.credits_button_position,
                                       scale = 3)
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, go to game scene
        if self.start_button.frame.contains_point(touch.location):
            self.present_modal_scene(GameScene())
            
        # if help button is pressed, go to help scene
        if self.help_button.frame.contains_point(touch.location):
            self.present_modal_scene(HelpScene())
        # if credits button is pressed, go to credits scene
        if self.credits_button.frame.contains_point(touch.location):
            self.present_modal_scene(CreditsScene())
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
