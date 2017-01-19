# Created by: James Sanii
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the help scene.

from scene import *
import ui

from main_menu_scene import *


class HelpScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'blue', 
                                     parent = self, 
                                     size = self.size)
        #rules for game, and thier locations
        self.rule_1_position = Vector2()
        self.rule_1_position.x= self.size.x / 2
        self.rule_1_position.y = self.size.y / 1.2
        self.rule_1 = LabelNode(text = 'Try to match sets of 3 or more gems.',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = self.rule_1_position)
        self.rule_2_position = Vector2()
        self.rule_2_position.x= self.size.x / 2
        self.rule_2_position.y = self.size.y / 1.5
        self.rule_2 = LabelNode(text = 'The game is played by tapping one gem, then tapping another to swap gems. ',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = self.rule_2_position)
        self.rule_3_position = Vector2()
        self.rule_3_position.x= self.size.x / 2
        self.rule_3_position.y = self.size.y / 3
        self.rule_3 = LabelNode(text = ' To gain points swap gems to create sets of 3 or more matching gems. ',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = self.rule_3_position)
        self.rule_4_position = Vector2()
        self.rule_4_position.x= self.size.x / 2
        self.rule_4_position.y = self.size.y / 2.5
        self.rule_4 = LabelNode(text = ' When matched, the gems will be removed and be replaced by random gems.',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = self.rule_4_position)
        self.rule_5_position = Vector2()
        self.rule_5_position.x= self.size.x / 2
        self.rule_5_position.y = self.size.y / 4
        self.rule_5 = LabelNode(text = 'The larger the match the more points you will get.',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = self.rule_5_position)
        #create back button position
        back_button_position = Vector2()
        back_button_position.x = self.size.x / 8
        back_button_position.y = self.size.y / 1.25
        #create back button
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                       parent = self,
                                       position = back_button_position)
        
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
        
        # if back button is pressed, go to main menu scene
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
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
